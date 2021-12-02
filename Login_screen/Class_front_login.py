from sqlite3.dbapi2 import IntegrityError
from tkinter import ttk,messagebox
from tkinter import *
import sqlite3
import os
from tkinter import font
import tkinter
from typing import List
from PIL import ImageTk,Image
from datetime import datetime
from tkcalendar import Calendar, DateEntry
from datetime import datetime,date
from Dashboard_main.Class_front_dashboard import Dashboard
from Appointment_module.Class_list import Listinfo
from Common_classes.Class_validation import Validation

from Members_module.Usuarios import *
from Appointment_module.Class_Appoitments import Appoitments
class Front_login():
    def __init__(self,master,antwindow):
        self.login_screen=master
        self.antwindow=antwindow
        self.login_screen.title('Login')

        Label(self.login_screen,text='Login to your account',font=('calibri',12)).grid(row=0,sticky=N,pady=5)

        Label(self.login_screen,text='Username',font=('calibri',12)).grid(row=1,sticky=W)
        Label(self.login_screen,text='Password',font=('calibri',12)).grid(row=2,sticky=W)
        self.login_notif=Label(self.login_screen,font=('calibri',12),text='',fg='red')
        self.login_notif.grid(row=4,columnspan=2,sticky=N)

        #Entry 
        self.login_uname=Entry(self.login_screen)
        self.login_uname.focus()
        self.login_uname.grid(row=1,column=1,padx=2)
        self.login_password=Entry(self.login_screen,show='*')
        self.login_password.grid(row=2,column=1,padx=2)
        #button

        Button(self.login_screen,text='Login',width=15,font=('Calibri',12),command=lambda:self.login_session()).grid(row=3,sticky=N,columnspan=2)    

    def login_session(self):
        
        loginObject=Validation()
        loganswer=loginObject.loginValidation(self.login_uname.get(),self.login_password.get())
        if loganswer =='NotInformation' :
            self.login_notif['text']='Please introduce the required information'
            self.login_uname.delete(0,END)
            self.login_password.delete(0,END)
            self.login_uname.focus()
        elif loganswer != True:
            messagebox.showerror("Validacion incorrecta","El usuario o la contraña no es correcta",parent=self.login_screen)
            self.login_uname.delete(0,END)
            self.login_password.delete(0,END)
            self.login_uname.focus()
        elif loganswer==True:
            
            self.login_screen.destroy()
            self.antwindow.destroy()
            self.main_dashboard=Tk()
            self.main_dashboard_object=Dashboard(self.main_dashboard,loginObject)