import datos
import os


class Menu():
	def __init__(self):
		self.opcionPrincipal = None
		

	def seleccionar(self):
		print("1-Graficar")
		self.opcionPrincipal = int(input(""))
		self.limpiar()
		return self.opcionPrincipal

	
	def limpiar(self):
		os.system('cls')
		print("------------Analisis------------\n")

	
