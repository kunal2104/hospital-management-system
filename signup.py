from tkinter import * 
from tkinter import messagebox
import pymysql

signup_window=Tk()
signup_window.title("Signup")
signup_window.resizable(False,False)
signup_window.geometry("1540x800+0+0")
signup_window.iconbitmap("signup.ico")
signup_window.configure(bg="dark olive green")

def clear():
	emailEntry.delete(0,END)
	userEntry.delete(0,END)
	passEntry.delete(0,END)
	confirmpassEntry.delete(0,END)
	check.set(0)

def connect_database():
	if emailEntry.get()=="" or userEntry.get()=="" or passEntry.get()=="" or confirmpassEntry.get()=="":
		messagebox.showerror("Error", "All Fields Are Required")
	elif len(userEntry.get())<2:
		messagebox.showerror("Error","Username should be alteast Minimum have two alphabets")
	elif passEntry.get() != confirmpassEntry.get():
		messagebox.showerror("Error","Password Mismatch")
	elif check.get()==0:
		messagebox.showerror("Error","Please Accept Terms & Conditions")
	else:
		try:
			con=pymysql.connect(host='localhost',user="root",password="kunaljain2104@")
			my_cursor=con.cursor()
		except:
			messagebox.showerror("Error","Database Connectivity Issue, Please Try Again")
			return
		try:
			query="create database registeruser"
			my_cursor.execute(query)
			query="use registeruser"
			my_cursor.execute(query)
			query="create table userdata(id int auto_increment primary key not null, email varchar(50),username varchar(100), password varchar(20))"
			my_cursor.execute(query)
			print("after table")
		except:
			my_cursor.execute("use registeruser")

		query="insert into userdata(email,username,password) values(%s,%s,%s)"
		my_cursor.execute(query,(emailEntry.get(),userEntry.get(),passEntry.get()))
		

		try:
			query="create database userdata"
			my_cursor.execute(query)
			query="use userdata"
			my_cursor.execute(query)
			query="create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100), password varchar(20))"
			my_cursor.execute(query)
		except:
			my_cursor.execute("use userdata")

		

		query="select * from data where username=%s"
		my_cursor.execute(query,(userEntry.get()))
		row=my_cursor.fetchone()
		if row !=None:
			messagebox.showerror("Error","Username Already Exists")
			clear()
		else:
			query="insert into data(email,username,password) values(%s,%s,%s)"
			my_cursor.execute(query,(emailEntry.get(),userEntry.get(),passEntry.get()))
			con.commit()
			con.close()
			messagebox.showinfo("Success","Registration is Successful")
			clear()
			signup_window.destroy()
			import main
		
		

def login_page():
	signup_window.destroy()
	import main


lb=Label(signup_window,text = "Hospital Management System",bg="dark olive green",fg="plum",font=('Microsoft YaHei UI Light',40,"bold underline"))
lb.place(x=100,y=40)

frame=Frame(signup_window,width=1300,height=600,bg="white")
frame.place(x=70, y=151)

background = PhotoImage(file="medical.png")
Label(frame,image=background,bg="white").place(x=400,y=-1.5)

heading = Label(frame,text="Sign up", fg='black', bg='white',font=('Microsoft YaHei UI Light',30,"bold"))
heading.place(x=110,y=20)

emailLabel=Label(frame,text="Email",font=('Microsoft YaHei UI Light',12,"bold"),fg="black",bg="white")
emailLabel.place(x=15,y=80)

emailEntry=Entry(frame,width=30,font=('Microsoft YaHei UI Light',12,"bold"),bg="dark olive green",fg="white")
emailEntry.place(x=15,y=110)


userLabel=Label(frame,text="Username",font=('Microsoft YaHei UI Light',12,"bold"),fg="black",bg="white")
userLabel.place(x=15,y=150)

userEntry=Entry(frame,width=30,font=('Microsoft YaHei UI Light',12,"bold"),bg="dark olive green",fg="white")
userEntry.place(x=15,y=180)

passLabel=Label(frame,text="Password",font=('Microsoft YaHei UI Light',12,"bold"),fg="black",bg="white")
passLabel.place(x=15,y=220)

passEntry=Entry(frame,width=30,font=('Microsoft YaHei UI Light',12,"bold"),bg="dark olive green",fg="white")
passEntry.place(x=15,y=250)

confirmpassLabel=Label(frame,text="confirm Password",font=('Microsoft YaHei UI Light',12,"bold"),fg="black",bg="white")
confirmpassLabel.place(x=15,y=290)

confirmpassEntry=Entry(frame,width=30,font=('Microsoft YaHei UI Light',12,"bold"),bg="dark olive green",fg="white")
confirmpassEntry.place(x=15,y=320)

check=IntVar()
T=Checkbutton(frame,text="I agree to the Terms & Conditions",font=('Microsoft YaHei UI Light',11,"bold"),bg="white",fg="black",padx=10,pady=10,activebackground="white",cursor="hand2",variable=check)
T.place(x=5,y=350)

signupButton=Button(frame,text="Signup",font=('Open Sans',12,"bold"),width=30,height=4,fg="white",bg="dark olive green",bd=0,cursor="hand2",activebackground="dark olive green",activeforeground="white",command=connect_database)
signupButton.place(x=15,y=400)

lb1=Label(frame, text="I have an Account?",font=('Microsoft YaHei UI Light',10,"bold"),fg="black",bg="white")
lb1.place(x=15,y=510)

loginButton=Button(frame,text="Login",font=('Microsoft YaHei UI Light',10,"underline"),fg="royal blue",bg="white",bd=0,cursor="hand2",activebackground="white", activeforeground="royal blue",command=login_page)
loginButton.place(x=160,y=507)







signup_window.mainloop()