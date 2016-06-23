
class Instrumentos_musicales:

	def inicializar(self, percu):
		self.percursion=percu


	def impresion(self):
		print ("instrumento:" )
		print (self.percursion)
		print ("")

instrumento1=Instrumentos_musicales()
instrumento1.inicializar("Bateria")
instrumento1.impresion()

instrumento2=Instrumentos_musicales()
instrumento2.inicializar("Tambor")
instrumento2.impresion()

instrumento3=Instrumentos_musicales()
instrumento3.inicializar("Ponpon")
instrumento3.impresion()