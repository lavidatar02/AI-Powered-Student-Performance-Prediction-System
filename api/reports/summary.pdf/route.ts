import { NextResponse } from 'next/server'

export async function GET() {
  const body = `%PDF-1.4
1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj
2 0 obj<</Type/Pages/Count 0/Kids[]>>endobj
trailer<</Root 1 0 R>>
%%EOF`
  return new NextResponse(body, { headers: { 'Content-Type': 'application/pdf', 'Content-Disposition': 'attachment; filename="edupredict-performance-report.pdf"' } })
}
