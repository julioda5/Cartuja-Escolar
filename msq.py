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
		psw = entry.get()
		if(psw):
			data['password'] = psw
			root.destroy()
	
	entry.bind("<Return>",getpsw)
	root.mainloop()
	
	getTables()
	
	return 'password' in data

def ventanaPrincipal():
	root = Tk()
	root.title('Base de Datos Escolares')
	root.resizable(0,0)
	cntVP = ttk.Frame(root)
	altasLb = ttk.Label(cntVP, text="Opciones:")
	def alto():
		darAltas(root)
	def cons():
		consultar(root)
			
	btnAlt = ttk.Button(cntVP, text = 'Altas',command = alto,width = 10)
	btnBjs = ttk.Button(cntVP, text = 'Bajas',command = alto,width = 10)
	btnRep = ttk.Button(cntVP, text = 'Reportes',command = alto,width = 10)
	btnCons = ttk.Button(cntVP, text = 'Consultas',command = alto,width = 10)
	
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
		db.close()
	except ValueError:
		print 'err'

def consultar(papa):
	pass
	
def getTblInfo(tbl):
	try:
		db = mysql.connect(**data)
		cr = db.cursor()
		query = """
		SELECT COLUMN_NAME,  DATA_TYPE, CHARACTER_MAXIMUM_LENGTH , IS_NULLABLE
		from INFORMATION_SCHEMA.COLUMNS 
		where table_name=""" +tbl +"and table_schema = 'escuela'"
		cr.execute(query)
		res = [n for n in cr]
		db.close()
		return res
	except ValueError:
		pass

def darAltas(papa):
	tablaA = None
	print 'dar alta'
	vent = Toplevel(papa)
	vent.title('Altas')
	vent.resizable(0,0)
	cntAl	= ttk.Frame(vent)
	cntAl.grid(column=0, row=0)
	tbls	= ttk.Combobox(cntAl,width = 15)
	tblsLb	= ttk.Label(cntAl, text="Tablas:")
	tbls['values'] = tables
	
	def obtener(e):
		global tablaA
		tablaA = tbls.get()
	tbls.bind('<<ComboboxSelected>>', obtener)
	
	tblsLb.grid(	column=0, row=0,padx=5)
	tbls.grid(		column=1, row=0,padx=5)


if __name__ == '__main__':
	#if(not init()): exit() #si no inicializa bien, salir
	
	#inicialización manual
	data['password'] = '!Snowbasin1)'
	getTables()
	#

	ventanaPrincipal()