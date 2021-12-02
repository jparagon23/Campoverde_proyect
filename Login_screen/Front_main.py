from sqlite3.dbapi2 import IntegrityError
from tkinter import ttk,messagebox
from tkinter import *
import sqlite3
import os
from tkinter import font
from PIL import ImageTk,Image
from datetime import datetime
from Login_screen.Class_front_login import Front_login

class Front_principal:
    def __init__(self,window):
        self.window=window
        #import the image

        self.img=Image.open('Campo_verde.jpg')
        self.img=self.img.resize((300,180)) #we change the size of the image 
        self.img=ImageTk.PhotoImage(self.img)
        self.date=datetime.now()

        #Create labels
        Label(self.window,text='Campo verde',font=('Calibri',14)).grid(row=0,sticky=N,pady=10) #sticky means in the middle
        Label(self.window,text="El mejor lugar para jugar tennis",font=('Calibri',12)).grid(row=1,sticky=N) 
        Label(self.window,image=self.img).grid(row=2,sticky=N,pady=30) #pady is the distance between rows 
 
        #we need buttons
        Button(self.window,text='Login', font=('calibri',12),command=lambda:self.login(),width=15).grid(row=3,sticky=N,pady=10)
    
    def login(self):

        #login_screen
        self.login_screen=Toplevel(self.window)
        self.login_screen=Front_login(self.login_screen,self.window)

