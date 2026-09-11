import { NextResponse } from 'next/server'

const escapePdf = (value: string) => value.replace(/\\/g, '\\\\').replace(/\(/g, '\\(').replace(/\)/g, '\\)')

export async function POST(request: Request) {
  try {
    const { type, data } = await request.json()
    const title = type === 'cohort' ? 'Cohort Performance Report' : type === 'intervention' ? 'Intervention Impact Report' : 'Academic Advisor Brief'
    const lines = [
      'AI-Powered Student Performance Prediction System', title, `Generated: ${new Date().toLocaleDateString()}`, '',
      `Total students: ${data.students?.length ?? 0}`, `Total predictions: ${data.students?.filter((s: { score: number }) => s.score > 0).length ?? 0}`, '',
      ...(data.students?.length ? data.students.map((s: { name: string; id: string; program: string; score: number; risk: string; trend: string }) => `${s.name} | ${s.id} | ${s.program} | Score: ${s.score}% | Risk: ${s.risk} | Trend: ${s.trend}`) : ['No student data is currently available.']),
      '', 'This report uses the current data available in EduPredict.'
    ]
    const stream = lines.map((line: string, index: number) => `BT /F1 ${index === 0 ? 16 : 10} Tf 50 ${770 - index * 18} Td (${escapePdf(line)}) Tj ET`).join('\n')
    const objects = [`<< /Type /Catalog /Pages 2 0 R >>`, `<< /Type /Pages /Kids [3 0 R] /Count 1 >>`, `<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>`, `<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>`, `<< /Length ${stream.length} >>\nstream\n${stream}\nendstream`]
    let pdf = '%PDF-1.4\n'; const offsets = [0]
    objects.forEach((object, index) => { offsets[index + 1] = pdf.length; pdf += `${index + 1} 0 obj\n${object}\nendobj\n` })
    const xref = pdf.length; pdf += `xref\n0 ${objects.length + 1}\n0000000000 65535 f \n${offsets.slice(1).map(offset => `${String(offset).padStart(10, '0')} 00000 n `).join('\n')}\ntrailer\n<< /Size ${objects.length + 1} /Root 1 0 R >>\nstartxref\n${xref}\n%%EOF`
    return new NextResponse(pdf, { headers: { 'Content-Type': 'application/pdf', 'Content-Disposition': `attachment; filename="${type}-report.pdf"` } })
  } catch { return NextResponse.json({ error: 'Unable to generate report.' }, { status: 500 }) }
}
