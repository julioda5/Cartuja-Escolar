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
			
	btnAlt  = ttk.Button(cntVP, command = alto,width = 10, text = 'Altas')
	btnBjs  = ttk.Button(cntVP, command = alto,width = 10, text = 'Bajas')
	btnRep  = ttk.Button(cntVP, command = alto,width = 10, text = 'Reportes')
	btnCons = ttk.Button(cntVP, command = cons,width = 10, text = 'Consultas')
	
	cntVP.grid(	column=0,	row=0)
	altasLb.grid(	column=0,	row=1, columnspan=2,padx=10)
	btnAlt.grid(	column=2,	row=2, columnspan=2,padx=10)
	btnBjs.grid(	column=2,	row=3, columnspan=2,padx=10)
	btnRep.grid(	column=2,	row=4, columnspan=2,padx=10)
	btnCons.grid(	column=2,	row=5, columnspan=2,padx=10)
	
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
	print 'consulta'
	#Definición de variables
	infoTabla = None
	isFltr = IntVar()
	#Propiedades de Ventana
	vent = Toplevel(papa)
	vent.title('Consultar')
	vent.resizable(0,0)
	#Elementos de ventana
	cntAl	= ttk.Frame(vent)
	tbls	= ttk.Combobox(cntAl,width = 15)
	tblsLb	= ttk.Label(cntAl, text="Tablas:")
	def mostrarFlts():
		print 'a'
	filtro = ttk.Checkbutton(cntAl, text = 'Filtrar',variable = isFltr,command = mostrarFlts)
	tbls['values'] = tables
	
	def cons():
		print isFltr.get()
	consBtn = ttk.Button(cntAl,text='Filtar',command = cons)
	
	def obtener(e):
		global infoTabla
		infoTabla = getTblInfo(tbls.get())
	
		
	tbls.bind('<<ComboboxSelected>>', obtener)
	
	cntAl.grid(  column=0, row=0)
	tblsLb.grid( column=0, row=0,padx=5)
	tbls.grid(   column=1, row=0,padx=5)
	filtro.grid( column=2, row=0,padx=5)
	consBtn.grid(column=1, row=1,padx=5)
	
def getTblInfo(tbl):
	try:
		db = mysql.connect(**data)
		cr = db.cursor()
		query = """
		SELECT COLUMN_NAME,  DATA_TYPE, CHARACTER_MAXIMUM_LENGTH , IS_NULLABLE
		FROM INFORMATION_SCHEMA.COLUMNS 
		where table_name= '"""+tbl+"""' and table_schema = 'escuela'"""
		cr.execute(query)
		res = [n for n in cr]
		db.close()
		return res
	except ValueError:
		pass

def darAltas(papa):
	global datos
	global darAlta
	darAlta= None
	datos	= []
	#print 'Dar alta'
	vent = Toplevel(papa)
	vent.title('Altas')
	vent.resizable(0,0)
	cntAl	= ttk.Frame(vent)
	cntAl.grid(column=0, row=0)
	tbls	= ttk.Combobox(cntAl,width = 15)
	tblsLb	= ttk.Label(cntAl, text="Tablas:")
	tbls['values'] = tables
	
	def obtener(e):
		global datos
		global darAlta
		#eliminar cosas
		for n in datos: 
			n[0].grid_remove()
			n[1].grid_remove()
			
		try: darAlta.grid_remove()
		except: pass
		tabla = tbls.get()
		infoTabla = getTblInfo(tabla)
		print infoTabla
		i = 2
		for n in infoTabla:
			tmpE = ttk.Entry(cntAl,width=15)
			tmpL = ttk.Label(cntAl,text = n[0].title(), justify='right')
			tmpE.grid(column=1,row=i, columnspan=2)
			tmpL.grid(column=0,row=i)
			i+=1
			datos+=[(tmpL,tmpE)]
		
		def darAlta():
			vals = {}
			for n in xrange(len(datos)):
				dat = datos[n][1].get()
				if(dat):
					#print infoTabla[n][0]
					vals[infoTabla[n][0]] = (dat,infoTabla[n][1],infoTabla[n][2])
				elif(infoTabla[n][-1] == 'NO'):
					print 'error'
					return
			str1 = ""
			str2 = ""
			for n in vals.keys():
				if(str1): str1 += ", "
				if(str2): str2 += ", "
				str1 += n
				if(vals[n][1] == 'char'):
					str2 += "'"+vals[n][0]+"'"
				else: 
					str2 += vals[n][0]
			
			query = "INSERT INTO "+str(tabla)+" ("+str1+") VALUES ("+str2+")"
			print query
			try:
				db = mysql.connect(**data)
				cr = db.cursor()
				cr.execute(query)
				db.commit()
				db.close()
			except ValueError:
				print 'err'
			
				
		darAlta = ttk.Button(cntAl, text='Dar de alta',command = darAlta)
		darAlta.grid(column=1,row=i)

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