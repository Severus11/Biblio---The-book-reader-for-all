import sys
import pyttsx3
import PyPDF2

pdfFileObj = open('pdf_example.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
a = pdfReader.numPages
print(a)
x = 1
c = 1

def read(page):
    page_content = pdfReader.getPage(int(page))
    b = page_content.extractText()
    print(b)
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say(b)
    engine.say("Page number " + str(page) + " is completed")
    engine.runAndWait()
    engine.stop()

while (x):
    page = input("Enter the page number to read :")
    read(page)
    c = int(input("Do you want to continue? (1)Yes (2)No"))
    if c == 2:
        x = 0
        print("Thank you")