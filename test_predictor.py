from .ml.predictor import StudentPerformanceModel

def test_prediction_is_bounded():
    result = StudentPerformanceModel().predict({'attendance_rate': 86, 'current_gpa': 3.4, 'assignments_completed': 18, 'study_hours': 14, 'previous_score': 78})
    assert 0 <= result.predicted_score <= 100
    assert result.risk_level in {'Low', 'Medium', 'High'}
    assert 0 <= result.risk_probability <= 1

def test_low_inputs_are_high_risk():
    result = StudentPerformanceModel().predict({'attendance_rate': 20, 'current_gpa': 1.0, 'assignments_completed': 2, 'study_hours': 1, 'previous_score': 25})
    assert result.risk_level == 'High'
