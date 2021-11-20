from config.placeholders import *
import os
import PyPDF2


def read_pdf():
    path = os.path.join(TRAINING_RESOURCES_DIR, 'shilha_bible.pdf')
    file = open(path, 'rb')
    fileReader = PyPDF2.PdfFileReader(file)

