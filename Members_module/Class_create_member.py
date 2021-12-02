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

class createMember:
    def __init__(self,window):
        self.create_members_screen=window

        self.create_members_screen.title('Crear usuario')


        Label(self.create_members_screen, text = 'Nombre: ').grid(row = 0, column=0,sticky=N)

        self.new_member_name = Entry(self.create_members_screen)
        self.new_member_name.grid(row = 0, column = 1)
        self.new_member_name.focus()

        Label(self.create_members_screen, text = 'Apellido:').grid(row = 0,column=2 , sticky=N)
        self.new_member_lastname = Entry(self.create_members_screen)
        self.new_member_lastname.grid(row = 0, column = 3)

        Label(self.create_members_screen, text = 'N. Indentificación: ').grid(row = 1,column=0, sticky=N)

        self.new_member_id = Entry(self.create_members_screen)
        self.new_member_id.grid(row = 1, column=1)

        Label(self.create_members_screen, text = 'Celular: ').grid(row = 1,column=2, sticky=N)

        self.new_member_phone = Entry(self.create_members_screen)
        self.new_member_phone.grid(row = 1, column = 3)

        Label(self.create_members_screen, text = 'Correo: ').grid(row = 2,column=0, sticky=N)

        self.new_member_mail = Entry(self.create_members_screen)
        self.new_member_mail.grid(row = 2, column = 1)

        
        Label(self.create_members_screen, text = 'Fecha de nacimiento: ').grid(row = 2,column=2, sticky=N)

        self.new_member_birthday= DateEntry(self.create_members_screen, width=12, background='darkblue',foreground='white', borderwidth=2, year=2010)
        self.new_member_birthday.grid(row=2,column=3)

        Button(self.create_members_screen,text='Crear',font=('Calibri',12),width=30,command=lambda:self.create_new_member()).grid(row=3,column=1, sticky=N,padx=10)
        Button(self.create_members_screen,text='Cancelar',font=('Calibri',12),width=30,command=lambda:self.cancel_new_member()).grid(row=3,column=2, sticky=N,padx=10)
    def create_new_member(self):

        user=Usuario(self.new_member_name.get(),self.new_member_lastname.get(),self.new_member_id.get(),self.new_member_phone.get(),self.new_member_mail.get(),self.new_member_birthday.get())
        var_createUser=user.createUser()
        if var_createUser=='Emptyfield':
            messagebox.showerror('Informacion incompleta','Por favor llenar los campos obligatorios',parent=self.create_members_screen)
            return
        elif var_createUser==True:
            message_created=messagebox.askquestion('Usuario creado','El usuario ha sido creado satisfactoriamente,¿desea crear un nuevo usuario?',parent=self.create_members_screen)
            if message_created=='yes':
                self.new_member_name.delete(0,END)
                self.new_member_id.delete(0,END)
                self.new_member_lastname.delete(0,END)
                self.new_member_mail.delete(0,END)
                self.new_member_phone.delete(0,END)
                self.new_member_name.focus()
            elif message_created=='no':
                self.create_members_screen.destroy()
        else:
            print(var_createUser)