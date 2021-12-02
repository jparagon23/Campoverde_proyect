from tkinter import *
from Class_createDates import CreateDatesScreen
from Class_makeAppointment import MakeAppointmentScreen
class AppointmentsScreen:
    def __init__(self,screen):
        self.appointment_screen = screen
        self.appointment_screen.title('Reservas')

        #adicionamos los labels

        Label(self.appointment_screen, text = 'Menu de reservas').grid(row = 0, sticky=N)

        Button(self.appointment_screen,text='Habilitar turnos',font=('Calibri',12),width=30,command=lambda:self.create_dates()).grid(row=1,sticky=N,padx=10)
        
        Button(self.appointment_screen,text='Crear una reserva',font=('Calibri',12),width=30,command=lambda:self.make_appointment()).grid(row=2,sticky=N,padx=10)
        Button(self.appointment_screen,text='Consultar una reserva',font=('Calibri',12),width=30,command=lambda:self.nada()).grid(row=3,sticky=N,padx=10)
    
    def create_dates(self):
        self.create_dates_screen=Toplevel(self.appointment_screen)
        self.objectCreateDates=CreateDatesScreen(self.create_dates_screen)
        return
    def make_appointment(self):
        self.make_appointment_screen=Toplevel(self.appointment_screen)
        self.objectMakeAppointment=MakeAppointmentScreen(self.make_appointment_screen,self.appointment_screen)
        return
    def nada(self):
        return
    