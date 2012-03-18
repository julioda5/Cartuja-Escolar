# -*- coding: utf-8 -*-
import mysql.connector as mysql
from Tkinter import *
import ttk

data = {"host": "localhost", "user":"root","database":"escuela"}
tables = []

def init():
	root = Tk()
	root.title('Autenticación')
	root.resizable(0,0)
	content = ttk.Frame(root)
	namelbl = ttk.Label(content, text="Contraseña")
	entry = ttk.Entry(content,show="*",width=15)

	content.grid(column=0, row=0)
	namelbl.grid(column=0, row=1, columnspan=2,padx=10,pady=10)
	entry.grid(column=3, row=1, columnspan=3,padx=10,pady=10)
	
	def getpsw(e):
		global val
		psw = entry.get()
		if(psw):
			data['password'] = psw
			root.destroy()
	entry.bind("<Return>",getpsw)
	
	root.mainloop()
	return 'password' in data

def ventanaPrincipal():
	root = Tk()
	root.title('Base de Datos Escolares')
	root.resizable(0,0)
	cntVP = ttk.Frame(root)
	altasLb = ttk.Label(cntVP, text="Opciones:")
	def alto():
		darAltas(root)
	btnAlt = ttk.Button(cntVP, text = 'Altas',command = alto,width = 10)
	btnBjs = ttk.Button(cntVP, text = 'Bajas',command = alto,width = 10)
	btnRep = ttk.Button(cntVP, text = 'Reportes',command = alto,width = 10)
	
	cntVP.grid(	column=0,	row=0)
	altasLb.grid(	column=0,	row=1, columnspan=2,padx=10)
	btnAlt.grid(	column=2,	row=2, columnspan=2,padx=10)
	btnBjs.grid(	column=2,	row=3, columnspan=2,padx=10)
	btnRep.grid(	column=2,	row=4, columnspan=2,padx=10)
	
	root.mainloop()
	
def getTables():
	try:
		db = mysql.connect(**data)
		cr = db.cursor()
		query = """
		SELECT TABLE_NAME 
		FROM information_schema.tables
		WHERE table_schema = 'escuela'
		"""
		cr.execute(query)
		for val in cr:
			tables.append(val[0].title())
	except ValueError:
		print 'err'

def darAltas(papa):
	tablaA = ''
	print 'dar alta'
	vent = Toplevel(papa)
	vent.title('Altas')
	vent.resizable(0,0)
	cntAl	= ttk.Frame(vent)
	cntAl.grid(column=0, row=0)
	tbls	= ttk.Combobox(cntAl,width = 15)
	tblsLb	= ttk.Label(cntAl, text="Tablas:")
	tbls['values'] = tables
	tblsLb.grid(column=0, row=0,padx=5)
	tbls.grid(column=1, row=0,padx=5)
	def obtener(e):
		global tablaA
		tablaA = tbls.get()
	tbls.bind('<<ComboboxSelected>>', obtener)

if __name__ == '__main__':
	#if(not init()): exit() #si no inicializa bien, salir
	data['password'] = '!Snowbasin1)'
	getTables()
	ventanaPrincipal()
	#print tables
	#ventanaPrincipal()
	"""
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
	"""