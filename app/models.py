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

        sql = """INSERT INTO students(ID_Number,First_Name,Last_Name,Program_Code,Year_Level,Gender)
                VALUES(%s, %s, %s, %s, %s, %s)""" 

        cursor.execute(sql, (self.id, self.f_name, self.l_name, self.prog, self.year_lvl, self.gender))
        mysql.connection.commit()
    def edit(self):
        cursor = mysql.connection.cursor()
        sql = """UPDATE students SET ID_Number = %s, First_Name = %s, Last_Name = %s, Program_Code = %s, Year_Level = %s, Gender = %s WHERE ID_Number = %s"""
        cursor.execute(sql, (self.id, self.f_name, self.l_name, self.prog, self.year_lvl, self.gender, self.id))
        mysql.connection.commit()

    @classmethod
    def delete(cls, student_id):
        try:
            cursor = mysql.connection.cursor()
            sql = """DELETE FROM students WHERE ID_Number = %s"""
            cursor.execute(sql, (student_id,))
            mysql.connection.commit()
            return True
        except:
            return False
    

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM students"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def get(id_num):
        cursor = mysql.connection.cursor()
        val = (id_num,)
        sql = "SELECT * FROM students WHERE ID_Number = %s"
        cursor.execute(sql, val)
        return cursor.fetchone()

    def input_error(error):
        if(error.args[0] == 1062):
            err_cause = error.args[1].split("'")[1]
            if(len(err_cause) == 9 and err_cause[4]=='-'):
                return f"Inputted ID Number '{err_cause}' already exists. Plz Change."
            else:
                name = err_cause.replace("-", " ")
                return f"Inputted name '{name}' already exists."
    
class Programs(object):
    def __init__(self, prog_code=None, prog_name=None, college_code=None, new_prog_code=None):
        self.prog_code = prog_code
        self.prog_name = prog_name
        self.college_code = college_code
        self.new_prog_code = new_prog_code

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM programs"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def get(prog_code):
        cursor = mysql.connection.cursor()
        val = (prog_code,)
        sql = "SELECT * FROM programs WHERE Program_Code = %s"
        cursor.execute(sql, val)
        return cursor.fetchone()

    def add(self):
        cursor = mysql.connection.cursor()

        sql = """INSERT INTO programs(Program_Code,Program_Name,College_Code)
                VALUES(%s, %s, %s)""" 
        cursor.execute(sql, (self.prog_code, self.prog_name, self.college_code))
        mysql.connection.commit()
    def edit(self):
        cursor = mysql.connection.cursor()
        sql = """UPDATE programs SET Program_Code = %s, Program_Name = %s, College_Code = %s WHERE Program_Code = %s"""
        cursor.execute(sql, (self.new_prog_code, self.prog_name, self.college_code, self.prog_code))
        mysql.connection.commit()

    @classmethod
    def delete(cls, prog_code):
        try:
            cursor = mysql.connection.cursor()
            sql = """DELETE FROM programs WHERE Program_Code = %s"""
            cursor.execute(sql, (prog_code,))
            mysql.connection.commit()
            return True
        except:
            return False

    def input_error(error):
        if(error.args[0] == 1062):
            err_cause = error.args[1].split("'")[1]
            return f"Inputted program '{err_cause}' already exists."

class Colleges(object):
    def __init__(self, college_code=None, college_name=None, new_college_code=None):
        self.college_code = college_code
        self.college_name = college_name
        self.new_college_code = new_college_code

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM colleges"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def get(prog_code):
        cursor = mysql.connection.cursor()
        val = (prog_code,)
        sql = "SELECT * FROM colleges WHERE College_Code = %s"
        cursor.execute(sql, val)
        return cursor.fetchone()

    def add(self):
        cursor = mysql.connection.cursor()

        sql = """INSERT INTO colleges(College_Code, College_Name)
                VALUES(%s, %s)""" 
        cursor.execute(sql, (self.college_code, self.college_name))
        mysql.connection.commit()

    def edit(self):
        cursor = mysql.connection.cursor()
        sql = """UPDATE colleges SET College_Code = %s, College_Name = %s WHERE College_Code = %s"""
        cursor.execute(sql, (self.new_college_code, self.college_code, self.college_code))
        mysql.connection.commit()

    @classmethod
    def delete(cls, college_code):
        try:
            cursor = mysql.connection.cursor()
            sql = """DELETE FROM colleges WHERE College_Code = %s"""
            cursor.execute(sql, (college_code,))
            mysql.connection.commit()
            return True
        except:
            return False

    def input_error(error):
        if(error.args[0] == 1062):
            err_cause = error.args[1].split("'")[1]
            return f"Inputted college '{err_cause}' already exists."