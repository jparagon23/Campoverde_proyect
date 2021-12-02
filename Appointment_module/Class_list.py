from typing import List

from Common_classes.Class_Query import Query


class Listinfo:
    def __init__(self):
        self.query=Query()


    def create_fields_list(self,date,hour):
        self.__date=date
        self.__hour=hour
        parameters_i=(str(self.__date),'',str(self.__hour))
        db_info=self.query.q_createListFields(parameters_i)
        self.list_fields=[]
        for row in db_info:
            self.list_fields.append(row[0])
        return self.list_fields
    def create_hours_list(self,member,date):
        self.__member=member
        self.__date=date
        parameters_i=('',str(self.__date))
        db_info=self.query.q_createListhours(parameters_i)
        self.list_fields=[]
        for row in db_info:
            self.list_fields.append(row[0])
        return self.list_fields

     


