from tkinter import *
from PIL import ImageTk
class Login_System:
	def __init__(self, root):
		self.root=root
		self.root.title('Login System')
		self.root.geometry('1350x700+0+0')

		#User Icon
		self.userIcon=PhotoImage(file='#')
		self.passIcon=PhotoImage(file='#')
		self.logoIcon=PhotoImage(file='#')

		title=Label(self.root, text='Login', font=('cambria', 40))
		title.place(x=0, y=0, relwidth=1)		

		Login_Frame=Frame(self.root, bg='white')
		Login_Frame.place(x=400, y=150)
		logolbl=Label(Login_Frame, image=self.logoIcon)
		logolbl.grid(row=0, column=0, pady=20)

root=Tk()
obj=Login_System(root)
root.mainloop()