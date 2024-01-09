# importing the libraries
import PyPDF2


pdf_file ='Document_from_Maleek_Toms.pdf'


with open(pdf_file, 'rb') as pdf:
    
    pdf_reader = PyPDF2.PdfReader(pdf)

    text = ""

    # Iterate through each page and extract text
    for page_number in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_number]
        text += page.extract_text()

# writing extracted text
with open("output.txt", "w") as text_file:
    text_file.write(text)
