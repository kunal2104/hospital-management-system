from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from datetime import date
import random
import time
import datetime
import re
import mysql.connector
import xlsxwriter

window = Tk()
window.title("Login")
window.geometry("1540x800+0+0")
window.configure(bg="#fff")
window.resizable(False,False)
window.iconbitmap("log.ico")
window.configure(bg="dark olive green")


lb=Label(window,text = "Hospital Management System",bg="dark olive green",fg="plum",font=('Microsoft YaHei UI Light',40,"bold underline"))
lb.place(x=100,y=40)

def clear():
	username.delete(0,END)
	code.delete(0,END)

def forgot_pass():
	def change_password():
		if username1.get()=="" or code1.get()=="" or code2.get()=="":
			messagebox.showerror("Error","All Fields Are Required", parent=window)
		elif code1.get() != code2.get():
			messagebox.showerror("Error","Password and Confirm Password are not matching", parent=window)
		else:
			con=pymysql.connect(host="localhost",user="root",password="kunaljain2104@",database="userdata")
			my_cursor=con.cursor()
			query="select * from data where username=%s"
			my_cursor.execute(query,(username1.get()))
			row=my_cursor.fetchone()
			if row==None:
				messagebox.showerror("Error","Invalid Username",parent=window)
			else:
				query="update data set password=%s where username=%s"
				my_cursor.execute(query,(code1.get(),username1.get()))		
				con.commit()
				con.close()
				messagebox.showinfo("Success","Password is reset, please login with new Password",parent=window)
				window.destroy()
	
	window=Toplevel()
	window.title("Change Password")
	window.geometry("1000x550+0+0")
	window.resizable(False,False)
	window.iconbitmap("log.ico")
	window.configure(bg="dark olive green")

	lb=Label(window,text = "Hospital Management System",bg="dark olive green",fg="plum",font=('Microsoft YaHei UI Light',30,"bold 	underline"))
	lb.place(x=80,y=20)

	frame=Frame(window,width=900,height=400,bg="white")
	frame.place(x=50, y=101)

	bgPic = PhotoImage(file="medical1.png")
	bglabel=Label(frame,image=bgPic,bg="white")
	bglabel.place(x=300,y=-1.5)

	heading = Label(frame,text="Reset Password", fg='black', bg='white',font=('Microsoft YaHei UI Light',20,"bold"))
	heading.place(x=45,y=20)

	def ue(event):
		if username1.get()=='Username':
			username1.delete(0,END)

	username1 = Entry(frame, width=30, fg="black", border=0,bg="white",font=('Microsoft YaHei UI Light',10,"bold"))
	username1.place(x=20,y=80)
	username1.insert(0,'Username')
	username1.bind('<FocusIn>', ue)

	Frame(frame,width=250,height=2,bg='black').place(x=15,y=100)

	def pe(event):
		if code1.get()=='New Password':
			code1.delete(0,END)

		
	code1 = Entry(frame, width=30, fg="black", border=0,bg="white",font=('Microsoft YaHei UI Light',10,"bold"))
	code1.place(x=20,y=160)
	code1.insert(0,'New Password')
	code1.bind('<FocusIn>',pe)
	Frame(frame,width=250,height=2,bg='black').place(x=15,y=180)
	

	def cpe(event):
		if code2.get()=="Change Password":
			code2.delete(0,END)

	code2=Entry(frame, width=30, fg="black", border=0,bg="white",font=('Microsoft YaHei UI Light',10,"bold"))
	code2.place(x=20,y=240)
	code2.insert(0,'Change Password')
	code2.bind('<FocusIn>', cpe)
	Frame(frame,width=250,height=2,bg='black').place(x=15,y=260)

	Button(frame,width=25,height=2,pady=15, text="Submit", bg="#57a1f8", fg="white", bd=0,font=('Microsoft YaHei UI Light',10,"bold"),cursor="hand2",activebackground="#57a1f8",	activeforeground="white",command=change_password).place(x=20,y=300)


	window.mainloop()

