#comentario
import mysql.connector as mysql
from Tkinter import *



def ventana():
	root = Tk()
	root.mainloop()

if __name__ == '__main__':
	ventana()
	
	try:
		data = {"host": "localhost", "user":"root","password":"!Snowbasin1)","database":"escuela"}
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