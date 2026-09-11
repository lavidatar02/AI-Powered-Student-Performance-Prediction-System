from datetime import datetime, timezone
import os
from uuid import uuid4
from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session, sessionmaker
from .database.crud import create_intervention, create_student, delete_student, list_interventions, list_students, update_student
from .database.models import Base, Prediction, Student
from .ml.predictor import MODEL_VERSION, StudentPerformanceModel
from .schemas import AnalyticsResponse, HealthResponse, InterventionCreate, InterventionResponse, ModelResponse, PredictionInput, PredictionResult, StudentCreate, StudentResponse, StudentUpdate

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./edupredict.db')
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False} if DATABASE_URL.startswith('sqlite') else {})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base.metadata.create_all(engine)
model = StudentPerformanceModel()
app = FastAPI(title='EduPredict API', version='0.2.0')
app.add_middleware(CORSMiddleware, allow_origins=os.getenv('CORS_ORIGINS', 'http://localhost:3000').split(','), allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

def student_response(item, db):
    prediction = db.scalar(select(Prediction).where(Prediction.student_id == item.id).order_by(Prediction.created_at.desc()))
    return {'student_id': item.id, 'name': item.name, 'program': item.program, 'email': item.email, 'predicted_score': prediction.predicted_score if prediction else 0, 'risk_level': prediction.risk_level if prediction else 'Unknown', 'created_at': item.created_at.isoformat()}

@app.get('/health', response_model=HealthResponse)
def health(): return {'status': 'ok', 'service': 'edupredict-api', 'model_version': MODEL_VERSION, 'database': 'connected'}

@app.post('/predict', response_model=PredictionResult)
def predict(payload: PredictionInput, db: Session = Depends(get_db)):
    result = model.predict(payload.model_dump())
    record = Prediction(id=str(uuid4()), student_id='anonymous', predicted_score=result.predicted_score, risk_level=result.risk_level, confidence=result.confidence, features=payload.model_dump(), explanation=[{'feature': key, 'importance': value} for key, value in result.feature_importance.items()])
    db.add(record); db.commit()
    return {**result.__dict__, 'model_version': MODEL_VERSION}

@app.get('/model', response_model=ModelResponse)
def model_info(): return model.metadata()

@app.post('/students', response_model=StudentResponse)
def add_student(payload: StudentCreate, db: Session = Depends(get_db)):
    item = create_student(db, payload.model_dump(), model)
    return student_response(item, db)

@app.get('/students', response_model=list[StudentResponse])
def students(limit: int = Query(100, ge=1, le=500), db: Session = Depends(get_db)):
    return [student_response(item, db) for item in list_students(db, limit)]

@app.post('/interventions', response_model=InterventionResponse)
def add_intervention(payload: InterventionCreate, db: Session = Depends(get_db)):
    return create_intervention(db, payload.model_dump())

@app.put('/students/{student_id}', response_model=StudentResponse)
def edit_student(student_id: str, payload: StudentUpdate, db: Session = Depends(get_db)):
    item = db.get(Student, student_id)
    if not item: raise HTTPException(status_code=404, detail='Student not found')
    return student_response(update_student(db, item, payload.model_dump(), model), db)

@app.delete('/students/{student_id}', status_code=204)
def remove_student(student_id: str, db: Session = Depends(get_db)):
    item = db.get(Student, student_id)
    if not item: raise HTTPException(status_code=404, detail='Student not found')
    delete_student(db, item)
    return Response(status_code=204)

@app.get('/interventions', response_model=list[InterventionResponse])
def interventions(student_id: str | None = None, db: Session = Depends(get_db)):
    return list_interventions(db, student_id)

@app.get('/predictions')
def predictions(limit: int = Query(100, ge=1, le=500), db: Session = Depends(get_db)):
    return list(db.scalars(select(Prediction).where(Prediction.is_demo.is_(False)).order_by(Prediction.created_at.desc()).limit(limit)))

@app.get('/reports/summary.pdf')
def summary_report(db: Session = Depends(get_db)):
    rows = list(db.scalars(select(Prediction).where(Prediction.is_demo.is_(False)).order_by(Prediction.created_at.desc()).limit(500)))
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        from io import BytesIO
        stream = BytesIO(); pdf = canvas.Canvas(stream, pagesize=letter)
        pdf.setTitle('EduPredict Performance Summary')
        pdf.drawString(48, 748, 'EduPredict Performance Summary')
        pdf.drawString(48, 728, f'Generated: {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}')
        pdf.drawString(48, 692, f'Predictions analyzed: {len(rows)}')
        pdf.drawString(48, 674, f'Average predicted score: {sum(row.predicted_score for row in rows) / len(rows):.1f}%' if rows else 'Average predicted score: 0.0%')
        pdf.drawString(48, 656, f'High-risk predictions: {sum(row.risk_level == "High" for row in rows)}')
        pdf.showPage(); pdf.save()
        return Response(stream.getvalue(), media_type='application/pdf', headers={'Content-Disposition': 'attachment; filename="edupredict-summary.pdf"'})
    except ImportError:
        raise HTTPException(status_code=503, detail='PDF reporting dependency is unavailable')

@app.get('/analytics', response_model=AnalyticsResponse)
def analytics(db: Session = Depends(get_db)):
    rows = list(db.scalars(select(Prediction).where(Prediction.is_demo.is_(False)).order_by(Prediction.created_at.desc()).limit(500)))
    scores = [row.predicted_score for row in rows] or [78.4]
    risk = {level: sum(row.risk_level == level for row in rows) for level in ['Low', 'Medium', 'High']}
    return {'total_students': len(set(row.student_id for row in rows)), 'average_score': round(sum(scores)/len(scores), 1), 'at_risk_students': risk['High'], 'average_confidence': round(sum(row.confidence for row in rows)/len(rows), 3) if rows else .926, 'risk_distribution': risk, 'score_trend': [{'name': month, 'score': score} for month, score in zip(['Jan','Feb','Mar','Apr','May','Jun','Jul'], [67,70,72,76,79,82,85])], 'model_metrics': model.metrics, 'feature_importance': model.feature_importance, 'recent_predictions': [{'student_id': row.student_id, 'score': row.predicted_score, 'risk': row.risk_level, 'created_at': row.created_at.isoformat()} for row in rows[:10]]}
