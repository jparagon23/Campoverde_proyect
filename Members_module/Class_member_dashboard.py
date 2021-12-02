
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
from Appointment_module.Class_list import Listinfo
from Common_classes.Class_validation import Validation

from Members_module.Usuarios import *
from Appointment_module.Class_Appoitments import Appoitments
from Members_module.Class_create_member import createMember
class MembersScreens:
    def __init__(self,screen):
        self.members_screen = screen
        self.members_screen.title('Afiliados')

        #adicionamos los labels

        Label(self.members_screen, text = 'Menu de afiliados').grid(row = 0, sticky=N)
        
        Button(self.members_screen,text='Crear un afiliado',font=('Calibri',12),width=30,command=lambda:self.create_member()).grid(row=1,sticky=N,padx=10)
        Button(self.members_screen,text='Consultar un afiliado',font=('Calibri',12),width=30,command=lambda:self.consult_member()).grid(row=2,sticky=N,padx=10)
    def create_member(self):
        
        self.create_members_screen=Toplevel(self.members_screen)
        self.objectCreateMember=createMember(self.create_members_screen)
    def consult_member(self):
        print('juan')
