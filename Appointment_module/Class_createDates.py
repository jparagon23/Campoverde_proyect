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
from Class_Appoitments import Appoitments
class CreateDatesScreen:
    def __init__(self,window):
        self.create_dates_screen=window
        self.create_dates_screen.title('Crear turnos')

        var_h_initial=StringVar()
        var_h_initial.set('6')
        var_h_final=StringVar()
        var_h_final.set('22')
        Label(self.create_dates_screen, text = 'Ingresa la fecha inicial').grid(row = 0, column=0 ,sticky=N)
        Label(self.create_dates_screen, text = 'Ingresa la fecha final').grid(row = 0, column=4, sticky=N)

        self.initial_date = DateEntry(self.create_dates_screen, width=12, background='darkblue',
                    foreground='white', borderwidth=2, day=int(date.today().strftime('%d')),month=int(date.today().strftime('%m')), year=int(date.today().strftime('%Y')),date_pattern='dd/mm/y')
        self.initial_date.grid(row=0,column=1)

        self.final_date = DateEntry(self.create_dates_screen, width=12, background='darkblue',
                    foreground='white', borderwidth=2, day=int(date.today().strftime('%d'))+9,month=int(date.today().strftime('%m')), year=int(date.today().strftime('%Y')),date_pattern='dd/mm/y')
        self.final_date.grid(row=0,column=5)        
    

        self.hours_spin_initial =Spinbox(
            self.create_dates_screen,
            from_=00,
            to=23,
            wrap=True,
            state="readonly",
            textvariable=var_h_initial,
            width=2,
            justify=CENTER
            )
        self.minutes_spin_initial = Spinbox(
            self.create_dates_screen,
            from_=00,
            to=59,
            wrap=True,
            state=DISABLED,
            width=2,
            justify=CENTER
            )
        self.hours_spin_final =Spinbox(
            self.create_dates_screen,
            from_=00,
            to=23,
            wrap=True,
            state="readonly",
            textvariable=var_h_final,
            width=2,
            justify=CENTER
            )
        self.minutes_spin_final = Spinbox(
            self.create_dates_screen,
            from_=00,
            to=59,
            wrap=True,
            state=DISABLED,
            width=2,
            justify=CENTER
            )

        self.hours_spin_initial.grid(row=0,column=2)
        self.minutes_spin_initial.grid(row=0,column=3)
        self.hours_spin_final.grid(row=0,column=6)
        self.minutes_spin_final.grid(row=0,column=7)

        Button(self.create_dates_screen, text='undeme', command=lambda:self.create_appointments()).grid(row=2,column=3)

    def create_appointments(self):
        self.initial_date_function=str(self.initial_date.get_date())+' '+str(self.hours_spin_initial.get())+':'+str(self.minutes_spin_initial.get())+':'+'0'
        self.final_date_function=str(self.final_date.get_date())+' '+str(self.hours_spin_final.get())+':'+str(self.minutes_spin_final.get())+':'+'0'

        self.objectAppointment=Appoitments()
        answer=self.objectAppointment.createAppointmentsDates(self.initial_date_function, self.final_date_function)

        if answer==True:
            messagebox.showinfo("Turnos creados","Los turnos se han creado satisfactoriamente",parent=self.create_dates_screen)
            self.create_dates_screen.destroy()

        if answer==False:
            messagebox.showerror("Error","Las fechas no se crearon, favor contactar al administrador",parent=self.create_dates_screen)
