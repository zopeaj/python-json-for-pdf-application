import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from datetime import datetime
from fastapi import APIRouter, Request, Response
from app.core.business.abstracts.JsonToPdfService import JsonToPdfService
from fastapi.responses import FileResponse
from app.utils.staff_member_annotation import staff_member_required
from app.core.business.abstracts.PdfPrintPage import PdfPrintPage
from io import BytesIO

jsonToPdfService = APIRouter()
jsonToPdfService = JsonToPdfService()

@jsonToPdfService.post("/")
def write_json_data_to_pdf(request: Request):
    pass

@jsonToPdfService.get("/")
def get_pdf_from_json(request: Request):
    pass


@jsonToPdfService.post("/")
def get_pdf_to_json(request: Request):
    buffer = jsonToPdfService.write_pdf_canvas_view()
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

@jsonToPdfService.post("/data")
def generate_pdf(request: Request):
    response = Response(media_type='application/pdf')
    d = datetime.today().strftime('%Y-%m-%d')
    response['Conent-Deposition'] = f'inline; filename="{d}.pdf"'
    pdf = jsonToPdfService.generate_pdf()
    response.write(pdf)
    return response

@jsonToPdfService.post("/")
@staff_member_required
def print_users_data(request: Request):
    response = Response(media_type='application/pdf')
    response['Conent-Deposition'] = f'attachment; filename="{request.data.get("username")}.pdf"'
    bufer = BytesIO()
    report = PdfPrintPage(bufer, 'Letter')
    pdf = report.print_users()
    response.write(pdf)
    return response

@jsonToPdfService.post("/")
def generate_report_view(request: Request):
    filename = request.data.get("filename")
    data = request.data.get("data")
    pdf = jsonToPdfService.generate_report(filename, data)
    return Response(pdf, media_type='application/pdf')
