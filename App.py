from tkinter import *
from tkinter import filedialog
import PyPDF2
import pyttsx3


def extract_text():
  file = filedialog.askopenfile(parent=root, mode='rb', title='Choose a PDF file')
  pdfReader = PyPDF2.PdfFileReader(file)
  global mytext
  mytext = ""
  page_content = pdfReader.getPage(0)
  mytext = page_content.extractText()
  print(mytext)
  engine = pyttsx3.init()
  rate = engine.getProperty('rate')
  engine.setProperty('rate', rate - 50)
  engine.say(mytext)
  engine.runAndWait()
  file.close()


def stop_speaking(): 
  
  engine.stop()


def speak_text():
  
  global rate
  global male
  global female
  engine = pyttsx3.init()
  rate = engine.getProperty('rate')              
  engine.setProperty('rate', rate-50)
  engine.say(mytext)
  engine.runAndWait()            
  

def Application(root):
  root.geometry('{}x{}'.format(600, 500))       
  root.resizable(width=False, height=False)
  root.title("Biblio - The Book Reader for All !")
  root.configure(background="#e0ffff")
  global male, female

  frame1 = Frame(root, width=500, height=200, bg="#8a2be2")  
  frame2 = Frame(root, width=500, height=450, bg="#e0ffff")   
  frame1.pack(side="top", fill="both")
  frame2.pack(side="top", fill="y")


  name1 = Label(frame1, text="WELCOME TO BIBLIO ! ", fg="white", bg="#8a2be2", font="Arial 28 bold")
  name1.pack()
  name2 = Label(frame1, text="A simple PDF Audio Reader for you!", fg="white",
                bg="#8a2be2", font="Calibri 15")
  name2.pack()


  btn = Button(frame2, text='Select PDF file', command=extract_text, activeforeground="red", 
                padx="70", pady="10", fg="white", bg="black", font="Arial 12")
  btn.grid(row=0, pady=20, columnspan=2)


  submitBtn = Button(frame2, text='Play PDF file', command=speak_text, activeforeground="red",
               padx="60", pady="10", fg="white", bg="black", font="Arial 12")
  submitBtn.grid(row=4,column=0, pady=65)


  stopBtn = Button(frame2, text='Stop playing', command=stop_speaking,activeforeground="red",
             padx="60", pady="10", fg="white", bg="black", font="Arial 12")
  stopBtn.grid(row=4, column=1, pady=65)





if __name__ == "__main__":
  mytext = ""        
  engine = pyttsx3.init()
  root = Tk()
  Application(root)
  root.mainloop()
