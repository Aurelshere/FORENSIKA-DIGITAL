import PyPDF2
import webbrowser
from reportlab.pdfgen import canvas
import io
import base64

def add_page_at_end(input_pdf, output_pdf, text):
    # buka file pdfnya
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])

        # buat halaman baru berisi text yang nantinya akan diencode
        encoded_text = base64.b64encode(text.encode()).decode()
        packet = io.BytesIO()
        c = canvas.Canvas(packet)
        c.setFont("Helvetica", 12)
        c.setFillColorRGB(1, 1, 1)  # di set warna putih agar invisible
        c.drawString(100, 100, encoded_text)
        c.save()
        packet.seek(0)
        new_pdf = PyPDF2.PdfReader(packet)

        # halaman baru ditambahkan di bagian akhir
        writer.add_page(new_pdf.pages[0])

        # file yang telah dimodifikasi akan disimpan
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

        # pdf dapat dibuka di chrome
        webbrowser.open(output_pdf)

input_pdf = 'modified_file.pdf'
output_pdf_modified = 'modified_file_tambahhalamanakhir.pdf'
text = "INFORMATIKAAAAAAAAAAAAAAAAAAAAAAA" # text yang akan diencode
add_page_at_end(input_pdf, output_pdf_modified, text)

# file pdf asli juga akan dibuka di chrome bersamaan dengan file yang telah dimodifikasi
output_pdf_asli = 'file_asli.pdf'
with open(input_pdf, 'rb') as file:
    with open(output_pdf_asli, 'wb') as output_file:
        output_file.write(file.read())

webbrowser.open(output_pdf_asli)