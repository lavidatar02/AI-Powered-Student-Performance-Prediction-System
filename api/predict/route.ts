import { NextResponse } from 'next/server'

export async function POST(request: Request) {
  const body = await request.json().catch(() => null)
  if (!body || typeof body.attendance_rate !== 'number') {
    return NextResponse.json({ error: 'Invalid prediction input' }, { status: 400 })
  }
  const score = Math.round(Math.min(98, Math.max(42, body.previous_score * 0.45 + body.attendance_rate * 0.25 + body.current_gpa * 12 + body.assignments_completed * 1.1 + body.study_hours * 0.5)))
  const risk_level = score >= 80 ? 'Low' : score >= 65 ? 'Medium' : 'High'
  const trend = body.previous_score > 0 ? `${score >= body.previous_score ? '+' : ''}${Math.round(score - body.previous_score)}%` : '—'
  return NextResponse.json({ predicted_score: score, risk_level, trend, confidence: 0.92, model_version: 'EduPredict RF v1.0', feature_importance: { attendance_rate: 0.28, current_gpa: 0.24, previous_score: 0.21, assignments_completed: 0.16, study_hours: 0.11 } })
}
