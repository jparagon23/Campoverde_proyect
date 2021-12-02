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
from Members_module.Class_member_dashboard import MembersScreens
from Appointment_module.Class_appointment_dashboard import AppointmentsScreen
class Dashboard:
    def __init__(self,window,object):
        self.main_dashboard = window
        self.objectVal=object
        self.main_dashboard.title ('Inicio')
        #labels de la pantalla 

        Label(self.main_dashboard,text='Campo Verde',font=('Calibri',12)).grid(row=0,sticky=N)
        Label(self.main_dashboard,text='Bienvenido '+self.objectVal.admin_username,font=('Calibri',12)).grid(row=1,sticky=N)

        # #buttons
        Button(self.main_dashboard,text='Afiliados',font=('Calibri',12),width=30,command=lambda:self.members()).grid(row=2,sticky=N,padx=10)
        Button(self.main_dashboard,text='Reservas',font=('Calibri',12),width=30,command=lambda:self.appointments()).grid(row=3,sticky=N,padx=10)
        Button(self.main_dashboard,text='Reportes',font=('Calibri',12),width=30,command=lambda:self.reports()).grid(row=4,sticky=N,padx=10)

    def members(self):
        self.members_screen=Toplevel(self.main_dashboard)
        self.objectMemberScreen=MembersScreens(self.members_screen)
    def appointments(self):
        self.appointment_screen=Toplevel(self.main_dashboard)
        self.objectAppointmentScreen=AppointmentsScreen(self.appointment_screen)
        return
    def reports(self):
        return