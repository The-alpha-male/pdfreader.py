import pyttsx3
import PyPDF2
book = open('SCI250.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(8)
text = page.extractText()
speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()
