#comentario
import mysql.connector as mysql
from Tkinter import *
import ttk
import getpass

data = {"host": "localhost", "user":"root","database":"escuela"}

def init():
	passwd = getpass.getpass('Password --> ') 
	data['password'] = passwd

def ventanaPrincipal():
	root = Tk()
	root.title('Base de Datos Escolares')
	root.mainloop()

if __name__ == '__main__':
	init()
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