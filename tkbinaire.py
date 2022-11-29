from tkinter import *

class Binaire:
	"""docstring for Binaire"""
	def __init__(self, root):
		self.root = root
		self.root.title("Convertisseur de nombre")
		self.root.geometry("450x400")
		self.root.config(bg="lightgrey")

		#variables
		self.var_nbr = IntVar()

		#widgets
		label1 = Label(self.root,text="Donnez un nombre en decimal ou en binaire",fg="black").place(x=20,y=1,width=400,height=50)
		label3 = Label(self.root,text="Résultat",fg="white",bg="black").place(x=20,y=200,width=400,height=40)
		entry1 = Entry(self.root,bd=2,relief=RIDGE,textvariable=self.var_nbr).place(x=20,y=50,width=200,height=30)
		btn1 = Button(self.root,text="Decimal => Binaire",command=self.binaire,bd=6,relief=GROOVE).place(x=20,y=80,width=200,height=40)
		btn2 = Button(self.root,text="Binaire => Decimal",command=self.decimal,bd=6,relief=GROOVE).place(x=20,y=120,width=200,height=40)
		btn3 = Button(self.root,text="Decimal => Hexadecimal",command=self.hexadecimal,bd=6,relief=GROOVE).place(x=20,y=160,width=200,height=40)

	# fonction permettant d'afficher un nombre décimal en binaire
	def binaire(self):
		self.nbr = self.var_nbr.get()
		self.liste = []	# liste vide pour stocker les nombres binaires 0 et 1
		self.liste1 = [] # liste vide pour l'affichage
		while (self.nbr>0):	
			if ((self.nbr%2) == 0):
				self.liste.append(0)
			else:
				self.liste.append(1)
			self.nbr=self.nbr/2
			self.nbr=int(self.nbr)	# si le n devient un réel après la division on le reconvertit en entier
		self.j=len(self.liste)-1	# la taille de la liste
		while (self.j>=0):
			self.liste1.append(self.liste[self.j])
			self.j -= 1
		label2 = Label(self.root,text=self.liste1,bd=10,relief=RIDGE,fg="black",bg="white").place(x=20,y=240,width=400,height=60)
	# fonction puissance
	def puissance(self,nbr1,nbr2):
		i=1
		p=1
		while(i <= nbr2):
			p *= 2
			i += 1
		return p

	# fonction permettant d'afficher un nombre binaire en décimal
	def decimal(self):
		self.nbr = str(self.var_nbr.get())
		i=0
		j=len(self.nbr)-1
		k=0
		self.liste = []	# liste vide pour stocker les caractères du chaine à convertir
		while(i < len(self.nbr)):
			self.liste.append(self.nbr[i])	# mettre les caractères dans une liste
			i += 1
		self.som = 0
		self.puiss = 1
		while(j >= 0):
			self.n = int(self.liste[k])	# permet de convertir en entier caractère par caractère
			self.som +=  self.n*self.puissance(2,j)
			j -= 1
			k += 1
		label2 = Label(self.root,text=self.som,bd=10,relief=RIDGE,fg="black",bg="white").place(x=20,y=240,width=400,height=60)
	# fonction permettant d'afficher un nombre décimal en héxadecimal
	def hexadecimal(self):
		self.nbr = self.var_nbr.get()
		self.hexa1,self.hexa2 = [],[] # deux listes vides pour mettre les hexadecimaux
		while(self.nbr > 0):
			if((self.nbr%16) != 0):
				if((self.nbr%16) == 10):
					self.hexa1.append('A')
				elif((self.nbr%16) == 11):
					self.hexa1.append('B')
				elif((self.nbr%16) == 12):
					self.hexa1.append('C')
				elif((self.nbr%16) == 13):
					self.hexa1.append('D')
				elif((self.nbr%16) == 14):
					self.hexa1.append('E')
				elif((self.nbr%16) == 15):
					self.hexa1.append('F')
				elif((self.nbr%16) == 0):
					self.hexa1.append('0')
				elif((self.nbr%16) == 1):
					self.hexa1.append('1')
				elif((self.nbr%16) == 2):
					self.hexa1.append('2')
				elif((self.nbr%16) == 3):
					self.hexa1.append('3')
				elif((self.nbr%16) == 4):
					self.hexa1.append('4')
				elif((self.nbr%16) == 5):
					self.hexa1.append('5')
				elif((self.nbr%16) == 6):
					self.hexa1.append('6')
				elif((self.nbr%16) == 7):
					self.hexa1.append('7')
				elif((self.nbr%16) == 8):
					self.hexa1.append('8')
				elif((self.nbr%16) == 9):
					self.hexa1.append('9')
			self.nbr = self.nbr/16
			self.nbr=int(self.nbr)	# si le n devient un réel après la division on le reconvertit en entier
		j=len(self.hexa1)-1
		while(j >= 0):
			self.hexa2.append(self.hexa1[j])
			j -= 1
		label2 = Label(self.root,text=self.hexa2,bd=10,relief=RIDGE,fg="black",bg="white").place(x=20,y=240,width=400,height=60)
	# permet de convertir un nombre binaire en hexadecimal
	def bin_hexa(self):
		self.nbr = str(self.var_nbr.get())
		i=0
				



#permet d'afficher la fenetre principale
root = Tk()
obj = Binaire(root)
root.mainloop()