##################--------------------------------------------------------------------------------------------
def login_user():
	if username.get()=="" or code.get()=="":
		messagebox.showerror("Error","All Fields Are Required")
		
	else:
		try:
			con=pymysql.connect(host="localhost",user="root",password="kunaljain2104@")
			my_cursor=con.cursor()
		except:
			messagebox.showerror("Error","Connection is not established try again")
			return
		query = "use userdata"
		my_cursor.execute(query)
		query="select * from data where username=%s and password=%s"
		my_cursor.execute(query,(username.get(),code.get()))
		row=my_cursor.fetchone()
		if row==None:
			messagebox.showerror("Error","Invalid username or password")
			clear()
		else:
			messagebox.showinfo("Welcome","Login is Sucessful")
			clear()
			import mysql.connector
			
			class Hospital:
				def __init__(self, root):
					self.root = root
					self.root.title("Hospital Management System")
					self.root.geometry("1540x800+0+0")
					self.root.iconbitmap("hospital.ico")
					self.root.resizable(False,False)	
				
					
					self.NameOfTablets=StringVar()
					self.Ref=StringVar()
					self.Dose=StringVar()
					self.NumberOfTablets=StringVar()
					self.Lot=StringVar()
					self.IssueDate=StringVar()
					self.ExpDate=StringVar()
					self.DailyDose=StringVar()
					self.SideEffect=StringVar()
					self.FurtherInformation=StringVar()
					self.StorageAdvice=StringVar()
					self.DrivingUsingMachine=StringVar()
					self.HowToUseMedication=StringVar()
					self.PatientId=StringVar()
					self.NHSNumber=StringVar()
					self.PatientName=StringVar()
					self.DateOfBirth=StringVar()
					self.PatientAddress=StringVar()
		



					lbltitle = Label(root,bd=20,relief = RIDGE,text = "HOSPITAL MANAGEMENT SYSTEM",fg ="dark olive green",bg ="white", font = ("times new roman",50, "bold"))
					lbltitle.pack(side=TOP,fill =X)
	
					# ======================================Data Frame=====================================================
					DataFrame = Frame(root,bd=20,relief=RIDGE)
					DataFrame.place(x=0,y=130,width=1530,height = 400)
		
					DataFrameLeft =LabelFrame(DataFrame,bd=14,relief=RIDGE,padx=10,font = ("times new roman",12, "bold"), text = "Patient Information")
					DataFrameLeft.place(x=5,y=5, width=980,height=350)

					DataFrameRight =LabelFrame(DataFrame,bd=14,relief=RIDGE,padx=10,font = ("times new roman",12, "bold"), text = "Prescription")
					DataFrameRight.place(x=990,y=5, width=495,height=350)
		
					# =====================================Buttons Frame====================================================
		
					ButtonFrame = Frame(root,bd=13,relief=RIDGE)
					ButtonFrame.place(x=0,y=530,width=1530,height = 70)


		
					# =====================================Details Frame====================================================

					DetailsFrame = Frame(root,bd=10,relief=RIDGE)
					DetailsFrame.place(x=0,y=600,width=1530,height =190)


					# ====================================DataFrame Left======================================================
		
					lblNameTablet = Label(DataFrameLeft, text = "Names Of Tablet:",font = ("arial",12, "bold"), padx=2,pady=6)
					lblNameTablet.grid(row=0, column=0,sticky=W)
		
					comNametablet=ttk.Combobox(DataFrameLeft,textvariable=self.NameOfTablets ,font = ("arial",12, "bold"), width=33)
					comNametablet["values"]=("Nice","CoronaVacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
					comNametablet.grid(row=0, column=1)	

	
					lblRef = Label(DataFrameLeft, text = "Reference No:",font = ("arial",12, "bold"), padx=2)
					lblRef.grid(row=1, column=0,sticky=W)
					txtRef = Entry(DataFrameLeft,textvariable=self.Ref,font = ("times new roman",13, "bold"),width=35)
					txtRef.grid(row=1, column=1)

					lblDose = Label(DataFrameLeft, text = "Dose:",font = ("arial",12, "bold"), padx=2,pady=4)
					lblDose.grid(row=2, column=0,sticky=W)
					txtDose = Entry(DataFrameLeft,textvariable=self.Dose,font = ("arial",13, "bold"),width=35)
					txtDose.grid(row=2, column=1)

					lblNoOfTablets = Label(DataFrameLeft, text = "No Of Tablets:",font = ("arial",12, "bold"), padx=2, pady=6)
					lblNoOfTablets.grid(row=3, column=0,sticky=W)
					txtNoOfTablets = Entry(DataFrameLeft,textvariable=self.NumberOfTablets,font = ("arial",13, "bold"),width=35)
					txtNoOfTablets.grid(row=3, column=1)

					lblLot = Label(DataFrameLeft, text = "Lot:",font = ("arial",12, "bold"), padx=2, pady=6)
					lblLot.grid(row=4, column=0,sticky=W)
					txtLot = Entry(DataFrameLeft,textvariable=self.Lot,font = ("arial",13, "bold"),width=35)
					txtLot.grid(row=4, column=1)

					lblIssueDate = Label(DataFrameLeft, text = "Isuue Date:",font = ("arial",12, "bold"), padx=2, pady=6)
					lblIssueDate.grid(row=5, column=0,sticky=W)
					txtIssueDate = DateEntry(DataFrameLeft,textvariable=self.IssueDate,font = ("arial",13, "bold"),width=33,date_pattern="yyyy/mm/dd")
					txtIssueDate.grid(row=5, column=1)				
	
					lblExpDate = Label(DataFrameLeft, text = "Exp Date:",font = ("arial",12, "bold"), padx=2, pady=6)
					lblExpDate.grid(row=6, column=0,sticky=W)
					txtExpDate = DateEntry(DataFrameLeft,textvariable= self.ExpDate,font = ("arial",13, "bold"),width=33,date_pattern="yyyy/mm/dd")
					txtExpDate.grid(row=6, column=1)
					
					
					
					lblDailyDose = Label(DataFrameLeft, text = "Daily Dose:",font = ("arial",12, "bold"), padx=2, pady=6)
					lblDailyDose.grid(row=7, column=0,sticky=W)
					txtDailyDose = Entry(DataFrameLeft,textvariable=self.DailyDose,font = ("arial",13, "bold"),width=35)
					txtDailyDose.grid(row=7, column=1)
		
					lblSideEffect = Label(DataFrameLeft, text = "Side Effect:",font = ("arial",12, "bold"), padx=2, pady=6)
					lblSideEffect.grid(row=8, column=0,sticky=W)
					txtSideEffect = Entry(DataFrameLeft,textvariable=self.SideEffect,font = ("arial",13, "bold"),width=35)
					txtSideEffect.grid(row=8, column=1)
		
					lblFurtherInformation = Label(DataFrameLeft, text = "Further Information:",font = ("arial",12, "bold"), padx=2)
					lblFurtherInformation.grid(row=0, column=2,sticky=W)
					txtFurtherInformation = Entry(DataFrameLeft,textvariable=self.FurtherInformation,font = ("arial",12, "bold"),width=35)
					txtFurtherInformation.grid(row=0, column=3)
		
					lblBloodPressure = Label(DataFrameLeft, text = "Blood Pressure:",font = ("arial",12, "bold"), padx=2, pady=6)
					lblBloodPressure.grid(row=1, column=2,sticky=W)
					txtBloodPressure = Entry(DataFrameLeft,textvariable=self.DrivingUsingMachine,font = ("arial",12, "bold"),width=35)
					txtBloodPressure.grid(row=1, column=3)
		
					lblStorageAdivce = Label(DataFrameLeft, text = "Storage Adivce:",font = ("arial",12, "bold"), padx=2, pady=6)
					lblStorageAdivce.grid(row=2, column=2,sticky=W)
					txtStorageAdivce = Entry(DataFrameLeft,textvariable=self.StorageAdvice,font = ("arial",12, "bold"),width=35)
					txtStorageAdivce.grid(row=2, column=3)
		
					lblMedication = Label(DataFrameLeft, text = "Medication:",font = ("arial",12, "bold"), padx=2, pady=6)
					lblMedication.grid(row=3, column=2,sticky=W)
					txtMedication = Entry(DataFrameLeft,textvariable=self.HowToUseMedication,font = ("arial",12, "bold"),width=35)
					txtMedication.grid(row=3, column=3)
		
					lblPatientId = Label(DataFrameLeft, text = "Patient Id:",font = ("arial",12, "bold"), padx=2, pady=6)
					lblPatientId.grid(row=4, column=2,sticky=W)
					txtPatientId = Entry(DataFrameLeft,textvariable=self.PatientId,font = ("arial",12, "bold"),width=35)
					txtPatientId.grid(row=4, column=3)
		
					lblNHSNumber = Label(DataFrameLeft, text = "NHS Number:",font = ("arial",12, "bold"), padx=2, pady=6)
					lblNHSNumber.grid(row=5, column=2,sticky=W)
					txtNHSNumber = Entry(DataFrameLeft,textvariable=self.NHSNumber,font = ("arial",12, "bold"),width=35)
					txtNHSNumber.grid(row=5, column=3)
		
					lblPatientName = Label(DataFrameLeft, text = "Patient Name:",font = ("arial",12, "bold"), padx=2, pady=6)
					lblPatientName.grid(row=6, column=2,sticky=W)
					txtPatientName = Entry(DataFrameLeft,text=self.PatientName,font = ("arial",12, "bold"),width=35)
					txtPatientName.grid(row=6, column=3)
		
					lblDOB = Label(DataFrameLeft, text = "Date Of Birth:",font = ("arial",12, "bold"), padx=2, pady=6)
					lblDOB.grid(row=7, column=2,sticky=W)
					txtDOB = DateEntry(DataFrameLeft,textvariable=self.DateOfBirth,font = ("arial",12, "bold"),width=33,date_pattern="dd/mm/yyyy")
					txtDOB.grid(row=7, column=3)
				
					lblPatientAddress = Label(DataFrameLeft, text = "Patient Address:",font = ("arial",12, "bold"), padx=2, pady=6)
					lblPatientAddress.grid(row=8, column=2,sticky=W)
					txtPatientAddress = Entry(DataFrameLeft,textvariable=self.PatientAddress,font = ("arial",12, "bold"),width=35)
					txtPatientAddress.grid(row=8, column=3)
		
					# ===================================================DataFrameRight======================================================
					scrollbar_y =ttk.Scrollbar(DataFrameRight,orient=VERTICAL)	
					self.txtPrescription=Text(DataFrameRight,font = ("arial",12, "bold"),width = 47, height=16,padx=3,pady=5,yscrollcommand=scrollbar_y.set)
					self.txtPrescription.place(x=0,y=0)	
								
					scrollbar_y.pack(side=RIGHT,fill=Y)
					scrollbar_y.config(command=self.txtPrescription.yview)
					# ====================================================Button=============================================================
					btnPrescription = Button(ButtonFrame,command=self.p3,text= " Prescription ", bg="dark olive green",fg ="plum",activebackground="dark olive green",							activeforeground="plum",font=("arial",12,"bold"),width=20,height =1,padx=2,pady=6)
					btnPrescription.grid(row=0, column=0)
		
					btnPrescriptionData = Button(ButtonFrame,command=self.p1, text= " Prescription Data ",bg="dark olive green",fg="plum",activebackground="dark olive green",						activeforeground="plum",font=("arial",12,"bold"),width=21,height =1,padx=2,pady=6)
					btnPrescriptionData.grid(row=0, column=1)		

					btnUpdate = Button(ButtonFrame,command = self.p2,text= " Update ", fg ="plum",bg="dark olive green",activebackground="dark olive green",
					activeforeground="plum",font=("arial",12,"bold"),width=20,height =1,padx=2,pady=6)
					btnUpdate.grid(row=0, column=2)		
		
					btnDelete = Button(ButtonFrame,command=self.p4, text= " Delete ", bg="dark olive green",fg="plum",activebackground="dark olive green",
					activeforeground="plum",font=("arial",12,"bold"),width=21,height =1,padx=2,pady=6)
					btnDelete.grid(row=0, column=3)		
		
					btnClear = Button(ButtonFrame,command=self.p5,text= " Clear ", bg="dark olive green",fg ="plum",activebackground="dark olive green",activeforeground="plum",					font=("arial",12,"bold"),width=20,height =1,padx=2,pady=6)
					btnClear.grid(row=0, column=4)
					
					btnBack = Button(ButtonFrame,command=self.p6, text= " Backup ", bg="dark olive green",fg ="plum",activebackground="dark olive green",activeforeground="plum",								font=("arial",12,"bold"),width=20,height =1,padx=2,pady=6)
					btnBack.grid(row=0, column=5)			
		
					btnExit = Button(ButtonFrame,command=self.p7, text= " Exit ", bg="dark olive green",fg ="plum",activebackground="dark olive green",activeforeground="plum",						font=("arial",12,"bold"),width=20,height =1,padx=2,pady=6)
					btnExit.grid(row=0, column=6)		
					# ====================================================Table==============================================================
					# ====================================================Scrollbar==========================================================
					
					scroll_x =ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
					scroll_y =ttk.Scrollbar(DetailsFrame,orient=VERTICAL)
					self.hospital_table=ttk.Treeview(DetailsFrame,column=("nameoftablet","ref","dose","nooftablets","lot","issue date","expire date","dailydose",									"side effect","further information","blood pressure","storage","medication","patientid","nhsnumber","pname","dob","address"))
					scroll_x.pack(side=BOTTOM,fill=X)
					scroll_y.pack(side=RIGHT,fill=Y)
					self.hospital_table.configure(xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
					scroll_x.config(command=self.hospital_table.xview)
					scroll_y.config(command=self.hospital_table.yview)
				
					s= ttk.Style()
					s.theme_use("clam")
					s.configure("Treeview.heading", background="DarkOliveGreen", foregroud="DarkOliveGreen")


					self.hospital_table.heading("nameoftablet", text = "Name Of Tablet")
					self.hospital_table.heading("ref", text = "Reference No.")
					self.hospital_table.heading("dose", text = "Dose")
					self.hospital_table.heading("nooftablets", text = "No Of Tablets")
					self.hospital_table.heading("lot", text = "Lot")
					self.hospital_table.heading("issue date", text = "Issue Date")
					self.hospital_table.heading("expire date", text = "Expire Date")
					self.hospital_table.heading("dailydose", text = "DailyDose")
					self.hospital_table.heading("side effect", text ="SideEffect")
					self.hospital_table.heading("further information", text = "FurtherInformation")
					self.hospital_table.heading("blood pressure", text = "BloodPressure")
					self.hospital_table.heading("storage", text = "Storage")
					self.hospital_table.heading("medication", text = "Medication")
					self.hospital_table.heading("patientid", text = "PatientId")
					self.hospital_table.heading("nhsnumber", text = "NHS Number")
					self.hospital_table.heading("pname", text = "Patient Name")
					self.hospital_table.heading("dob", text = "DOB")
					self.hospital_table.heading("address", text = "Address")

					self.hospital_table["show"]="headings"
			
					
					self.hospital_table.column("nameoftablet", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("ref", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("dose", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("nooftablets", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("lot", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("issue date", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("expire date", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("dailydose", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("side effect", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("further information", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("blood pressure", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("storage", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("medication", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("patientid", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("nhsnumber", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("pname", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("dob", width=85,minwidth=150,stretch=False)
					self.hospital_table.column("address", width=85,minwidth=150,stretch=False)

					self.hospital_table.pack(fill=BOTH,side=LEFT, expand=1)
					self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
					self.fatch_data()

				# =================================================Functionality Declaration=====================================
				
					
						
				def p1(self):
					try:
						if self.NameOfTablets.get()=="" or self.Ref.get()=="" or self.PatientName.get()=="" or self.Dose.get()=="" or self.NumberOfTablets.get()=="" or 							self.DailyDose.get()==""or self.Lot.get()=="" or self.SideEffect.get()=="" or self.FurtherInformation.get=="" or self.StorageAdvice.get()=="" or 							self.IssueDate.get()=="" or self.ExpDate.get()=="" or self.HowToUseMedication.get()=="" or self.DrivingUsingMachine.get()=="" or 										self.PatientId.get()=="" or self.NHSNumber.get()=="" or self.NumberOfTablets.get()=="" or self.DateOfBirth.get()=="" or self.PatientAddress.get()=="":
							messagebox.showerror("Error", "All Fields are Required!")
						elif len(self.NameOfTablets.get())<=2 or len(self.PatientName.get())<=2:
							messagebox.showerror("Error", "Minimum Two Charcter are required!") 
						
						elif re.search(r'[^A-Za-z0-9\s]',self.Ref.get()) or self.Ref.get().isalpha():
							messagebox.showerror("Error", "Reference must be positive number only !")		
						elif self.NameOfTablets.get().isalpha()==False or self.PatientName.get().isalpha()==False:
							messagebox.showerror("Error", "Name should Required letter only!")
						elif self.StorageAdvice.get().isalpha()==False:
							messagebox.showerror("Error", "StorageAdivce should Required letter only!")
						elif int(self.Dose.get()) < 0:
							messagebox.showerror("Error","Dose should be positive only!") 
						elif int(self.DailyDose.get()) < 0:
							messagebox.showerror("Error","DailyDose should be positive only!") 
						elif int(self.Lot.get()) < 0:
							messagebox.showerror("Error","Lot should be positive only!")
						elif re.search(r'[^A-Za-z0-9\s]',self.PatientId.get()) or self.PatientId.get().isalpha():
							messagebox.showerror("Error", "PatientId must be positive number only!") 
						elif re.search(r'[^A-Za-z0-9\s]',self.SideEffect.get()): 
							messagebox.showerror("Error", "Side effect does not contain special character!")
						elif int(self.DrivingUsingMachine.get()) < 0:
							messagebox.showerror("Error","Blood Pressure should be positive only!") 
						elif int(self.NumberOfTablets.get()) < 0:
							messagebox.showerror("Error","Number of Tablets should be positive only!") 
						
						elif re.search(r'[^A-Za-z0-9\s]',self.NHSNumber.get()) or self.NHSNumber.get().isalpha():
							messagebox.showerror("Error", "NHSNumber must be positive number only !") 
						 
						elif  int(self.DrivingUsingMachine.get()) <= 20:
							messagebox.showerror("Error","Human Blood Pressure Should not be less than 20!")
						elif self.ExpDate.get() <= self.IssueDate.get():
							messagebox.showerror("Error","Expiry date must be greater than the issue date!")
						
						else:
							conn=mysql.connector.connect(host="localhost",username="root",password="kunaljain2104@",database="Mydata")
							my_cursor=conn.cursor()
							my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.NameOfTablets.get(),self.Ref.get(),							self.Dose.get(),self.NumberOfTablets.get(),self.Lot.get(),self.IssueDate.get(),self.ExpDate.get(),self.DailyDose.get(),self.SideEffect.get(),
							self.FurtherInformation.get(),self.DrivingUsingMachine.get(),self.StorageAdvice.get(),self.HowToUseMedication.get(),self.PatientId.get(),									self.NHSNumber.get(),self.PatientName.get(),self.DateOfBirth.get(),self.PatientAddress.get()))															
							conn.commit()
							self.fatch_data()
							conn.close()
							messagebox.showinfo("Success", "Record has been Inserted")
					except mysql.connector.IntegrityError:
						messagebox.showerror("Error", "Reference already exists")
						conn.rollback()
					

				def p2(self):
					try:
						if self.NameOfTablets.get()=="" or self.Ref.get()=="" or self.PatientName.get()=="" or self.Dose.get()=="" or self.NumberOfTablets.get()=="" or 							self.DailyDose.get()==""or self.Lot.get()=="" or self.SideEffect.get()=="" or self.FurtherInformation.get=="" or self.StorageAdvice.get()=="" or 							self.IssueDate.get()=="" or self.ExpDate.get()=="" or self.HowToUseMedication.get()=="" or self.DrivingUsingMachine.get()=="" or 										self.PatientId.get()=="" or self.NHSNumber.get()=="" or self.NumberOfTablets.get()=="" or self.DateOfBirth.get()=="" or self.PatientAddress.get()=="":
							messagebox.showerror("Error", "All Fields are Required!")
						elif len(self.NameOfTablets.get())<=2 or len(self.PatientName.get())<=2:
							messagebox.showerror("Error", "Minimum Two Charcter are required!")	 
						
						elif re.search(r'[^A-Za-z0-9\s]',self.Ref.get()) or self.Ref.get().isalpha():
							messagebox.showerror("Error", "Reference must be positive number only !")		
						elif self.NameOfTablets.get().isalpha()==False or self.PatientName.get().isalpha()==False:
							messagebox.showerror("Error", "Name should Required letter only!")
						elif self.StorageAdvice.get().isalpha()==False:
							messagebox.showerror("Error", "StorageAdivce should Required letter only!")
						elif int(self.Dose.get()) < 0:
							messagebox.showerror("Error","Dose should be positive only!") 
						elif int(self.DailyDose.get()) < 0:
							messagebox.showerror("Error","DailyDose should be positive only!") 
						elif int(self.Lot.get()) < 0:
							messagebox.showerror("Error","Lot should be positive only!")
						elif re.search(r'[^A-Za-z0-9\s]',self.PatientId.get()) or self.PatientId.get().isalpha():
							messagebox.showerror("Error", "PatientId must be positive number only!") 
						elif re.search(r'[^A-Za-z0-9\s]',self.SideEffect.get()): 
							messagebox.showerror("Error", "Side effect does not contain special character!")
						elif int(self.DrivingUsingMachine.get()) < 0:
							messagebox.showerror("Error","Blood Pressure should be positive only!") 
						elif int(self.NumberOfTablets.get()) < 0:
							messagebox.showerror("Error","Number of Tablets should be positive only!") 
						elif re.search(r'[^A-Za-z0-9\s]',self.NHSNumber.get()) or self.NHSNumber.get().isalpha():
							messagebox.showerror("Error", "NHSNumber must be positive number only !") 
						 
						elif  int(self.DrivingUsingMachine.get()) <= 20:
							messagebox.showerror("Error","Human Blood Pressure Should not be less than 20!")
						elif self.ExpDate.get() <= self.IssueDate.get():
							messagebox.showerror("Error","Expiry date must be greater than the issue date!")
						else:
							conn=mysql.connector.connect(host="localhost",username="root",password="kunaljain2104@",database='Mydata')
							my_cursor=conn.cursor()
							my_cursor.execute("update hospital set NameOfTablets=%s,Dose=%s,NumberOfTablets=%s,Lot=%s,IssueDate=%s,ExpireDate=%s,DailyDose=%s,SideEffect=%s,							FurtherInformation=%s,BloodPressure=%s,Storage=%s,Medication=%s,PatientId=%s,NHSNumber=%s,PatientName=%s,DOB=%s,PatientAddress=%s where 									Reference_No = %s ",(self.NameOfTablets.get(),self.Dose.get(),self.NumberOfTablets.get(),self.Lot.get(),self.IssueDate.get(),self.ExpDate.get(),							self.DailyDose.get(),self.SideEffect.get(),self.FurtherInformation.get(),self.DrivingUsingMachine.get(),self.StorageAdvice.get(),										self.HowToUseMedication.get(),self.PatientId.get(),self.NHSNumber.get(),self.PatientName.get(),self.DateOfBirth.get(),self.PatientAddress.get(),							self.Ref.get()))
										
							conn.commit()
							self.fatch_data()
							conn.close()
							messagebox.showinfo("Update", "Record has been updated successfully")
					except mysql.connector.IntegrityError:
						messagebox.showerror("Error", "Reference already exists")
						conn.rollback()
						




				def fatch_data(self):
					conn=mysql.connector.connect(host="localhost",username="root",password="kunaljain2104@",database="Mydata")
					my_cursor=conn.cursor()
					my_cursor.execute("select * from hospital")
					rows=my_cursor.fetchall()
					if len(rows)!=0:
						self.hospital_table.delete(*self.hospital_table.get_children())
						for i in rows:
							self.hospital_table.insert("", END,values=i)
						conn.commit()
					conn.close()			
	
				def get_cursor(self,event=""):
					cursor_row=self.hospital_table.focus()
					content=self.hospital_table.item(cursor_row)
					row=content["values"]
					
					self.NameOfTablets.set(row[0])
					self.Ref.set(row[1])
					self.Dose.set(row[2])
					self.NumberOfTablets.set(row[3])
					self.Lot.set(row[4])
					self.IssueDate.set(row[5])
					self.ExpDate.set(row[6])
					self.DailyDose.set(row[7])
					self.SideEffect.set(row[8])
					self.FurtherInformation.set(row[9])
					self.DrivingUsingMachine.set(row[10])
					self.StorageAdvice.set(row[11])
					self.HowToUseMedication.set(row[12])
					self.PatientId.set(row[13])
					self.NHSNumber.set(row[14])
					self.PatientName.set(row[15])
					self.DateOfBirth.set(row[16])
					self.PatientAddress.set(row[17])		

				def p3(self):
					if self.NameOfTablets.get()=="" or self.Ref.get()=="" or self.PatientName.get()=="" or self.Dose.get()=="" or self.NumberOfTablets.get()=="" or 							self.DailyDose.get()==""or self.Lot.get()=="" or self.SideEffect.get()=="" or self.FurtherInformation.get=="" or self.StorageAdvice.get()=="" or 							self.IssueDate.get()=="" or self.ExpDate.get()=="" or self.HowToUseMedication.get()=="" or self.DrivingUsingMachine.get()=="" or 										self.PatientId.get()=="" or self.NHSNumber.get()=="" or self.NumberOfTablets.get()=="" or self.DateOfBirth.get()=="" or self.PatientAddress.get()=="":
						messagebox.showerror("Error", "All Fields are Required")
					else:
						self.txtPrescription.insert(END,"Name Of Tablets:\t\t\t" + self.NameOfTablets.get()+"\n")	
						self.txtPrescription.insert(END,"Reference_No:\t\t\t" + self.Ref.get()+"\n")	
						self.txtPrescription.insert(END,"Dose:\t\t\t" + self.Dose.get()+"\n")	
						self.txtPrescription.insert(END,"Number Of Tablets:\t\t\t" + self.NumberOfTablets.get()+"\n")	
						self.txtPrescription.insert(END,"Lot:\t\t\t" + self.Lot.get()+"\n")	
						self.txtPrescription.insert(END,"Issue Date:\t\t\t" + self.IssueDate.get()+"\n")	
						self.txtPrescription.insert(END,"Exp Date:\t\t\t" + self.ExpDate.get()+"\n")	
						self.txtPrescription.insert(END,"Daily Dose:\t\t\t" + self.DailyDose.get()+"\n")	
						self.txtPrescription.insert(END,"SideEffect:\t\t\t" + self.SideEffect.get()+"\n")	
						self.txtPrescription.insert(END,"Further Information:\t\t\t" + self.FurtherInformation.get()+"\n")
						self.txtPrescription.insert(END,"Blood Pressure:\t\t\t" + self.DrivingUsingMachine.get()+"\n")	
						self.txtPrescription.insert(END,"StorageAdvice:\t\t\t" + self.StorageAdvice.get()+"\n")	
						self.txtPrescription.insert(END,"Medication:\t\t\t" + self.HowToUseMedication.get()+"\n")		
						self.txtPrescription.insert(END,"PatientId:\t\t\t" + self.PatientId.get()+"\n")	
						self.txtPrescription.insert(END,"NHSNumber:\t\t\t" + self.NHSNumber.get()+"\n")	
						self.txtPrescription.insert(END,"PatientName:\t\t\t" + self.PatientName.get()+"\n")	
						self.txtPrescription.insert(END,"DateOfBirth:\t\t\t" + self.DateOfBirth.get()+"\n")	
						self.txtPrescription.insert(END,"PatientAddress:\t\t\t" + self.PatientAddress.get()+"\n")	


				def p4(self):	
					if self.NameOfTablets.get()=="" or self.Ref.get()=="" or self.PatientName.get()=="" or self.Dose.get()=="" or self.NumberOfTablets.get()=="" or 							self.DailyDose.get()==""or self.Lot.get()=="" or self.SideEffect.get()=="" or self.FurtherInformation.get=="" or self.StorageAdvice.get()=="" or 							self.IssueDate.get()=="" or self.ExpDate.get()=="" or self.HowToUseMedication.get()=="" or self.DrivingUsingMachine.get()=="" or self.PatientId.get()=="" or 					self.NHSNumber.get()=="" or self.NumberOfTablets.get()=="" or self.DateOfBirth.get()=="" or self.PatientAddress.get()=="":
						messagebox.showerror("Error", "All Fields are Required")
					
					else:
						conn=mysql.connector.connect(host="localhost",username="root",password="kunaljain2104@",database='Mydata')
						my_cursor=conn.cursor()
						query="delete from hospital where Reference_No=%s"
						value=(self.Ref.get(),)
						my_cursor.execute(query,value)

						conn.commit()
						conn.close()
						self.fatch_data()
						messagebox.showinfo("Delete", "Patient has been deleted successfully")
						self.NameOfTablets.set("")
						self.Ref.set("")
						self.Dose.set("")
						self.NumberOfTablets.set("")
						self.Lot.set("")
						self.IssueDate.set("")
						self.ExpDate.set("")
						self.DailyDose.set("")
						self.SideEffect.set("")
						self.FurtherInformation.set("")
						self.StorageAdvice.set("")
						self.DrivingUsingMachine.set("")
						self.HowToUseMedication.set("")
						self.PatientId.set("")
						self.NHSNumber.set("")
						self.PatientName.set("")
						self.DateOfBirth.set("")
						self.PatientAddress.set("")
						self.txtPrescription.delete("1.0",END)


				def p5(self):
					self.NameOfTablets.set("")
					self.Ref.set("")
					self.Dose.set("")
					self.NumberOfTablets.set("")
					self.Lot.set("")
					self.IssueDate.set("")
					self.ExpDate.set("")
					self.DailyDose.set("")
					self.SideEffect.set("")
					self.FurtherInformation.set("")
					self.StorageAdvice.set("")
					self.DrivingUsingMachine.set("")
					self.HowToUseMedication.set("")
					self.PatientId.set("")
					self.NHSNumber.set("")
					self.PatientName.set("")
					self.DateOfBirth.set("")
					self.PatientAddress.set("")
					self.txtPrescription.delete("1.0",END)

				def p6(self):
					backup_path = 'C:/mysql/Project/'				
					conn=mysql.connector.connect(host="localhost",user="root",password="kunaljain2104@",database="Mydata")
					my_cursor=conn.cursor()				
					my_cursor.execute("SELECT * FROM hospital")		
					
					column_names = [desc[0] for desc in my_cursor.description]
					filename = f"hospital_data_backup_{date.today()}.xlsx"
					file_path = backup_path + filename
					workbook = xlsxwriter.Workbook(file_path)
					worksheet = workbook.add_worksheet()
					cell_width = 15
					for col_num in range(len(column_names)):
						worksheet.set_column(col_num,col_num,cell_width)

					for col_num, col_name in enumerate(column_names):
						worksheet.write(0, col_num, col_name)
					row_num = 1
					for row in my_cursor:
						for col_num, col_value in enumerate(row):
							worksheet.write(row_num, col_num, col_value)		
						row_num += 1
					workbook.close()
					my_cursor.close()
					conn.close()
					
					messagebox.showinfo('success','Backup Successful completed')
					

				def p7(self):
					p7=messagebox.askyesno("Hospital Management System", "Confirm you want to exit")
					if p7>0:
						root.destroy()
						return
			
			root=Toplevel(window)
			root.transient(window)
			ob= Hospital(root)
			root.mainloop()
			
####################----------------------------------------------------------------------------------------
def signup_page():
	window.destroy()
	import signup
	
#####################---------------------------------------------------------------------------------------
def hide():
	openeye.config(file="close.png")
	code.config(show="*")
	eyeButton.config(command=show)
def show():
	openeye.config(file="open.png")
	code.config(show="")
	eyeButton.config(command=hide)


##################--------------------------------------------------------------------------------------------

frame=Frame(window,width=1400,height=600,bg="white")
frame.place(x=50, y=151)

img = PhotoImage(file="medical.png")
Label(frame,image=img,bg="white").place(x=500,y=-1.5)

heading = Label(frame,text="Sign in", fg='black', bg='white',font=('Microsoft YaHei UI Light',30,"bold"))
heading.place(x=170,y=20)
#############--------------------------------------------------------------------------------------------------
def user_enter(event):
	if username.get()=='Username':
		username.delete(0,END)

username = Entry(frame, width=30, fg="black", border=0,bg="white",font=('Microsoft YaHei UI Light',16,"bold"))
username.place(x=50,y=100)
username.insert(0,'Username')
username.bind('<FocusIn>', user_enter)
Frame(frame,width=400,height=2,bg='black').place(x=45,y=130)

##############--------------------------------------------------------------------------------------------------
def password_enter(event):
	if code.get()=='Password':
		code.delete(0,END)

		
code = Entry(frame, width=30, fg="black", border=0,bg="white",font=('Microsoft YaHei UI Light',16,"bold"))
code.place(x=50,y=200)
code.insert(0,'Password')
code.bind('<FocusIn>',password_enter)

Frame(frame,width=400,height=2,bg='black').place(x=45,y=230)
openeye = PhotoImage(file='open.png')
eyeButton=Button(frame,image=openeye,border=0,bg="white",activebackground="white",cursor="hand2",command=hide)
eyeButton.place(x=410,y=196)

############----------------------------------------------------------------------------------------------------
forgetButton=Button(frame,text="Forgot Password?",border=0,bg="white",activebackground="white",cursor="hand2",font=('Microsoft YaHei UI Light',9,"bold"),command=forgot_pass)
forgetButton.place(x=330,y=240)

Button(frame,width=35,height=3,pady=15, text="Sign in", bg="#57a1f8", fg="white", bd=0,font=('Microsoft YaHei UI Light',12,"bold"),cursor="hand2",activebackground="#57a1f8",	activeforeground="white",command=login_user).place(x=67,y=300)
label=Label(frame,text="Don't have an account?", fg='black', bg='white',font=('Microsoft YaHei UI Light',12))
label.place(x=125,y=420)


sign_up=Button(frame,width=6, text="Sign up",bd=0,fg="royal blue",bg="white",cursor="hand2",activebackground="white",activeforeground="#57a1f8",font=("Microsoft YaHei UI Light",12,"underline"),command=signup_page)
sign_up.place(x=310,y=415)





window.mainloop()