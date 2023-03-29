import os, sys
path = os.environ['FILE_PATH']
sys.path.append(path)

from app.models.user import User

import reportlab
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lb.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import letter, A4

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics import renderPDF
from reportlab.graphics import PdfPrint


class PdfPrintPage:
    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize


    def print_users(self):
        buffer = self.buffer
        doc = SimpleDocTemplate(buffer, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72, pagesize=self.pagesize)
        elements = []
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

        users = User.objects.all()
        elements.append(Paragraph('My User Names', styles['Heading']))
        for i, user in enumerate(users):
            elements.append(Paragraph(user.get_full_name(), styles["Normal"]))

        pdf = buffer.getValue()
        buffer.close()
        return pdf

