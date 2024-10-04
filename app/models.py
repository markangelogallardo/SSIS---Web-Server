from app import mysql


class Students(object):
    def __init__(self, id_num=None, f_name=None, l_name=None, prog=None, year_lvl=None, gender=None):
        self.id = id_num
        self.f_name = f_name
        self.l_name = l_name
        self.prog = prog
        self.year_lvl = year_lvl
        self.gender = gender


    def add(self):
        cursor = mysql.connection.cursor()

        sql = f"INSERT INTO students(ID_Number,First_Name,Last_Name,Program_Code,Year_Level,Gender) \
                VALUES('{self.id}',('{self.f_name}'),'{self.l_name}','{self.prog}','{self.year_lvl}','{self.gender}')" 

        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM students"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    