from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from studentdatabackend import student_data 
from tkcalendar import *
import re

class Student:
	def __init__(self,root):
		self.root = root
		self.root.title('Student Database System')
		self.root.geometry("1530x700+150+50")
		self.root.config(bg = 'cadet blue')

		Class = StringVar()
		Firstname = StringVar()
		Surname = StringVar()
		self.DOB = StringVar()
		self.DOB.set('YYYY-MM-DD')
		
		self.Gender = StringVar()
		self.Gender.set('Select Gender')
		Address = StringVar()
		Mobile = StringVar()
		Fathername = StringVar()
		
		############################# Functions ################################
		def iExit():
			iExit = tkinter.messagebox.askyesno('Student Database System',
												'Confirm if you want to exit')
			if iExit:
				root.destroy()
			return
		
		def clearData():
			self.txtClass.delete(0,END)
			self.txtfna.delete(0,END)
			self.txtSna.delete(0,END)
			# self.txtDOB.delete(0,END)
			# self.txtG.delete(0,END)
			self.Gender.set('Select Gender')
			self.txtAd.delete(0,END)
			self.txtMno.delete(0,END)
			self.txtfaname.delete(0,END)

		def addData():
			if checkvalidations() == 0:
				


					data.addStdRec(Class.get(), 
								Firstname.get(), 
								Surname.get(), 
								DOB.get(), 
								self.Gender.get(), 
								Address.get(), 
								Mobile.get(), 
								Fathername.get())
					studentlist.delete(0,END)
					a = data.getlastrecordid()
					studentlist.insert(END,(a,Class.get(),
									 Firstname.get(),
									 Surname.get(), 
									 DOB.get(), 
									 self.Gender.get(), 
									 Address.get(), 
									 Mobile.get(), 
									 Fathername.get()))
			clearData()

		def displayData():
			studentlist.delete(0,END)
			for row in data.viewData():
				studentlist.insert(END,row,str(''))


		def StudentRec(event):
			global sd
			if studentlist.curselection():
				# print(studentlist.curselection())
				searchStd = studentlist.curselection()[0]
				if searchStd % 2 == 0:
					sd = studentlist.get(searchStd)
					self.txtClass.delete(0,END)
					self.txtClass.insert(END,sd[1])
					self.txtfna.delete(0,END)
					self.txtfna.insert(END,sd[2])
					self.txtSna.delete(0,END)
					self.txtSna.insert(END,sd[3])
					# self.txtDOB.delete(0,END)
					# self.txtDOB.insert(END,sd[4])
					# self.txtG.delete(0,END)
					# self.txtG.insert(END,sd[5])
					self.Gender.set(sd[5])
					self.txtAd.delete(0,END)
					self.txtAd.insert(END,sd[6])
					self.txtMno.delete(0,END)
					self.txtMno.insert(END,sd[7])
					self.txtfaname.delete(0,END)
					self.txtfaname.insert(END,sd[8])

		def checkvalidations():
			a = 0
			#######  Class ###########
			try:
				if (int(Class.get()) not in range(0,13)):
					self.txtClass.delete(0,END)
					tkinter.messagebox.showerror('Invalid Input',
												'Enter an integer from range 0-12')
					a = 1
			except ValueError as e:
				self.txtClass.delete(0,END)
				tkinter.messagebox.showerror('Invalid Input',
											'Enter an integer from range 0-12')
				a = 1
			###### Fisrt name ################
			x = re.match('[a-zA-z]+',Firstname.get())
			
			try:
				if x.string != x.group():
					self.txtFirstname.delete(0,END)
					tkinter.messagebox.showerror('Invalid Input',
												'Please enter a valid Name')
					a = 1	
			except AttributeError :
					tkinter.messagebox.showerror('Invalid Input',
												'Please enter a name')
					a = 1

			except Exception:
					tkinter.messagebox.showerror('Invalid Input',
												'An unexpected error occured')
					a = 1
			
			#########Surname#######33

			x = re.match('[a-zA-z]+',Surname.get())
			
			try:
				if x.string != x.group():
					self.txtSurname.delete(0,END)
					tkinter.messagebox.showerror('Invalid Input',
												'Please enter a valid Name')
					a = 1	
			except AttributeError :
					pass

			except Exception:
					tkinter.messagebox.showerror('Invalid Input',
												'An unexpected error occured')
					a = 1

			########### Address #############

			x = re.match(r'[\w + \s + ,]+',Address.get())
			s = 'Address should not contain any special character'
			try:
				if x.string != x.group():
					self.txtAd.delete(0,END)
					tkinter.messagebox.showerror('Invalid Input',
												s)
					a = 1	
			except AttributeError:
					tkinter.messagebox.showerror('Invalid Input',
												'Please enter an Address')
					a = 1

			except Exception:
					tkinter.messagebox.showerror('Invalid Input',
												'An unexpected error occured')
					a = 1
			x = re.match(r'[(a-zA-z) + \s]+',Fathername.get())
			try:
				if x.string != x.group():
					self.txtfaname.delete(0,END)
					tkinter.messagebox.showerror('Invalid Input',
												'Please enter correct Fathername')
					a = 1	
			except AttributeError:
					tkinter.messagebox.showerror('Invalid Input',
												'Please enter a Fathername')
					a = 1

			except Exception:
					tkinter.messagebox.showerror('Invalid Input',
												'An unexpected error occured')
					a = 1
			if self.Gender.get() != 'Male' and self.Gender.get() != 'Female':
				tkinter.messagebox.showerror('Invalid Input(Gender)',
											'Select a valid choice')
				a = 1

			x = re.match(r'\d{10}',Mobile.get())
			try:
				if x.string != x.group():
					self.txtMno.delete(0,END)
					tkinter.messagebox.showerror('Invalid Input',
												'Please enter a valid Mobile no.')
					a = 1	
			except AttributeError:
					tkinter.messagebox.showerror('Invalid Input',
												'Please enter a valid Mobileno.')
					a = 1

			except Exception:
					tkinter.messagebox.showerror('Invalid Input',
												'An unexpected error occured')
					a = 1

			return a
		def DeleteData():
			
				try :
					data.deleteRec(sd[0])
					clearData()
					displayData()
				except NameError:
					tkinter.messagebox.showerror('Invalid Selection',
											'Selecct a Record First')

		def SearchData():
			studentlist.delete(0,END)
			a =	data.searchData(Class.get(),
											Firstname.get(),
											Surname.get(), 
											DOB.get(), 
											self.Gender.get(), 
											Address.get(), 
											Mobile.get(), 
											Fathername.get())
			for row in a:
				studentlist.insert(END,row,"")

		def update():
			if checkvalidations() == 0:	
				try :
					data.dataUpdate(sd[0],Class.get(),
									Firstname.get(), 
									Surname.get(), 
									DOB.get(), 
									self.Gender.get(), 
									Address.get(), 
									Mobile.get(), 
									Fathername.get())
					displayData()
				except NameError:
					tkinter.messagebox.showerror('Invalid Selection',
												'Please select a reccord first')

		def select_date():
			win= Tk()
			win.title("Calendar")
			win.geometry("300x200")

			cal= Calendar(win, selectmode="day",year= 2021, month=1, day=1)
			cal.pack(pady=20)

			#Define Function to select the date
			def get_date():
			   label.config(text=cal.get_date())

			#Create a button to pick the date from the calendar
			button= Button(win, text= "Select the Date", command= get_date)
			button.pack(pady=20)

			#Create Label for displaying selected Date
			label= Label(win, text="")
			label.pack(pady=20)

			win.mainloop()
			
		################################ Frame ###############################
		
		MainFrame = Frame(self.root,bg='cadet blue')
		MainFrame.grid()

		TitFrame = Frame(MainFrame, bd = 2 , padx = 200, pady = 8, bg = 'black')
		TitFrame.pack(side = TOP)

		self.lblTit = Label(TitFrame ,
					 font=('arial',47,'bold'),
					 text = 'Student Database Management', 
					 bg = 'black',
					 foreground = 'white')
		self.lblTit.grid()

		ButtonFrame = Frame(MainFrame, 
							bd = 2, 
							width = 1350, 
					
							height = 70, 
							padx = 18,
							pady = 10, 
							bg = 'ghost white', 
							relief = RIDGE)
		ButtonFrame.pack(side =BOTTOM)

		DataFrame = Frame(MainFrame, 
							bd = 1, 
							width = 1300, 
							height = 400, 
							padx = 20,
							pady = 20, 
							bg = 'cadet blue', 
							relief = RIDGE)
		DataFrame.pack(side = BOTTOM)

		DataFrameLEFT = LabelFrame(DataFrame, 
									bd = 1, 
									width = 1000, 
									height = 600, 
									padx = 20, 
									bg = 'ghost white', 
									relief = RIDGE,
									font = ('arial',20,'bold'), 
									text = 'Student Info\n')
		DataFrameLEFT.pack(side = LEFT)

		DataFrameRIGHT = LabelFrame(DataFrame,
									bd = 1, 
									width = 450, 
									height = 300, 
									padx = 31, 
									pady = 3 ,
									bg = 'ghost white', 
									relief = RIDGE,
									font = ('arial',20,'bold'), 
									text = 'Student Details\n')
		DataFrameRIGHT.pack(side = RIGHT)

		########################### Labels and Entries #######################
		self.lblClass = Label(DataFrameLEFT ,
							 font=('arial',20,'bold'),
							 text = 'Class : ',
							 padx = 2, pady=2,
							 bg = 'ghost white')
		self.lblClass.grid(row=0,column=0,sticky=W)
		self.txtClass = Entry(DataFrameLEFT , 
							  font=('arial',20,'bold'),
							  textvariable = Class, 
							  width = 39)
		self.txtClass.grid(row=0,column=1)

		self.lblfna = Label(DataFrameLEFT ,
							font=('arial',20,'bold'),
							text = 'First Name : ', 
							padx = 2, pady=2, 
							bg = 'ghost white')
		self.lblfna.grid(row=1,column=0,sticky=W)
		self.txtfna = Entry(DataFrameLEFT ,
							font=('arial',20,'bold'),
							textvariable = Firstname,
							width = 39)
		self.txtfna.grid(row=1,column=1)

		self.lblSna = Label(DataFrameLEFT ,
							font=('arial',20,'bold'),
							text = 'Surname : ', 
							padx = 2, pady=2, 
							bg = 'ghost white')
		self.lblSna.grid(row=2,column=0,sticky=W)
		self.txtSna = Entry(DataFrameLEFT , 
							font=('arial',20,'bold'),
							textvariable = Surname, 
							width = 39)
		self.txtSna.grid(row=2,column=1)

		self.lblDOB = Label(DataFrameLEFT , 
						font=('arial',20,'bold'),
						text = 'Date of Birth : ', 
						padx = 2, pady=2, 
						bg = 'ghost white')
		self.lblDOB.grid(row=3,column=0,sticky=W)
		self.txtDOB = Label(DataFrameLEFT,
							font=('arial',20),
							textvariable = self.DOB,
							width = 35,bg = 'white')
		self.txtDOB.grid(row=3,column=1,sticky = W)

		self.btnDOB = Button(DataFrameLEFT,
							font=('arial',20,'bold'),
							text = 'Select Date',
							command = select_date)
		self.btnDOB.grid(row=3,column=2)


		self.lblG = Label(DataFrameLEFT ,
						font=('arial',20,'bold'),
						text = 'Gender : ',
						padx = 2, pady=2, 
						bg = 'ghost white')
		self.lblG.grid(row=4,column=0,sticky=W)
		self.txtG = OptionMenu(DataFrameLEFT,self.Gender,'Male','Female')
		self.txtG.config(font = 'Arial 18',width = 39)
		self.txtG.grid(row=4,column=1)

		self.lblAd = Label(DataFrameLEFT , 
						font=('arial',20,'bold'),
						text = 'Address: ', 
						padx = 2, pady=2, 
						bg = 'ghost white')
		self.lblAd.grid(row=5,column=0,sticky=W)
		self.txtAd = Entry(DataFrameLEFT , 
							font=('arial',20,'bold'),
							textvariable = Address, 
							width = 39)
		self.txtAd.grid(row=5,column=1)


		self.lblMno = Label(DataFrameLEFT , 
							font=('arial',20,'bold'),
							text = 'Mobile No : ', 
							padx = 2, pady=2, 
							bg = 'ghost white')
		self.lblMno.grid(row=6,column=0,sticky=W)
		self.txtMno = Entry(DataFrameLEFT , 
							font=('arial',20,'bold'),
							textvariable = Mobile, 
							width = 39)
		self.txtMno.grid(row=6,column=1)


		self.lblfaname = Label(DataFrameLEFT , 
								font=('arial',20,'bold'),
								text = 'Father\'s Name : ', 
								padx = 2, 
								pady=2, 
								bg = 'ghost white')
		self.lblfaname.grid(row=7,column=0,sticky=W)
		self.txtfaname = Entry(DataFrameLEFT ,
							font=('arial',20,'bold'),
							textvariable = Fathername, 
							width = 39)
		self.txtfaname.grid(row=7,column=1)

		################################## Listbox and Scrollbar ###################
		scrollbar = Scrollbar(DataFrameRIGHT)
		scrollbar.grid(row=0,column=1,sticky='ns')

		studentlist = Listbox(DataFrameRIGHT, 
							width = 41, height=16, 
							font =('arial',12,'bold'), 
							yscrollcommand=scrollbar.set)
		studentlist.bind('<<ListboxSelect>>', StudentRec)
		studentlist.grid(row = 0, column =0, padx=8)
		scrollbar.config(command = studentlist.yview)


		################################## Button Widgets ###########################
		self.btnAddData = Button(ButtonFrame,
								command =addData, 
								text="Add New", 
								font = ('arial',20,'bold'), 
								height = 1, width = 10, 
								bd =4)
		self.btnAddData.grid(row =0,column=0)

		self.btnDisplayData = Button(ButtonFrame,
									command = displayData, 
									text="Display", 
									font = ('arial',20,'bold'), 
									height = 1, width = 10, 
									bd =4)
		self.btnDisplayData.grid(row =0,column=1)

		self.btnClearData = Button(ButtonFrame,
									command = clearData, 
									text="Clear", 
									font = ('arial',20,'bold'), 
									height = 1, width = 10, 
									bd =4)
		self.btnClearData.grid(row =0,column=2)

		self.btnDeleteData = Button(ButtonFrame,
									command = DeleteData, 
									text="Delete", 
									font = ('arial',20,'bold'), 
									height = 1, width = 10, 
									bd =4)
		self.btnDeleteData.grid(row =0,column=3)

		self.btnSearchData = Button(ButtonFrame,
									command = SearchData, 
									text="Search", 
									font = ('arial',20,'bold'), 
									height = 1, width = 10, 
									bd =4)
		self.btnSearchData.grid(row =0,column=4)

		self.btnUpdateData = Button(ButtonFrame,
									command = update, 
									text="Update", 
									font = ('arial',20,'bold'), 
									height = 1, width = 10, 
									bd =4)
		self.btnUpdateData.grid(row =0,column=5)

		self.btnExit = Button(ButtonFrame,
								text="Exit",
								command = iExit, 
								font = ('arial',20,'bold'), 
								height = 1, width = 10, bd =4)
		self.btnExit.grid(row =0,column=6)


if __name__ =='__main__':
	root = Tk()
	root.iconbitmap('C:/Users/psbd1/OneDrive/Desktop/Project/Studentmanagement_sqlite/school.ico')
	data = student_data('students.db')
	app = Student(root)

	# photo = PhotoImage(file = "schoolicon3.png")
	# root.iconphoto(False, photo)
	root.mainloop()
	data.exitdatabase()
