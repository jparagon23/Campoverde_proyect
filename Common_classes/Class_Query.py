import sqlite3
class Query:
    def __init__(self):
        pass
    def q_CreateUser(self,parameters):
        self.parameters=parameters
        self.query='INSERT INTO members VALUES(?,?,?,?,?)'
        self.run_query(self.query,self.parameters)

    def q_CreateAdminUser(self,parameters):
        self.parameters=parameters
        self.query='INSERT INTO admin_members VALUES(?,?,?,?)'
        self.run_query(self.query,self.parameters)
    
    def q_SearchAdminUser(self,parameters):
        self.parameters=parameters
        self.query='SELECT * FROM user_admi where user=?'
        data_info=self.run_query(self.query,self.parameters)
        return data_info
    def q_CreateAppointment(self,parameters):
        self.parameters=parameters
        self.query='INSERT INTO appointments VALUES(?,?,?,?)'
        self.run_query(self.query,self.parameters)
    def q_allMembers(self):
        self.query='SELECT name FROM members'
        data_info=self.run_query(self.query)
        return data_info

    def q_CreateUserAppointment(self,parameters):
        self.parameters=parameters
        self.query='UPDATE appointments SET mem_assign=? where date=? and hour=? and field=?'
        self.run_query(self.query,self.parameters)
    
    def q_createListFields(self,parameter):
        self.parameters=parameter
        self.query='select field from appointments where date=? and mem_assign=? and hour=?'
        data_info=self.run_query(self.query,self.parameters)
        return data_info
        
    def q_createListhours(self,parameter):
        self.parameters=parameter
        self.query="select distinct hour from appointments where mem_assign=? and date=?"
        data_info=self.run_query(self.query,self.parameters)
        return data_info
    def q_initial_list_appointment(self):    
        self.query='SELECT name FROM members'
        data_info=self.run_query(self.query)
        return data_info


    def run_query(self,query,parameters=()):
        db_name='Campo_bd.db'
        with sqlite3.connect(db_name) as conn:
            cursor= conn.cursor()
            result=cursor.execute(query,parameters)
            check=cursor.fetchall()
            conn.commit()
        return check