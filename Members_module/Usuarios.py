from Common_classes.Class_Query import Query
class Usuario():
    def __init__(self, name, lastName,id,phone,email,birthdate):
        self.name = name
        self.lastName=lastName
        self.id=id
        self.phone = phone
        self.email=email
        self.birthdate=birthdate 
        self.query = Query()

    def createUser(self):
        if self.name=='' or self.lastName=='' or self.id=='':
            return('Emptyfield')
        try:
            parameters=(self.id,self.name+' '+self.lastName,self.phone,self.email,self.birthdate)

            self.query.q_CreateUser(parameters)
            return True
        except:
            return('CreateUserProblem')
    def showAllUsers(self):
        self.list_members=[]
        db_rows=self.query.q_allMembers()
        for row in db_rows:
            self.list_members.append(row[0])
        return self.list_members



class Admin_user(Usuario):
    def __init__(self, name, lastName, id, password,userAdmin):
        super().__init__(name, lastName, id)
        self.password=password
        self.userAdmin=userAdmin

    def createUser(self):
        if self.name=='' or self.lastName=='' or self.id=='' or self.password=='' or self.userAdmin=='':
            return('Emptyfield')
        try:
            parameters=(self.id,self.name+' '+self.lastName,self.userAdmin,self.password)

            self.query.q_CreateUser(parameters)
            return True
        except:
            return('CreateUserProblem')
