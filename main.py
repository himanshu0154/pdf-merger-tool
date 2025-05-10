from pypdf import PdfWriter
import os
merger = PdfWriter()
# No. of pdfs you want to merge
no_of_pdfs = int(input("how many pdfs do you want to merge?\n"))
pdfs = []
# Set the correct path of your folder
path = r"PDF_merger\data"
print("enter the name of your pdf")
for i in range(1,no_of_pdfs + 1):
    # Input the name of your files
    user = input(f"{i}. ")
    extention = ".pdf"
    file_name = os.path.join(path, user + extention)
    # Make sure you are using correct file name to avoid any errors
    if os.path.exists(file_name):
        pdfs.append(file_name)
    else:
        print("file not found!!")

for pdf in pdfs:
    merger.append(pdf)

merger.write(r"PDF_merger\data\\merged-pdf.pdf")
print("pdf merged successfully")
merger.close()