
from Common_classes.Class_Query import *

class Validation():
    def __init__(self):
        self.state=False
        self.admin_username=''
        self.query=Query()
    
    def loginValidation(self,user,password):
        self.user=user
        self.password=password
        if self.user=='' or self.password=='':
            self.state='NotInformation'
            return(self.state)
        parameter=(self.user,)
        self.queryresult=self.query.q_SearchAdminUser(parameter)
        if self.queryresult==[]:
            self.state='NotUser'
            return (self.state)
        else:
            for db_info in self.queryresult:
                self.__admin_id=db_info[0]
                self.__admin_user=db_info[1]
                self.admin_username=db_info[2]
                self.__admin_password=db_info[3]

                if self.user==self.__admin_user and self.password==self.__admin_password:
                    self.state=True
                    return(self.state)
                else:
                    return(self.state)
        
        return self.state
    