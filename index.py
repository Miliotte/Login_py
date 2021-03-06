#Importação das Bibliotecas

from sqlite3 import TimeFromTicks
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import ttk
from turtle import left, width
from cffi import VerificationError

from numpy import tile
import DataBase

# Criar Windows

win = Tk()
win.title("Miliotte System - Acess Panel")
win.geometry("600x300")
win.configure(background="white")
win.resizable(width=FALSE, height=False)
win.attributes("-alpha", 0.9)
win.iconbitmap(default="img/logoIcon.ico")

logo = PhotoImage(file="img/logo.png")

LeftFrame = Frame(win, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(win, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg='MIDNIGHTBLUE')
LogoLabel.place(x=50 , y=100)

#####Label User
UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg='MIDNIGHTBLUE' , fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=113)

#####Label Password

PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg='MIDNIGHTBLUE' , fg="White")
PassLabel.place(x=6, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="•")
PassEntry.place(x=150, y=160)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBase.cursor.execute("""
    SELECT User, Password FROM Users WHERE User = ? and Password = ?
    """, (User, Pass))
    print("Logou")

    VerifyLogin = DataBase.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmardo")
    except:
            messagebox.showerror(title="Login Info", message="Acesso Negado")


"""Tupan acha o erro dessa porra ! lkkkk
"""
##Button

LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    NomeLabel = Label(RightFrame, text= "Name: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=39)
    NomeEntry.place(x=100, y=20)

    EmailLabel = Label(RightFrame, text= "Email: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=70)

    ValPassLabel = Label(RightFrame, text= "Password: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    ValPassLabel.place(x=5, y=190)

    ValPassEntry = ttk.Entry(RightFrame, width=30)
    ValPassEntry.place(x=150, y=200)

    ##register back to database
    def AuthenticatePass(): 
        PassOn = PassEntry.get()
        PassTwo = ValPassEntry.get()
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        DataBase.cursor.execute("""
            SELECT user FROM Users
            """)
        for  UserVerificaion in DataBase.cursor:
          print (UserVerificaion)
##rever 
        if (Name == "" or Email == "" or User == "" or Pass == "" ):
            messagebox.showerror(title='Register Error', message="Fill in all fields") 
        elif(PassOn != PassTwo):
             messagebox.showerror(title='Password Error!',  message='Password Error!')
        elif(User in UserVerificaion): 
            print('ok')
            messagebox.showerror(title='User Exist',  message='User Exist')        
        else:
            DataBase.cursor.execute("""
            INSERT INTO Users(Name, Email, user, password)VALUES(?,?,?,?)
            """,(Name, Email, User, Pass))
            DataBase.conm.commit()
            messagebox.showinfo(title='Cadastro Efetuado',  message='Cadastro Efetuado')
        

    Register = ttk.Button(RightFrame, text="Register", width=30, command=AuthenticatePass)
    Register.place(x=100, y=225)

    def BackToLogin ():
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        ValPassEntry.place(x=5000)
        ValPassLabel.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        

        LoginButton.place(x=100, y=225)
        RegisterButton.place(x=130, y=260)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=130, y=260)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=130, y=260)

win.mainloop()


