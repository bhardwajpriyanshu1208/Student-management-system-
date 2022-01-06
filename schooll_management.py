import csv
import os
os.chdir('C:/Users/psbd1/OneDrive/Desktop/Project/Student_management_csv')
from tabulate import tabulate
def clear():
	os.system('cls')
class Student:
	admission_no =0
	classes_dict = {x:0 for x in range(1,13)}
	s_list=[]
	houses = ["Vivekanand","Mother Teresa","Rani Laxmi Bai", "Tagore"]
	def admission(self):
		self.admission_no += 1
		print("enter name :",end = " ")
		name = input()
		while name.isalpha() == False:
			name = input("Please enter Valid name : ")
		print("enter class :",end = " ")
		Class = input()
		while Class.isdigit() == False or int(Class) not in range(0,13):
			Class = input("Please enter A VALID CLASS from range 0 to 12 : ")
		Class = int(Class)

		Father_firstname = input("Enter Father's First name : ")
		while Father_firstname.isalpha() == False:
			Father_firstname = input("Please enter Valid name : ")
		Father_lastname = input("Enter Father's Last name : ")
		while Father_lastname.isalpha() == False and Father_lastname!="":
			Father_lastname = input("Please enter Valid name : ")
		Father_name = Father_firstname + " " + Father_lastname
		house = self.houses[self.admission_no%4]
		self.s_list.append([self.admission_no,name,Class,Father_name,house])
		self.updatefile()
		print("Admission Successful , Admission no is : {}"
									.format(self.admission_no))

	def search(self):
		no = input("Enter Admission no. : ")
		while no.isdigit()==False:
			no = input("Please enter a valid number")
		while int(no)>int(self.s_list[-1][0]) or int(no)<1 :
			no = input("Please enter a valid number in range {} : "
						.format(int(self.s_list[-1][0])))
		for o in self.s_list[1:]:
			if int(o[0]) == int(no):
				print("Name : ",o[1])
				print("Father_name : ",o[3])
				print("Class : ", o[2])
				return self.s_list.index(o)
		else:
			print("No student Found")
			return -1


	def delete(self):
		no = self.search()
		if no != -1:
			decision = input("are you sure to delete this object :(y/n)\n")
			while decision!= "y" and decision != "n":
				decision = input("are you sure to delete this object :(y/n)\n")
			if decision == "y":
				del self.s_list[no]
				print("Deleted")
			else:
				print("command declined")
		self.updatefile()

	def edit(self):
		no = self.search()
		print("\nWhat do you want to edit in this students info \n")
		print("""	1. Name 
			2. Class
			3. Father Name
			4. All of these
			5. Back""")
		d = input()
		if d == "1":
			name = input("Enter new name : ")
			while name.isalpha() == False:
				name = input("Please enter Valid name : ")
			self.s_list[no][1] = name
		elif d == "2":
			Class = input("Enter new class : ")
			while Class.isdigit() == False or int(Class) not in range(0,13):
				Class = input("Please enter A VALID CLASS from range 0 to 12 : ")
			Class = int(Class)
			self.s_list[no][2]= Class
		elif d == "3":
			Father_firstname = input("Enter Father's First name : ")
			while Father_firstname.isalpha() == False:
				Father_firstname = input("Please enter Valid name : ")
			Father_lastname = input("Enter Father's Last name : ")
			while Father_lastname.isalpha() == False and Father_lastname!="":
				Father_lastname = input("Please enter Valid name : ")
			Father_name = Father_firstname + " " + Father_lastname
			self.s_list[no][3] = Father_name

		elif d=="4":
			self.admission_no += 1
			print("enter name :",end = " ")
			name = input()
			while name.isalpha() == False:
				name = input("Please enter Valid name : ")
			print("enter class :",end = " ")
			Class = input()
			while Class.isdigit() == False or int(Class) not in range(0,13):
				Class = input("Please enter A VALID CLASS from range 0 to 12 : ")
			Class = int(Class)

			Father_firstname = input("Enter Father's First name : ")
			while Father_firstname.isalpha() == False:
				Father_firstname = input("Please enter Valid name : ")
			Father_lastname = input("Enter Father's Last name : ")
			while Father_lastname.isalpha() == False and Father_lastname!="":
				Father_lastname = input("Please enter Valid name : ")
			Father_name = Father_firstname + " " + Father_lastname
			self.s_list[no][1] = name
			self.s_list[no][2] = Class
			self.s_list[no][3] = Father_name
		elif d=='5':
			return
		self.updatefile()
		print("Details edited successfully")


	def countstudents(self):
		Class = input("Enter Class : ")
		while Class.isdigit() == False or int(Class) not in range(0,13):
			Class = input("Please enter A VALID CLASS from range 0 to 12 : ")
		strength = 0
		for x in self.s_list:
			if x[2] == Class:
				strength+=1
		return(strength)

	def viewallstudents(self):
		print(tabulate(self.s_list))


	# def assignrollnos.(self):
	# 	Class = input("Enter Class : ")
	# 	while Class.isdigit() == False or int(Class) not in range(0,13):
	# 		Class = input("Please enter A VALID CLASS from range 0 to 12 : ")
	# 	for
	
	def updatefile(self):
		with open("students.csv","w",newline = "") as f:
			csv_writer = csv.writer(f,
									 delimiter=',',
									 quotechar='"', 
									 quoting=csv.QUOTE_MINIMAL)
			for ob in self.s_list:
				csv_writer.writerow(ob)

	def readfile(self):
		with open("students.csv","r") as f:
			csv_reader = csv.reader(f, delimiter=',')
			for line in csv_reader:
				self.s_list.append(line)


if __name__ == "__main__":
	School = Student()
	School.readfile()
	School.admission_no = int(School.s_list[-1][0])
	quit = False
	while not quit:
		clear()
		print("Students Management, enter your choice to continue")
		print("	1. New admission")
		print("	2. Search")
		print("	3. delete")
		print("	4. Edit")
		print("	5. find class strength")
		print("	6. View all Students")
		choice = input()
		if choice == "1":
			clear()
			School.admission()

		elif choice == "2":
			clear()
			School.search()

		elif choice == "3":
			clear()
			School.delete()

		elif choice == "4":
			clear()
			School.edit()


		elif choice == "5":
			clear()
			print(School.countstudents())

		elif choice == "6":
			clear()
			School.viewallstudents()

		else:
			print("Enter a valid choice")



		print("Press q to quit and c to continue")
		choice_2 = input()
		while choice_2!="q" and choice_2!="c":
			print("Press q to quit and c to continue")
			choice_2 = input()
		if choice_2 == "q":
			clear()
			quit = True
			exit()
		elif choice_2 == "c":
			clear()
			continue