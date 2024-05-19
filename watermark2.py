# PyPDF2 updated version

import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.mergePage(watermark.pages[0])
    output.addPage(page)

    with open('watermarked.pdf', 'wb') as file:
        output.write(file)