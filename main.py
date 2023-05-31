from tkinter import *
from pwdgen import PASSWORDGENERATOR
import pyperclip
import json

popup1 = None
WebsiteEntry = None

window = Tk()
window.geometry("800x600")
window.title("Password Manager")

def generatepassword():
    gnpwd = PASSWORDGENERATOR()
    PasswordEntry.delete(0,END)
    PasswordEntry.insert(0,gnpwd)

def close():
     popup1.destroy()

def addtofile():
    global popup1    
    username = UsernameEntry.get()
    password = PasswordEntry.get()
    website = WebsiteEntry.get()
    pyperclip.copy(password)
    new_data = {
             website:
             {
                "email":username,
                "password":password
             }
        }
    try:
        with open("Pwdinfo.json",'r') as f:
            data = json.load(f)
            data.update(new_data)
        with open("Pwdinfo.json","w") as f:
            json.dump(data,f,indent=4)
    except:
         with open("Pwdinfo.json","w") as f:
            json.dump(new_data,f,indent=4)

    popup1.destroy()


def popuponpressingadd():
    global popup1
    if UsernameEntry.get() == "" or PasswordEntry.get() == "" or WebsiteEntry.get() == "":
            popup = Tk()
            popup.geometry("200x75")
            popup.title("Failed Entry")
            popuplabel = Label(popup,text="One or more fields missing!",font=("Arial",15,"normal"),wraplength=75)
            popuplabel.pack()
    else:
        popup1 = Tk()
        popup1.geometry("400x200")
        popuplabelemail = Label(popup1,text=f"Email: {UsernameEntry.get()}")
        popuplabelemail.place(x=40,y=50)
        popuplabelpassword = Label(popup1,text = f"Password: {PasswordEntry.get()}")
        popuplabelpassword.place(x = 40, y = 75)
        popuplabel2 = Label(popup1,text="Is this OK?")
        popuplabel2.place(x=40,y=100)
        yesbutton = Button(popup1,text="Yes",command=addtofile)
        nobutton = Button(popup1, text="No",command=close)
        yesbutton.place(x=300,y=150)
        nobutton.place(x=250,y=150)

def search():
    global WebsiteEntry
    with open("Pwdinfo.json","r") as f:
        data = json.load(f)
    try:
        email = data[WebsiteEntry.get()]["email"]
        password = data[WebsiteEntry.get()]["password"]
        popup2 = Tk()
        emaillbl = Label(popup2,text = f"Email/Username: {email}")
        emaillbl.place(x=30,y=40)
        pwdlbl = Label(popup2,text = f"Password: {password}")
        pwdlbl.place(x=30,y=60)

    except KeyError:
        popup3 = Tk()
        popuplabel = Label(popup3,text="Not Found")
        popuplabel.pack()

canvas = Canvas(width = 189,height=200)
myimg = PhotoImage(file = "logo1.png")
canvas.create_image(95,110,image=myimg)
canvas.place(x=300,y=130)

Websitelabel = Label(text = "Website: ",font=("Arial",17,"normal"))
Websitelabel.place(x=150,y=350)

WebsiteEntry = Entry(width=45)
WebsiteEntry.place(y=350,x=225)

Usernamelabel = Label(text = "Email/Username: ",font=("Arial",17,"normal"))
Usernamelabel.place(x=86,y=380)

UsernameEntry = Entry(width=45)
UsernameEntry.place(y=380,x=225)

Passwordlabel = Label(text = "Password: ",font=("Arial",17,"normal"))
Passwordlabel.place(x=137,y=410)

PasswordEntry = Entry(width=24)
PasswordEntry.place(y=410,x=225)

GeneratePassword = Button(text="Generate Password",command=generatepassword)
GeneratePassword.place(y=410,x=488)

AddPassword = Button(text = "Add",command=popuponpressingadd)
AddPassword.config(width=43)
AddPassword.place(x=223,y=440)

Search = Button(text = "Search",command=search)
Search.place(y=346.8,x=645)


window.mainloop()