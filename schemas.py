from pydantic import BaseModel, Field
from typing import Literal

class PredictionInput(BaseModel):
    attendance_rate: float = Field(ge=0, le=100)
    current_gpa: float = Field(ge=0, le=4)
    assignments_completed: int = Field(ge=0, le=100)
    study_hours: float = Field(ge=0, le=168)
    previous_score: float = Field(ge=0, le=100)

class PredictionResult(BaseModel):
    predicted_score: float
    risk_probability: float
    risk_level: Literal['Low', 'Medium', 'High']
    confidence: float
    model_version: str
    feature_importance: dict[str, float]

class StudentCreate(BaseModel):
    student_id: str = Field(min_length=2, max_length=64)
    name: str = Field(min_length=2, max_length=120)
    program: str = Field(min_length=2, max_length=120)
    attendance_rate: float = Field(ge=0, le=100)
    current_gpa: float = Field(ge=0, le=4)
    assignments_completed: int = Field(ge=0, le=100)
    study_hours: float = Field(ge=0, le=168)
    previous_score: float = Field(ge=0, le=100)

class StudentUpdate(StudentCreate):
    pass

class InterventionCreate(BaseModel):
    student_id: str
    intervention_type: str
    notes: str = Field(default='', max_length=1000)

class HealthResponse(BaseModel):
    status: str
    service: str
    model_version: str
    database: str

class AnalyticsResponse(BaseModel):
    total_students: int
    average_score: float
    at_risk_students: int
    average_confidence: float
    risk_distribution: dict[str, int]
    score_trend: list[dict[str, float | str]]
    model_metrics: dict[str, float]
    feature_importance: dict[str, float]
    recent_predictions: list[dict[str, str | float]]

class StudentResponse(BaseModel):
    student_id: str
    name: str
    program: str
    email: str | None = None
    predicted_score: float = 0
    risk_level: str = 'Unknown'
    created_at: str

class InterventionResponse(BaseModel):
    id: str
    student_id: str
    title: str
    description: str
    status: str
    created_at: str

class ModelResponse(BaseModel):
    model_version: str
    algorithm: str
    trained_at: str
    dataset_size: int
    metrics: dict[str, float]
    features: list[str]
    status: str
    explanations: list[dict[str, str | float]]
