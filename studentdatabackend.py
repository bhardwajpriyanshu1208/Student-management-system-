import sqlite3 as sq
class student_data:
	def __init__(self,file_name):
		self.con=sq.connect(file_name)
		self.cur = self.con.cursor()
	def create_table(self):
		q = '''
			CREATE TABLE IF NOT EXISTS student(
			id INTEGER PRIMARY KEY,
			Class text,
			Firstname text,
			Surname text, 
			DOB text,
			Gender text,
			Address text,
			Mobile text,
			Fathername text
			)
			'''
		self.cur.execute(q)
		self.con.commit()

	def addStdRec(self,Class, Firstname, Surname, DOB, 
				Gender, Address, Mobile, FatherName):

		q  = '''
				INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)
			'''
		self.cur.execute(q,(Class,
							Firstname,
							Surname,
							DOB,
							Gender,
							Address,
							Mobile,
							FatherName))
		self.con.commit()

	 
	def viewData(self):

		q  = '''
				SELECT * FROM student
			'''
		self.cur.execute(q)
		rows = self.cur.fetchall()
		return rows

	def deleteRec(self,id):

		q  = '''
				DELETE FROM student
				WHERE id =?
			'''
		self.cur.execute(q,(id,))
		self.con.commit()


	def searchData(self,Class ='',
				Firstname='',
				Surname='',
				DOB='',
				Gender='',
				Address='',
				Mobile='',
				FatherName=''):
		
		q  = '''
				SELECT * FROM student
				WHERE Class =? 
					OR Firstname=? 
					OR Surname =? 
					OR DOB=? 
					OR GEnder=? 
					OR Address=? 
					OR Mobile=? 
					OR Fathername=?
			'''
		self.cur.execute(q,(Class,
							Firstname,
							Surname,
							DOB,
							Gender,
							Address,
							Mobile,
							FatherName))
		rows = self.cur.fetchall()
		return rows

	def dataUpdate(self,id,Class='',
							Firstname='',
							Surname='',
							DOB='',
							Gender='',
							Address='',
							Mobile='',
							FatherName=''):
		q  = '''
				UPDATE student
				SET Class=?,
					Firstname=?,
					Surname=?,
					DOB=?,
					Gender=?,
					Address=?,
					Mobile=?,
					FatherName=?
				WHERE id =?;
			'''
		self.cur.execute(q,(Class,
							Firstname,
							Surname,
							DOB,
							Gender,
							Address,
							Mobile,
							FatherName,
							id))
		self.con.commit()

	def exitdatabase(self):
		self.con.close()
		print('database closed sucessfully')

	def getlastrecordid(self):
	
		q = '''SELECT * FROM student
			WHERE ID = (
    		SELECT MAX(ID) FROM student)'''
		self.cur.execute(q)
		lastrec = self.cur.fetchone()
		return lastrec[0]