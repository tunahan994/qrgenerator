from tkinter import *
from tkinter import messagebox
import pyqrcode
import os
import qrcode

window = Tk()
window.title("QR Code Generator by tunahan994")

window.geometry("750x450")

def generate():
    if len(subject.get()) != 0:
        global myQr
        myQr = pyqrcode.create(subject.get())
        qrImage = myQr.xbm(scale=6)
        global photo 
        photo = BitmapImage(data=qrImage)
    else:
        messagebox.showerror("Hata!","Lütfen metni giriniz.") 
    try:
        showCode()
    except:
        pass

def showCode():
    global photo
    notificationLabel.config(image=photo)
    subLabel.config(text="QR kod şunun için gösteriliyor: " + subject.get())

def save():
    try:
        code = qrcode.make(subjectEntry.get())
        code.save(nameEntry.get()+ ".png")
    except Exception:
        messagebox.showerror("Aynı dizinde birden fazla aynı isimde dosya olabilir.")

lab1 = Label(window, text="Metni Giriniz", font = ("Helvetica", 12)) 
lab1.grid(row=0, column=0, sticky=N + S + E + W)

lab2 = Label(window, text="Oluştur", font = ("Helvetica", 12)) 
lab2.grid(row=1, column=0, sticky=N + S + E + W)

lab3 = Label(window,text="Dosya Adı", font=("Helvetica",12))
lab3.grid(row=0, column=2, sticky=N + S + E + W)

subject = StringVar()
subjectEntry = Entry(window, textvariable = subject, font=("Helvetica", 12))
subjectEntry.grid(row=0, column=1, sticky= N + S + E + W)

createButton = Button(window, text="QR Kod oluştur", font=("Helvetica",12), width=15, command=generate)
createButton.grid(row=1, column=1, sticky=N + S + W + E)

name = StringVar()
nameEntry = Entry(window, textvariable = name, font=("Helvetica", 12))
nameEntry.grid(row=0, column=3, sticky=N + S + E + W)


notificationLabel = Label(window)
notificationLabel.grid(row=2, column=1, sticky= N + S + E + W)

subLabel = Label(window, text="")
subLabel.grid(row=3, column=2, sticky=N + S + E + W)

showButton = Button(window, text="PNG olarak kaydet", font=("Helvetica",12), width=15, command=save)
showButton.grid(row=3, column=1, sticky=N + S + E + W)

totalRows=3
totalColumns=3
for row in range(totalRows + 1):
    window.grid_rowconfigure(row, weight=1)
for col in range(totalColumns + 1):
    window.grid_columnconfigure(col, weight=1)

window.mainloop()    
























