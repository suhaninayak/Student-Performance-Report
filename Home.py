from tkinter import *
from tkinter import messagebox
from pymysql import *
from tkinter import filedialog
import csv
from matplotlib import pyplot as plt
conobj = connect(host='localhost', user='root', password='Suhani@123!', database='MyProject')
curobj=conobj.cursor()
curobj.execute('use MyProject;')
win1=Tk()
#=====================================
def Login():
	#print(Name.get(), Pwd.get())
	r='select * from Admin where UserName="{}" and Password="{}";'.format(Name.get(), Pwd.get())
	curobj.execute(r)
	record=curobj.fetchall()
	#print(record)
	if len(record):
		win1.destroy()
		win2=Tk()
		#========================
		def Report():
			#print(regno.get(), name.get(), Dvar.get(), Gvar.get())

			Rollno1, Name1, eng1, math1, c1, java1, py1=[], [], [], [], [], [], []
			global file_path1
			fobj1= open(file_path1, 'r')
			cobj1=csv.reader (fobj1)
			next(cobj1)
			for data in cobj1:
				Rollno1.append(int(data[0]))
				Name1.append(data[1])
				eng1.append(int(data[2]))
				math1.append(int(data[3]))
				c1.append(int(data[4]))
				java1.append(int(data[5]))
				py1.append(int(data[6]))
			
			if int(regno.get()) in Rollno1:
				index=Rollno1.index(int(regno.get()))
				marklist=[eng1[index], math1[index], c1[index], java1[index], py1[index]]
				plt.subplot(2, 3, 1)
				plt.bar(['Eng', 'Math', 'C', 'Java', 'Python'], marklist)
				plt.title("INTERNAL 1 MARKS")
				plt.xlabel('Subject name')
				plt.ylabel('Marks secured out of 20')
			else:
				print('Regno is invalid')
			#..................................................
			Rollno2, Name2, eng2, math2, c2, java2, py2=[], [], [], [], [], [], []
			global file_path2
			fobj2= open(file_path2, 'r')
			cobj2=csv.reader (fobj2)
			next(cobj2)
			for data in cobj2:
				Rollno2.append(int(data[0]))
				Name2.append(data[1])
				eng2.append(int(data[2]))
				math2.append(int(data[3]))
				c2.append(int(data[4]))
				java2.append(int(data[5]))
				py2.append(int(data[6]))
			
			if int(regno.get()) in Rollno1:
				index=Rollno1.index(int(regno.get()))
				marklist=[eng2[index], math2[index], c2[index], java2[index], py2[index]]
				plt.subplot(2, 3, 2)
				plt.bar(['Eng', 'Math', 'C', 'Java', 'Python'], marklist)
				plt.title("INTERNAL 2 MARKS")
				plt.xlabel('Subject name')
				plt.ylabel('Marks secured out of 20')
				
			else:
				print('Regno is invalid')
				
				
			
			#..................................................
			Rollno3, Name3, jan, feb, mar=[], [], [], [], []
			global file_path3
			fobj3= open(file_path3, 'r')
			cobj3=csv.reader (fobj3)
			next(cobj3)
			for data in cobj3:
				Rollno3.append(int(data[0]))
				Name3.append(data[1])
				jan.append(int(data[2]))
				feb.append(int(data[3]))
				mar.append(int(data[4]))
			'''
			print(Rollno3)
			print(Name3)
			print(jan)
			print(feb)
			print(mar)'''

			if int(regno.get()) in Rollno1:
				index=Rollno1.index(int(regno.get()))
				marklist=[jan[index], feb[index], mar[index]]
				plt.subplot(2, 3, 3)
				plt.pie(marklist, labels=['Jan', 'Feb', 'Mar'], autopct='%1.2f%%')
				plt.title("ATTENDANCE ")
				plt.show()
				
			
		def Reset():
			regno.delete(0, END)
			name.delete(0, END)
			Dvar.set("--Select Department Name--")
			Gvar.set('Select Gender')
		def Exit():
			win2.destroy()
		#===================
		def Internal1():
			global file_path1
			file_path1= filedialog.askopenfilename(defaultextension=".csv", filetypes=[('CSV Files', '*.csv')])
		#..........................................
		def Internal2():
			global file_path2
			file_path2= filedialog.askopenfilename(defaultextension=".csv", filetypes=[('CSV Files', '*.csv')])
		#..........................................
		def Attendance ():
			global file_path3
			file_path3= filedialog.askopenfilename(defaultextension=".csv", filetypes=[('CSV Files', '*.csv')])
		#==================
		win2.minsize(550, 600)
		win2.maxsize(550, 600)
		win2.title('Admin Home Page')
		win2.configure(bg='#bcc6cc')
		#===================
		Label(win2, text="Student's Details", font=('Georgia',18),width=20, bg='#f5fffa', fg='blue', relief='raised').place(x=125,y=30)

		Label(win2,text='Registration no. :',font=('Georgia', 14),width='20', bg='#f5fffa', fg='blue', relief='raised').place(x=30, y=100)
		regno = Entry(win2,font=('Lucida Fax', 14),bg='#8a865d',fg='black', relief='groove')
		regno.place(x=280,y=100)

		Label(win2,text='Name :',font=('Georgia', 14),width='20', bg='#f5fffa', fg='blue', relief='raised').place(x=30, y=150)
		name = Entry(win2,font=('Lucida Fax', 14),bg='#8a865d',fg='black', relief='groove')
		name.place(x=280,y=150)

		Label(win2,text='Department :',font=('Georgia', 14),width='20', bg='#f5fffa', fg='blue', relief='raised').place(x=30, y=200)
		Dvar=StringVar()
		Dvar.set('--Select Department Name--')
		OptionMenu(win2, Dvar, 'CSE', 'ECE', 'EEE', 'CS-IT', 'ME', 'CIVIL').place(x=280,y=200)

		Label(win2,text='Gender :',font=('Georgia', 14),width='20', bg='#f5fffa', fg='blue', relief='raised').place(x=30, y=250)
		#Entry(win2,font=('Lucida Fax', 14),bg='#8a865d',fg='black', relief='groove').place(x=280,y=250)
		Gvar=StringVar()
		Radiobutton(win2, text='Male', variable=Gvar, value='Male').place(x=280,y=250)
		Radiobutton(win2, text='Female', variable=Gvar, value='Female').place(x=350,y=250)

		Label(win2,text='Upload Internal-1 Marks :',font=('Georgia', 14),width='20', bg='#f5fffa', fg='blue', relief='raised').place(x=30, y=300)
		#Entry(win2,font=('Lucida Fax', 14),bg='#8a865d',fg='black', relief='groove').place(x=280,y=300)
		Button(win2, text='Browse Internal-1 File', width=20,font=('Georgia', 11), command=Internal1).place(x=280, y=300)

		Label(win2,text='Upload Internal-2 Marks :',font=('Georgia', 14),width='20', bg='#f5fffa', fg='blue', relief='raised').place(x=30, y=350)
		#Entry(win2,font=('Lucida Fax', 14),bg='#8a865d',fg='black', relief='groove').place(x=280,y=350)
		Button(win2, text='Browse Internal-2 File', width=20,font=('Georgia', 11), command=Internal2).place(x=280, y=350)

		Label(win2,text='Upload Attendance Sheet :',font=('Georgia', 14),width='21', bg='#f5fffa', fg='blue', relief='raised').place(x=30, y=400)
		#Entry(win2,font=('Lucida Fax', 14),bg='#8a865d',fg='black', relief='groove').place(x=280,y=400)
		Button(win2, text='Browse Attendance Sheet', width=20,font=('Georgia', 11), command=Attendance).place(x=280, y=400)

		Button(win2, text='Report', font=('Elephant', 14), width='8', bg='#c04000', fg='white', relief='raised', activebackground='red',command=Report).place(x=100,y=500)
		Button(win2, text='Reset', font=('Elephant', 14), width='8', bg='#c04000', fg='white', relief='raised', activebackground='red',command=Reset).place(x=230,y=500)
		Button(win2, text='Exit', font=('Elephant', 14), width='8', bg='#c04000', fg='white', relief='raised', activebackground='red', command=Exit).place(x=360,y=500)
		#=========================
		win2.mainloop()
	else:
		messagebox.showinfo('close','Invalid Username And Password!!!')
		win1.destroy()
