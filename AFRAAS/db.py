import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path


class db:
    def __init__(self) -> None:
        dotenv_path = Path(r'AFRAAS\resources\user.env')
        load_dotenv(dotenv_path = dotenv_path)
        self.conn = mysql.connector.connect(
            host=os.getenv('AFRAAS_HOST'),
            user=os.getenv('AFRAAS_USER'),
            password=os.getenv('AFRAAS_PASSWORD'),
            database=os.getenv('AFRAAS_DATABASE'),
        )

    def check(self):
        cursor = self.conn.cursor()
        cursor.execute("select table_name, table_type, table_schema from information_schema.TABLES where table_schema like 'afraas';")
        

    def addNewUser(self,name, dept_id, shift_id):
        cursor = self.conn.cursor()
        cursor.execute("show databases")
        pass
    def deleteUser(self, user_id, name=""):
        pass
    def updateUserDetails(self, user_id, args):
        pass
    def viewAllUsers(self):
        pass

    def addNewDept(self, dept_name):
        pass
    def updateDeptName(self, dept_id, new_name):
        pass
    def deleteDept(self, dept_id):
        pass
    def viewAllDepts(self):
        pass

    def addNewShift(self, time_in, time_out):
        pass
    def updateShift(self, shift_id, time_in=0, time_out=0):
        pass
    def deleteShift(self, shift_id):
        pass
    def viewAllShifts(self):
        pass

    def markAttendance(self, user_id, status):
        pass
    def viewAttendanceTable(self, From, To):
        pass

    def executeCustomQuery(self, query):
        pass
