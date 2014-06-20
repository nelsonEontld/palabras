from models import *
from django.db import connection
from django.db.models import Q
import random
import operator


class PalabrasFrasesEtiqueta(object):

	dbMultimedia = 'Multimedia'
	dbGeolocalizacion = 'Geolocalizacion'


	def getPalabras(self, order = (False,"") ):
		palabras=Palabra.objects.all()	
		
		if(order[0]):
			palabras = palabras.order_by(order[1])

		return palabras

	def getPalabrasAleatoria(self, limite = None ,  order = (False,"") ):
		count = Palabra.objects.all().count()		
		
		if(not(limite == None)):
			if(count >= limite):
				slice = random.random() * (count - limite)
				palabras = Palabra.objects.all()[slice: slice+limite]
			else:
				palabras = Palabra.objects.all()		
		else:
			palabras = Palabra.objects.all()		

		return palabras

	def getPalabraId(self, id):
		palabras = Palabra.objects.filter(pk=id)			
		return palabras

	def getPalabrasNombre(self, nombre):
		palabras = Palabra.objects.filter(nombre__exact = nombre)		
		return palabras

	def getPalabrasNombreContains(self, nombre , order = (False,"") ):
		palabras= Palabra.objects.filter(nombre__contains = nombre)
		
		if(order[0]):
			palabras = palabras.order_by(order[1])

		return palabras

	def getPalabrasPorLetra(self, letras , order = (False,"") ):
		palabras = Palabra.objects.all()
		qset=[]		
		for letra in letras:
			qset.append(
				Q(nombre__contains = letra) 
			)
		palabras = palabras.filter(reduce(operator.or_,qset))
		
		if(order[0]):
			palabras=palabras.order_by(order[1])

		return palabras

	def getPalabrasEmpezarLetra(self, letra , order = (False,"") ):
		palabras = Palabra.objects.filter(nombre__startswith = letra)
		
		if(order[0]):
			palabras=palabras.order_by(order[1])

		return palabras

	def getPalabrasTerminarLetra(self, letra , order = (False,"") ):
		palabras = Palabra.objects.filter(nombre__endswith = letra)
		
		if(order[0]):
			palabras=palabras.order_by(order[1])

		return palabras

	def getPalabrasNumeroLetras(self, numero, order = (False,"") ):
		 #Frases.objects.filter(frase__size = numero)
		palabras =[]
		if(order[0]):
			palabras = Palabra.objects.raw("SELECT id, nombre FROM Palabra WHERE LENGTH(nombre) = "+str(numero)+" ORDER BY "+order[1]+"")
		else:
			palabras = Palabra.objects.raw("SELECT id, nombre FROM Palabra WHERE LENGTH(nombre) = "+str(numero)+"")
		return palabras

	def getPalabrasLimit(self, limite , order = (False,"") ):
		palabras=Palabra.objects.all()
		if(order[0]):
			palabras = palabras.order_by(order[1])[:limite]					
		return palabras

	def getPalabrasExectId(self, id , order = (False,"") ):
		palabras=Palabra.objects.exclude(id__exact = id)
		
		if(order[0]):
			palabras = palabras.order_by(order[1])

		return palabras

	def getPalabrasExectNombre(self , nombre , order = (False,"") ):
		palabras=Palabra.objects.exclude(nombre__exact = nombre)
		
		if(order[0]):
			palabras= palabras.order_by(order[1])

		return palabras

	def getPalabrasExectPalabra(self , palabra , order = (False,"") ):
		palabras =[]
		if(isinstance(palabra, Palabra)):
			palabras = Palabra.objects.exclude(pk = palabra.id)
		
		if(order[0]):
			palabras=palabras.order_by(order[1])

		return palabras


	def getPalabrasExectLetra(self, letras , order = (False,"") ):
		palabras = Palabra.objects.all()
		qset=[]		
		for letra in letras:
			qset.append(
				Q(nombre__contains = letra) 
			)
		
		palabras = palabras.exclude(reduce(operator.or_,qset))
		
		if(order[0]):
			palabras=palabras.order_by(order[1])

		return palabras

	def getPalabrasExectEmpezarLetra(self, letra , order = (False,"") ):
		palabras = Palabra.objects.exclude(nombre__startswith = letra)
		
		if(order[0]):
			palabras=palabras.order_by(order[1])

		return palabras

	def getPalabrasExectTerminarLetra(self, letra , order = (False,"") ):
		palabras = Palabra.objects.exclude(nombre__endswith = letra)
		
		if(order[0]):
			palabras=palabras.order_by(order[1])

		return palabras


	def getPalabrasExectList(self,lista, order = (False,"") ):
		palabras = Palabra.objects.all()
		qset=[]		
		for palabra in lista:
			qset.append(
				Q(nombre__exact = palabra) 
			)
		
		palabras = palabras.exclude(reduce(operator.or_,qset))
		if(order[0]):			
			palabras= palabras.order_by(order[1])

		return palabras

	def getFrases(self, order = (False,"")):
		frases = Frase.objects.all()
		if(order[0]):
			frases = frases.order_by(order[1])
		return frases

	def getFrasesAleatoria(self, limite = 0 ,  order = (False,"") ):
		count = Frase.objects.all().count()		
		

		if(not(limite == None)):
			if(count >= limite):
				slice = random.random() * (count - limite)
				frases = Frase.objects.all()[slice: slice+limite]
			else:
				frases = Frase.objects.all()	
		else:
			frases = Frase.objects.all()		
		

		return frases

	def getFrasesPalabraId(self, id):
		frase = []
		return frase

	def getFrasesExectPalabra(self, id):
		frases = []
		return frases


	def getFrasesPalabraNombre(self, nombre, order = (False,"") ):
		frases = Frase.objects.filter(clausula__contains = nombre) 
		if(order[0]):
			frases = frases.order_by(order[1])
		return frases

	def getFrasesExectPalabraNombre(self, nombre , order = (False,"") ):
		frases = Frase.objects.exclude(clausula__contains = nombre) 
		if(order[0]):
			frases = frases.order_by(order[1])
		return frases

	def getFrasesExectPalabraId(self, id):
		frases = []
		return frases



	def getFrasesExectPalabra(self, palabra , order = (False,"") ):
		frases = []
		return frases


	def getFrasesEmpezarCon(self, algo , order = (False,"") ):
		frases = Frase.objects.filter(clausula__startswith = algo)
		
		if(order[0]):
			frases = frases.order_by(order[1])

		return frases

	def getFrasesTerminarCon(self, algo , order = (False,"") ):
		frases = Frase.objects.filter(clausula__endswith = algo)
		
		if(order[0]):
			frases = frases.order_by(order[1])

		return frases

	def getFrasesLetras(self, letras, order = (False,"") ):
		frases = Frase.objects.all()
		qset=[]		
		for letra in letras:
			if(len(letra) == 1):
				qset.append(
					Q(clausula__contains = letra) 
				)
		
		frases = frases.filter(reduce(operator.or_,qset))
		if(order[0]):
			frases = frases.order_by(order[1])
		return frases


	def getFrasesExectLetras(self, letras, order = (False,"") ):
		frases = Frase.objects.all()
		qset=[]		
		for letra in letras:
			if(len(letra) == 1):
				qset.append(
					Q(clausula__contains = letra) 
				)
		frases = frases.exclude(reduce(operator.or_,qset))
		if(order[0]):
			frases = frases.order_by(order[1])
		return frases


	def getFrasesPalabras(self, palabras, order = (False,"") ):
		frases = Frase.objects.all()
		qset=[]		
		for palabra in palabras:
			if(isinstance(palabra, Palabra)):
				qset.append(
					Q(clausula__contains = palabra.nombre) 
				)
			elif(isinstance(palabra, str)):	
				qset.append(
					Q(clausula__contains = palabra) 
				)			
		frases = frases.filter(reduce(operator.or_,qset))
		if(order[0]):
			frases = frases.order_by(order[1])
		return frases



	def getFrasesExectPalabras(self, palabras, order = (False,"") ):
		frases = Frase.objects.all()
		qset=[]		
		for palabra in palabras:
			if(isinstance(palabra, Palabra)):
				qset.append(
					Q(clausula__contains = palabra.nombre) 
				)
			elif(isinstance(palabra, str)):	
				qset.append(
					Q(clausula__contains = palabra) 
				)				
		frases = frases.exclude(reduce(operator.or_,qset))
		if(order[0]):
			frases = frases.order_by(order[1])
		return frases



	def getFrasesNumeroPalabras(self, numero, order = (False,"") ):
		frases =[]

		if(order[0]):
			frases = Frase.objects.raw("SELECT id, clausula FROM Frase WHERE wordcount(clausula,' ',"+str(numero)+") ORDER BY "+order[1]+"") #Frases.objects.filter(frase__size = numero)
		else:
			frases = Frase.objects.raw("SELECT id, clausula FROM Frase WHERE wordcount(clausula,' ',"+str(numero)+")") #Frases.objects.filter(frase__size = numero)				
		return frases

	def getFrasesExectNumeroPalabras(self, numero, order = (False,"") ):
		frases =[]

		if(order[0]):
			frases = Frase.objects.raw("SELECT id, clausula FROM Frase WHERE not(wordcount(clausula,' ',"+str(numero)+")) ORDER BY "+order[1]+"") #Frases.objects.filter(frase__size = numero)
		else:
			frases = Frase.objects.raw("SELECT id, clausula FROM Frase WHERE not(wordcount(clausula,' ',"+str(numero)+"))") #Frases.objects.filter(frase__size = numero)				
		return frases


	def getFrasesNumeroLetras(self, numero, order = (False,"") ):
		frases =[]
		if(order[0]):
			frases = Frase.objects.raw("SELECT id, clausula FROM Frase WHERE LENGTH(REPLACE(Frase,' ', '')) = "+str(numero)+" ORDER BY "+order[1]+"")
		else:
			frases = Frase.objects.raw("SELECT id, clausula FROM Frase WHERE LENGTH(REPLACE(Frase,' ', '')) = "+str(numero)+"")
		return frases

