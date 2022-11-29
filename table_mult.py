from tkinter import *

fontLabel = 'Helvetica 25 bold'

class Multiplication:
	"""docstring for Multiplication"""
	def __init__(self, root):
		self.root = root
		self.root.title("Table de Multiplication")
		self.root.geometry("800x680+100+100")
		self.root.config(bg="lightgrey")

		#variables
		self.var_nbr = IntVar()

		#widgets
		label1 = Label(self.root,text="Donnez un nombre",fg="black").place(x=20,y=1,width=200,height=50)
		entry1 = Entry(self.root,bd=2,relief=RIDGE,textvariable=self.var_nbr).place(x=20,y=50,width=200,height=30)
		btn1 = Button(self.root,text="Afficher",command=self.multi,bd=3,relief=GROOVE).place(x=20,y=80,width=100,height=30)

	# fonction pour afficher la table de multiplication
	def multi(self):
		self.nbr = self.var_nbr.get()
		i = 1
		self.liste = []
		while i <= 10:
			self.liste.append(str(self.nbr)+" * "+str(i)+" = "+str(self.nbr*i)+"\n") 
			i+=1
		print(self.liste[0])
		for i in range(len(self.liste)):
			if(self.liste[i] != "{" or self.liste[i] != "}"):
				label2 = Label(self.root,text=self.liste,bd=6,relief=GROOVE,font=fontLabel,fg="black",bg="white").place(x=20,y=120,width=350,height=400)
		

root = Tk()
obj = Multiplication(root)
root.mainloop()