#.........................................
def Exit():
	messagebox.showinfo('close', 'Thank you')
	win1.destroy ()
#===========================================
#win1.geometry('600x500') #width x height, the window can be resized to keep it fix use minsize and maxsize
win1.minsize(550, 400)
win1.maxsize(550, 400)
win1.title('Admin Login Page')
win1.configure(bg='#e2cfea')

Label(win1, text='Admin User Name :', font=('Lucida Fax', 14),width='15', bg='#f5fffa', fg='blue', relief='raised').place(x=30, y=100)
Name=Entry(win1,font=('Lucida Fax', 14),bg='#8a865d',fg='black', relief='sunken')
Name.place(x=280, y=100)

Label(win1, text='Admin Password :', font=('Lucida Fax', 14),width='15', bg='#f5fffa', fg='blue', relief='raised').place(x=30, y=150)
Pwd=Entry(win1,font=('Lucida Fax', 14),bg='#8a865d',fg='black', relief='sunken')
Pwd.place(x=280, y=150)

Button(win1, text='Login', font=('Elephant', 14), width='8', bg='#c04000', fg='white', relief='raised', activebackground='red', command=Login).place(x=100, y=250)
Button(win1, text='Exit', font=('Elephant', 14), width='8', bg='#c04000', fg='white', relief='raised', activebackground='red', command=Exit).place(x=300, y=250)

win1.mainloop()
