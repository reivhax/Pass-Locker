from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from program import Program
from base64 import b64encode
from os import urandom
root = Tk()
passwlocker=Program()

class WelcomeFrame(Frame):
	def __init__(self, master):
		master.title("Passlocker 1.0")
		Frame.__init__(self, master)
		self.font=("Times New Roman", 28, "bold italic")
		self.screen = Frame()
		self.default()
	def default(self):
		self.screen.destroy()
		self.screen = Frame()
		self.welcome =Label(self.screen,text="Welcome to Passlocker 1.0")
		self.loginbutton = Button(self.screen,text="Login",command=self.login)
		self.userbutton = Button(self.screen,text="Add User",command=self.adduser)
		self.welcome.grid(row=0,column=1,pady=10,padx=50)
		self.loginbutton.grid(row=1,column=1,pady=10,padx=10)
		self.userbutton.grid(row=2,column=1,pady=10,padx=10)
		self.screen.pack(fill=BOTH,expand=1)
	def login(self):
		if len(passwlocker.users)<1:
			message="There are no users registered.Please register first"
			messagebox.showerror("Error",message)
			self.adduser()
			return
		self.screen.destroy()
		self.screen=Frame()
		banner=Label(self.screen,text="Type Your Master pasword below")
		banner['font']=("Times New Roman", 25, "bold italic")
		banner.grid(row=0,column=0,columnspan=2,pady=10)
		Label(self.screen, text="Username: ").grid(row=1,column=0,pady=20)
		Label(self.screen, text="Password: ").grid(row=2,column=0)
		login=Button(self.screen, text="Login",command=self.dologin)
		self.defuser=StringVar()
		users=list(passwlocker.users.keys())
		self.defuser.set(users[0])
		user=OptionMenu(self.screen,self.defuser,users[0],*users)
		self.passentry = Entry(self.screen,show="*",width=18)
		user.grid(row=1,column=1,pady=20)
		self.passentry.grid(row=2,column=1,padx=10)
		login.grid(row=3,column=1,pady=10,padx=10)
		self.screen.pack(fill=BOTH,expand=1)
	def adduser(self):
		self.screen.destroy()
		self.screen=Frame()
		Label(self.screen, text="Username: ").pack()
		adduser=Button(self.screen, text="Add User", command=self.doadduser)
		self.unameentry = Entry(self.screen)
		self.passentry = Entry(self.screen, show="*")
		self.unameentry.pack()
		Label(self.screen, text="Password: ").pack()
		self.passentry.pack()
		adduser.pack()
		self.screen.pack(fill=BOTH,expand=1)
	def toclip(self,cred):
		root.clipboard_clear()
		root.clipboard_append(cred)
	def showpass(self):
		self.screen.destroy()
		self.screen=Frame(width=12)
		style=Style()
		style.configure("spread.TLabel",borderwidth=2, relief="ridge")
		name=Label(self.screen, text="Name",style="spread.TLabel")
		name.grid(row=0,column=0,sticky=W)
		user=Label(self.screen, text="User",style="spread.TLabel")
		user.grid(row=0,column=1,sticky=W)
		passw=Label(self.screen, text="Password",style="spread.TLabel")
		passw.grid(row=0,column=2,sticky=W)
		index=1
		for cred in self.userobject.show():
			name=Label(self.screen, text=cred[0],style="spread.TLabel")
			name.grid(row=index,column=0,sticky=W)
			user=Label(self.screen, text=cred[1],style="spread.TLabel")
			user.grid(row=index,column=1,sticky=W)
			passw=Label(self.screen, text=cred[2],style="spread.TLabel")
			passw.grid(row=index,column=2,sticky=W)
			copy=Button(self.screen, text="copy",command=lambda: self.toclip(cred))
			copy.grid(row=index,column=3,padx=30)
			index+=1
		home=Button(self.screen, text="Home",command=self.successlogin)
		home.grid(row=index,column=0,padx=20,pady=30)
		logout=Button(self.screen, text="Log out",command=self.default)
		logout.grid(row=index,column=1)
		exit=Button(self.screen, text="Exit",command=passwlocker.export)
		exit.grid(row=index,column=2)
		self.screen.pack(fill=BOTH,expand=1)
	def genrand(self,limit=9):
		if type(limit).__name__!='int':
			return
		rnd=b64encode(urandom(320))[:limit]
		self.passentry.delete(0,END)
		self.passentry.insert(0,rnd)
	def addcreds(self):
		self.screen.destroy()
		self.screen=Frame()
		Label(self.screen, text="Name: ").grid(row=0,column=0,pady=15)
		Label(self.screen, text="User: ").grid(row=1,column=0,pady=15)
		Label(self.screen, text="Pass: ").grid(row=2,column=0,pady=15)
		saver=Button(self.screen, text="Save Cred",command=self.savecred)
		gen=Button(self.screen, text="Generate pass",command=self.genrand)
		gen.grid(row=3,column=1)
		saver.grid(row=4,column=1,padx=30,pady=20)
		self.unameentry=Entry(self.screen)
		self.userentry=Entry(self.screen)
		self.passentry=Entry(self.screen,show="*")
		self.unameentry.grid(row=0,column=1)
		self.userentry.grid(row=1,column=1)
		self.passentry.grid(row=2,column=1)
		home=Button(self.screen, text="Home",command=self.successlogin)
		home.grid(row=5,column=0,padx=20,pady=30)
		logout=Button(self.screen, text="Log out",command=self.default)
		logout.grid(row=5,column=1)
		self.screen.pack(fill=BOTH,expand=1)
	def changekey(self):
		self.screen.destroy()
		self.screen=Frame()
		Label(self.screen, text="Current: ").grid(row=0,column=0,padx=25,pady=50)
		Label(self.screen, text="    New: ").grid(row=1,column=0,padx=25)
		adduser=Button(self.screen, text="Change key", command=self.dochange)
		adduser.grid(row=2,column=1,pady=35)
		self.oldentry = Entry(self.screen,width=18)
		self.newentry = Entry(self.screen, show="*",width=18)
		self.oldentry.grid(row=0,column=1,columnspan=1)
		self.newentry.grid(row=1,column=1,columnspan=1)
		home=Button(self.screen, text="Home",command=self.successlogin)
		home.grid(row=3,column=0,padx=20,pady=30)
		logout=Button(self.screen, text="Log out",command=self.default)
		logout.grid(row=3,column=1)
		self.screen.pack(fill=BOTH,expand=1)
	def successlogin(self):
		self.screen.destroy()
		self.screen=Frame()
		welcome=Label(self.screen,text=f"Welcome back {self.userobject.name}")
		welcome["font"]=self.font
		welcome.grid(column=0,row=0,padx=80)
		show=Button(self.screen, text="Show credentials", command=self.showpass)
		show.grid(column=0,row=1,padx=25,pady=10)
		add=Button(self.screen, text="Add credential", command=self.addcreds)
		add.grid(column=0,row=2,padx=25,pady=10)
		change=Button(self.screen, text="Change Master pass", command=self.changekey)
		change.grid(column=0,row=3,padx=25,pady=10)
		logout=Button(self.screen, text="Log out",command=self.default)
		logout.grid(row=4,column=0,pady=40)
		exit=Button(self.screen, text="Exit",command=passwlocker.export)
		exit.grid(row=5,column=0)
		self.screen.pack(fill=BOTH,expand=1)
	#Interactive methods -->
	def dochange(self):
		old=self.oldentry.get()
		new=self.newentry.get()
		name=self.userobject.name
		state=self.userobject.updatemaster(old,new)
		if state:
			self.oldentry.delete(0, END)
			self.newentry.delete(0, END)
			message=f"Master Password for {name} changed"
			messagebox.showinfo("Success",message)
			self.login()
		else:
			message=f"Wrong Password for {name}.You have been logged out!"
			messagebox.showerror("Error",message)
			self.login()
	def dologin(self):
		username=self.defuser.get()
		password=self.passentry.get()
		state=passwlocker.users[username].login(password=password)
		if state:
			self.userobject=passwlocker.users[username]
			self.successlogin()
		else:
			self.passentry.delete(0, END)
			messagebox.showwarning("Error",f"Wrong Password for {username}")
	def savecred(self):
		encname=self.unameentry.get()
		uname=self.userentry.get()
		passw=self.passentry.get()
		state=self.userobject.add_password(encname,uname,passw)
		if state:
			messagebox.showinfo("Success",f"Password {encname} has been recorded")
			self.successlogin()
		else:
			messagebox.showwarning("Error",f"Duplicate entry {encname} found!")
	def doadduser(self):
		username=self.unameentry.get()
		password=self.passentry.get()
		state=passwlocker.adduser(username,password)
		if state:
			messagebox.showinfo("Success",f"Username {username} has been created")
			self.default()
		else:
			self.passentry.delete(0, END)
			self.unameentry.delete(0, END)
			messagebox.showwarning("Error",f"Username {username} already exists")
			self.defa.ult()
root.option_add("*Font", ("Times New Roman", 25, "bold italic"))
root.geometry("500x500")
root.resizable(0, 0)
welcome = WelcomeFrame(root)
root.protocol("WM_DELETE_WINDOW", passwlocker.export)
root.mainloop()