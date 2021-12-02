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
class MakeAppointmentScreen:

    def __init__(self,screen,parentScreen):
        self.appointment_screen=parentScreen
        self.make_appointment_screen=screen
        self.make_appointment_screen.title('Crear reserva')

        query=Query()
        db_rows=query.q_initial_list_appointment()
        self.list_members=[]
        for row in db_rows:
            self.list_members.append(row[0])
        Label(self.make_appointment_screen, text = 'Nombre del usuario: ').grid(row = 0, column=2 ,sticky=N)
        self.appointment_user_name=Entry(self.make_appointment_screen,text='start typing')
        self.appointment_user_name.grid(row=0,column=3)
        self.appointment_user_name.delete(0,END)

        self.user_name_list=Listbox(self.make_appointment_screen,width=20,height=3)
        self.user_name_list.grid(row=1,column=3,sticky=N)

        Label(self.make_appointment_screen, text = ' ').grid(row = 2, column=0 ,sticky=N)

        Label(self.make_appointment_screen, text = ' Dia de reserva: ').grid(row = 3, column=0 ,sticky=N)

        self.appointment_date = DateEntry(self.make_appointment_screen, width=12, background='darkblue',
                    foreground='white', borderwidth=2, day=int(date.today().strftime('%d')),month=int(date.today().strftime('%m')), year=int(date.today().strftime('%Y')),date_pattern='y/mm/dd')
        self.appointment_date.grid(row=3,column=1)        

        Label(self.make_appointment_screen, text = ' Ingrese la hora:  ').grid(row = 3, column=2 ,sticky=N)

        self.appointment_hour=ttk.Combobox(self.make_appointment_screen,value=[],state=DISABLED)
        self.appointment_hour.grid(row=3,column=3)

        Label(self.make_appointment_screen, text = ' Ingrese la cancha:  ').grid(row = 3, column=4 ,sticky=N)

        self.appointment_field=ttk.Combobox(self.make_appointment_screen,value=[],state=DISABLED)
        self.appointment_field.grid(row=3,column=5)

        Button(self.make_appointment_screen,text='Reservar',width=10,height=3, command=lambda:self.Create_user_appointment()).grid(row=4,column=3,sticky=N)


        self.Create_list_hour('')

        #create de list when the date is created
        self.appointment_date.bind('<<DateEntrySelected>>',self.Create_list_hour)
        
        #create the list of Field available for the date and hour

        self.appointment_hour.bind('<<ComboboxSelected>>',self.Create_list_fields)


        self.update_member_list(self.list_members)
        ##This bind insert the value y select in the list to the entry
        self.user_name_list.bind('<<ListboxSelect>>',self.fillout)
        ##every time i type something, we are going to search if it exist in the members
        self.appointment_user_name.bind('<KeyRelease>',self.check)

    def Create_list_hour(self,event):
        self.objectlist=Listinfo()
        objectreturn=self.objectlist.create_hours_list('',self.appointment_date.get_date()) 
        
        if len(objectreturn)>0:
            self.appointment_hour.config(value=objectreturn)  
            self.appointment_hour.config(state='readonly')    
        else:
            self.appointment_hour.config(state=DISABLED)  
    def Create_list_fields(self,event):
        ##here we create the list of the available fields for date and hour
        objectReturn=self.objectlist.create_fields_list(self.appointment_date.get_date(),self.appointment_hour.get())
        
        if len(objectReturn)>0:
            self.appointment_field.config(value=objectReturn) 
            self.appointment_field.config(state='readonly')
        else:
            self.appointment_field.config(state=DISABLED)         


    def check(self,event):
        type=self.appointment_user_name.get()
        if type=='':
            data=self.list_members
        else:
            data=[]
            for item in self.list_members:
                if type.lower() in item.lower():
                    data.append(item)
        #update the list with the type info
        self.update_member_list(data)


    def fillout(self,event):
        #HERE WE INSERT THE VALUE WE SELECT IN THE LIST, TO THE ENTRY
        self.appointment_user_name.delete(0,END)
        self.appointment_user_name.insert(0,self.user_name_list.get(ACTIVE))

        return

    def update_member_list(self,list) :
        ##here we create the list that the user is going to see in the listbox
        self.user_name_list.delete(0,END)
        for item in list:
            self.user_name_list.insert(END,item)

    def Create_user_appointment(self):
        self.objectAppointment=Appoitments()
        objectmessage=self.objectAppointment.createUserAppointment(self.appointment_user_name.get(),self.appointment_date.get_date(),self.appointment_hour.get(),self.appointment_field.get())

        if objectmessage=='InfoNotComplete':
            messagebox.showerror("Informacion incompleta","Favor ingresar la informacion completa",parent=self.make_appointment_screen)
            return
        elif objectmessage=='AppointmentCreated':
                answer= messagebox.askquestion("Reserva creada","""La reserva se creo con exito,
                ¿Deseas crear una nueva reserva?""",parent=self.make_appointment_screen)

                if answer=='yes':
                    self.make_appointment_screen.destroy()
                    self.make_appointment_screen=Toplevel(self.appointment_screen)
                    self.objectMakeAppointment=MakeAppointmentScreen(self.make_appointment_screen,self.appointment_screen)

                else:
                    self.make_appointment_screen.destroy()

                print(answer)

        elif objectmessage==False:
                messagebox.showerror("Error de sistema","Contacte al administrador",parent=self.make_appointment_screen)