# -*- coding: utf-8 -*-
import mysql.connector as mysql
from Tkinter import *
import ttk

data = {"host": "localhost", "user":"root","database":"escuela"}

def init():
	pswroot = Tk()
	pswroot.title('Autenticación')
	lpass = Label(pswroot,text= u'Contraseña')
	lpass.pack()
	entry = Entry(pswroot,width  = 25, show ="*")
	def getpsw(e):
		psw = entry.get()
		data['password'] = psw
		pswroot.destroy()
	entry.bind("<Return>",getpsw)
	entry.pack()
	pswroot.mainloop()
	return 1

def ventanaPrincipal():
	root = Tk()
	root.title('Base de Datos Escolares')
	root.mainloop()

if __name__ == '__main__':
	if(not init()): exit() #si no inicializa bien, salir
	ventanaPrincipal()
	
	try:
		db = mysql.connect(**data)
		cr = db.cursor()
		query = 'select * from Alumnos'
		cr.execute(query)
		for row in cr: 
			for n in row:
				print str(n) +" ",
			print ""
	except ValueError:
		print 'err'