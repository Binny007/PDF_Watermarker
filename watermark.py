import PyPDF2

# Read the watermark and without watermark pdf files
template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

# Creating write object in memory and combine both file
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))     # Add the watermark to the page
    output.addPage(page)

# finally, write the new document with a watermark
with open("watermarked_output.pdf", "wb") as file:
    output.write(file)