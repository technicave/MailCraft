# Importing Modules
import smtplib
from tkinter import *
import tkinter.messagebox as thh

root = Tk()
root.geometry("744x544")
root.minsize(744,544)
root.maxsize(744,544)
root.title("MailCraft--Made By Aryan Tiwari")
root.config(bg='orange')

icon = PhotoImage("ico.ico")
root.iconbitmap(icon)


def sendEmail():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("sender email", "password")   
        server.sendmail("sender email", to.get(), textmail.get(1.0, END))
        server.close()
        thh.showinfo(f"Sended", "Message Is Sended")
    except Exception as e:
        thh.showinfo("Failed", "Failed To Send Email")

to = StringVar()
 
label1 = Label(root, text="MailCraft", font="comic 40 bold", pady=20, bg="orange")
label1.pack()
label2 = Label(root,text="Enter Email Below", bg="orange", fg="purple", font="lucida 12 bold" )
label2.pack()
mail = Entry(root,textvariable=to, borderwidth=10, font="comic 20 bold")
mail.pack()
labelcontent = Label(root, text="Enter Your Message Below", bg="orange", fg="purple",font="lucida 12 bold")
labelcontent.pack()
textmail = Text(root, bg="brown", fg="yellow",font="comic 12 bold", height=12, width=80)
textmail.pack()

button = Button(root, text="Send Mail", font= "comic 20 bold", bg="pink", command=sendEmail)
button.pack()

root.mainloop()
