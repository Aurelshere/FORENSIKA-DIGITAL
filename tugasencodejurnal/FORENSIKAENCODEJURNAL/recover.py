import PyPDF2
import webbrowser
from reportlab.pdfgen import canvas
import io
import base64

def add_page_at_end(input_pdf, output_pdf, text):
    # buka pdf filenya
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])

        # create halaman baru berisi pesan yang di encode
        encoded_text = base64.b64encode(text.encode()).decode()
        packet = io.BytesIO()
        c = canvas.Canvas(packet)
        c.setFont("Helvetica", 12)
        c.setFillColorRGB(1, 1, 1)
        c.drawString(100, 100, encoded_text)
        c.save()
        packet.seek(0)
        new_pdf = PyPDF2.PdfReader(packet)

        # halaman baru ditambahkan di bagian akhir
        writer.add_page(new_pdf.pages[0])

        # file yang telah dimodifikasi akan disimpan
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

        # agar pdf terbuka di chrome
        webbrowser.open(output_pdf)

# decode pesan text
with open('modified_file_tambahhalamanakhir.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[len(reader.pages) - 1]
    text = page.extract_text()
    decoded_text = base64.b64decode(text.encode()).decode()

# buat pdf baru hasil pesan text yang sudah direcover
output_pdf_recovered = 'modified_file_tambahhalamanakhir_recovered.pdf'
packet = io.BytesIO()
c = canvas.Canvas(packet)
c.setFont("Helvetica", 12)
c.setFillColorRGB(0, 0, 0)
c.drawString(100, 100, decoded_text)
c.save()
packet.seek(0)
new_pdf = PyPDF2.PdfReader(packet)

with open(output_pdf_recovered, 'wb') as output_file:
    writer = PyPDF2.PdfWriter()
    writer.add_page(new_pdf.pages[0])
    writer.write(output_file)

# pdf hasil recover akan terbuka di chrome
webbrowser.open(output_pdf_recovered)