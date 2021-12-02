from Common_classes.Class_Query import Query


class Appoitments:
    def __init__(self):
        self.query = Query()
        pass


    def Turnos(self,fecha_i,fecha_j):
        from datetime import date, datetime, timedelta
        self.fecha_i_formateada = datetime.strptime(fecha_i, '%Y-%m-%d %H:%M:%S')
        self.fecha_j_formateada=datetime.strptime(fecha_j, '%Y-%m-%d %H:%M:%S')
        # print(diassolos)
        hours_week=15
        hours_weekend=11
        list=[]
        num_fields=7

        fecha_inicial1=self.fecha_i_formateada

        while fecha_inicial1 <=self.fecha_j_formateada:
            if str(fecha_inicial1.weekday())=='0' or str(fecha_inicial1.weekday())=='1'or str(fecha_inicial1.weekday())=='2'or str(fecha_inicial1.weekday())=='3'or fecha_inicial1.today=='4':
                inicializador=0
                fecha_inicial=fecha_inicial1
                while inicializador<=hours_week:
                    fields=1
                    list_fields=[]
                    hora1=fecha_inicial
                    while fields<=num_fields:
                        list_fields.append([str(hora1.strftime('%Y-%m-%d')),str(hora1.strftime('%H')),fields])
                        fields+=1

                    list.append(list_fields)
                    fecha_inicial=fecha_inicial+timedelta(hours=1)
                    inicializador+=1

            else:
                inicializador_else=0
                fecha_inicial_else=fecha_inicial1
                while inicializador_else<=hours_weekend:
                    fields=1
                    list_fields=[]
                    hora1=fecha_inicial_else
                    while fields<=num_fields:
                        list_fields.append([str(hora1.strftime('%Y-%m-%d')),str(hora1.strftime('%H')),fields])
                        fields+=1

                    list.append(list_fields)
                    fecha_inicial_else=fecha_inicial_else+timedelta(hours=1)
                    inicializador_else+=1 
                
            fecha_inicial1+=timedelta(days=1)
        return list

    def createAppointmentsDates(self,fecha_i,fecha_j):
        self.status=False
        self.appointments_created=self.Turnos(fecha_i,fecha_j)
        try:
            for i in self.appointments_created:
                for j in i:
                    parameters=(j[0],j[1],j[2],'')
                    
                    self.query.q_CreateAppointment(parameters)
            self.status =True
            return(self.status)
        except:
            return(self.status)
    
    def createUserAppointment(self,name,date,hour,field):
        self.__name=name
        self.__date=date
        self.__hour=hour
        self.__field=field
        self.returnMessage=False

        if self.__name=='' or self.__date=='' or self.__hour=='' or self.__field=='':
            self.returnMessage='InfoNotComplete'
            return(self.returnMessage)
        else:
            try:
                parameters_i=(str(self.__name),str(self.__date),str(self.__hour),str(self.__field))
                
                self.query.q_CreateUserAppointment(parameters_i)

                self.returnMessage='AppointmentCreated'
                return(self.returnMessage)
            except:
                return (self.returnMessage)

        

