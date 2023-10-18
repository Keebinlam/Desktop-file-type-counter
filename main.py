import os
desktoppath = ()   # path to the desktop
files = os.listdir(desktoppath)  # lists out files in the desktop


def pdfcount():  # by giving the number of pdf files on my desktop
    pdf_files = [file for file in files if file.endswith(
        ".pdf")]  # the files variable gets all the files on the desktop, this adds a filter to gather only "pdfs"
    num_pdf = len(pdf_files)  # counts number of pdfs from the pdf list
    print(f'Number of pdf{num_pdf}')


pdfcount()

#tell me all number of each type of file on my desktop