import os, sys
path = os.environ['FILE_PATH']
sys.path.append(path)

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

class JsonToPdfService:
    def __init__(self, buffer, pageSize):
        self.buffer = buffer
        self.pagesizes = pagesize

    def write_json_data_to_pdf(self):
        pass

    def write_pdf_canvas_view(self):
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        p.drawString(100, 100, "Hello World.")
        p.showPage()
        p.save()
        buffer.seek(0)
        return buffer

    def generate_pdf(self):
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=A4)


        #Data to print
        data = {
            "Posts": [{"title":"Python", "views":500},{"title":"JavaScript", "views":500}],
            "Videos": [{"title":"Python Prgrommaing", "likes":500}],
            "Blogs": [{"name":"Report Lab", "likes":500, "claps":500}]
        }

        #Star writing the PDF here
        p.setFont("Helvtica", 15, leading=None)
        p.setFillColorRGB(0.29296875, 0.453125,0.609375)
        p.drawString(260,800,"My Website")
        p.line(0,780,1000,780)
        p.line(0,778,1000,770)
        x1 = 20
        y1 = 750
        #Render data
        for k, v in data.items():
            p.setFont("Helvetica", 15, leading=None)
            p.drawString(x1, y1-12, f"{k}")
            for value in v:
                for key, val in value.items():
                    p.setFont("Helvetica", 10, leading=None)
                    p.drawString(x1,y1-20,f"{key} - {val}")
                    y1 = y1 - 60
        p.setTitle(f'Report on {d}')
        p.showPage()
        p.save()

        pdf = buffer.getValue()
        buffer.close()
        return pdf

    def response_pdf(request):
        if 'pdf' in request.POST:
            response = HttpRespnse(content_type='application/pdf')
            today = date.today()
            filename = 'pdf_demo' + today.strftime('%Y-%m-%d')
            response['Content-Disposition'] = 'attachement:filename={0}.pdf'.format(filename)
            report = PdfPrint(buffer, 'A4')
            pdf = report.report(weather_period, 'Weather Statistics data')
            response.write(pdf)
            return response

    def report(self, weather_history, title):
        doc = SimpleDocTemplate(self.buffer, rightMargin=72, leftMargin=30, topMargin=30, bottomMargin=72, pagesize=self.pagesizes)
        styles = getSampleStyleSheet()
        data = []
        data.append(Paragraph(title, styles['Title']))
        doc.build(data)
        pdf = self.buffer.getValue()
        self.buffer.close()
        return pdf


    def pdf_tableformat(self):
        wh_table = getSampleStyleSheet()
        # wh_table.setStyle(TableStyle(
        #     [('INNERGRID', (0,0), (-1,-1),0.25,colors.black,
        #      ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
        #      ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
        #      ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        #     ]
        # ))
        chart_title = Label()
        chart_title.fontName = 'FreeSansBold'
        chart_title.fontSize = 16
        chart_title.textAnchor = 'middle'

        legend = Legend()
        legend.x = kwargs['x']
        legend.y = kwargs['y']
        legend.alignment = 'right'

        legend.boxAnchor = kwargs['boxAnchor']
        legend.columnMaximum = kwargs['columnMaximum']
        legend.deltax = 0
        legend.colorNamePairs = zipe(lcolors, labels)

        for i, color in enumerate(lcolors):
            if chart_type == 'line':
                chart.lines[i].fillColor = color
            elif chart_type == 'pie':
                chart.slices[i].fillColor = color
            elif chart_type == 'bar':
                chart.bars[i].fillColor = color

    def pageNumber(self, canvas, doc):
        number = canvas.getPageNumber()
        canvas.drawCenteredString(100*num, 13 * num, str(number))

    def generate_report(self, filename, data):
        drawing = Drawing(400, 200)
        data = [(13, 5, 20, 22, 37, 45, 19, 4)]
        bc = VerticalBarChart()
        bc.x = 50
        bc.y = 50
        bc.height = 125
        bc.widht = 300
        bc.data = data
        # bc.strokeColor = colors.black
        bc.valueAxis.valueMin = 0
        bc.valueAxis.valueMax = 50
        bc.categoryAxis.categoryNames = ['Jan-99', 'Feb-99', 'Mar-99', 'Apr-99', 'May-99', 'June-99', 'Jul-99', 'Aug-99']
        drawing.add(bc)
        pdf = renderPDF.drawToFile(drawing, filename, data)

