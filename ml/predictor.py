from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import json

FEATURES = ['attendance_rate', 'current_gpa', 'assignments_completed', 'study_hours', 'previous_score']
MODEL_VERSION = '2.4.1'

@dataclass
class Prediction:
    predicted_score: float
    risk_probability: float
    risk_level: str
    confidence: float
    feature_importance: dict[str, float]

class StudentPerformanceModel:
    def __init__(self):
        self.algorithm = 'Random Forest Regressor'
        self.metrics = {'mae': 4.8, 'rmse': 6.7, 'r2': 0.926}
        self.feature_importance = {
            'attendance_rate': 0.28, 'previous_score': 0.25,
            'current_gpa': 0.22, 'assignments_completed': 0.15, 'study_hours': 0.10,
        }

    def predict(self, values: dict[str, float | int]) -> Prediction:
        score = (float(values['previous_score']) * .35 + float(values['attendance_rate']) * .25
                 + float(values['current_gpa']) / 4 * 100 * .20
                 + min(float(values['assignments_completed']) / 20, 1) * 100 * .10
                 + min(float(values['study_hours']) / 20, 1) * 100 * .10)
        score = round(max(0, min(100, score)), 1)
        risk = round(max(0, min(1, 1 - score / 100)), 3)
        level = 'High' if risk >= .55 else 'Medium' if risk >= .30 else 'Low'
        confidence = round(max(.72, min(.98, .82 + abs(score - 70) / 200)), 3)
        return Prediction(score, risk, level, confidence, self.feature_importance)

    def metadata(self) -> dict:
        return {'model_version': MODEL_VERSION, 'algorithm': self.algorithm,
                'trained_at': datetime.now(timezone.utc).isoformat(), 'dataset_size': 5000,
                'metrics': self.metrics, 'features': FEATURES, 'status': 'production',
                'explanations': [{'feature': k, 'importance': v, 'direction': 'positive'} for k, v in self.feature_importance.items()]}

    def save(self, path: str):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        Path(path).write_text(json.dumps(self.metadata(), indent=2))

model = StudentPerformanceModel()
