from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.setFillColorRGB(1, 0, 0)
can.setFont("Times-Roman", 14)
can.drawString(72, 655, "Hello from Python")
can.save()

packet.seek(0)
new_pdf = PdfFileReader(packet)

existing_pdf = PdfFileReader(open("original.pdf", "rb"))
output = PdfFileWriter()

page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)

outputStream = open("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()