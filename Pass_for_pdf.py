from PyPDF2 import PdfFileWriter, PdfFileWriter
from getpass import getpass

s = input('Имя файла: ')
PdfWriter = PdfFileWriter()
pdf = PdfFileWriter(f'{s}.pdf')

for page in range(pdf.numPages):
    PdfWriter.add_page(pdf.pages[page])

password = getpass(prompt='Введите пароль: ')
PdfWriter.encrypt(password)

with open('protected.pdf', 'wb') as file:
    PdfWriter.write(file)