from models import *
from django.db import connection
from django.db.models import Q
import random
import operator


class PalabrasFrasesEtiqueta(object):

	def getPalabras(self, order = (False,"") ):
		palabras=Todo.objects.all()	
		
		if(order[0]):
			palabras = palabras.order_by(order[1])

		return palabras

	def getPalabrasAleatoria(self, limite = None ,  order = (False,"") ):
		count = Todo.objects.all().count()		
		

		if(not(limite == None)):
			slice = random.random() * (count - limite)
			palabras = Todo.objects.all()[slice: slice+limite]	
		else:
			palabras = Todo.objects.all()		

		return palabras

	def getPalabraId(self, id):
		palabras = Todo.objects.get(pk=id)			
		return palabras

	def getPalabrasNombre(self, nombre):
		palabras = Todo.objects.filter(nombre__exact = nombre)		
		return palabras

	def getPalabrasNombreContains(self, nombre , order = (False,"") ):
		palabras= Todo.objects.filter(nombre__contains = nombre)
		
		if(order[0]):
			palabras = palabras.order_by(order[1])

		return palabras

	def getPalabrasPorLetra(self, letras , order = (False,"") ):
		palabras = Todo.objects.all()
		qset=[]		
		for letra in lista:
			qset.append(
				Q(nombre__contains = letra) 
			)
		palabras = palabras.filter(reduce(operator.or_,qset))
		
		if(order[0]):
			palabras=palabras.order_by(order[1])

		return palabra

	def getPalabrasEmpezarLetra(self, letra , order = (False,"") ):
		palabras = Todo.objects.filter(nombre__startswith = letra)
		
		if(order[0]):
			palabras=palabras.order_by(order[1])

		return palabras

	def getPalabrasTerminarLetra(self, letra , order = (False,"") ):
		palabras = Todo.objects.filter(nombre__endswith = letra)
		
		if(order[0]):
			palabras=palabras.order_by(order[1])

		return palabras

	def getPalabrasNumeroLetras(self, numero, order = (False,"") ):
		 #Frases.objects.filter(frase__size = numero)
		palabras =[]
		if(order[0]):
			palabras = Todo.objects.raw("SELECT idtodo, nombre FROM palabras WHERE LENGTH(nombre) = "+str(numero)+" ORDER BY "+order[1]+"")
		else:
			palabras = Todo.objects.raw("SELECT idtodo, nombre FROM frases WHERE LENGTH(REPLACE(nombre) = "+str(numero)+"")
		return frases

	def getPalabrasLimit(self, limite , order = (False,"") ):
		palabras=Todo.objects.all()
		if(order[0]):
			palabras = palabras.order_by(order[1])[:limite]					
		return palabras

	def getPalabrasExectId(self, id , order = (False,"") ):
		palabras=Todo.objects.exclude(idtodo__exact = id)
		
		if(order[0]):
			palabras = palabras.order_by(order[1])

		return palabra

	def getPalabrasExectNombre(self , nombre , order = (False,"") ):
		palabras=Todo.objects.exclude(nombre__exact = nombre)
		
		if(order[0]):
			palabras= palabras.order_by(order[1])

		return palabras

	def getPalabrasExectPalabra(self , palabra , order = (False,"") ):

		palabras = Todo.objects.exclude(idtodo = palabra.idtodo)
		
		if(order[0]):
			palabras=palabras.order_by(order[1])


		return palabras


	def getPalabrasExectLetra(self, letras , order = (False,"") ):
		palabras = Todo.objects.all()
		qset=[]		
		for letra in lista:
			qset.append(
				Q(nombre__contains = letra) 
			)
		
		palabras = palabras.exclude(reduce(operator.or_,qset))
		
		if(order[0]):
			palabras=palabras.order_by(order[1])

		return palabra

	def getPalabrasExectEmpezarLetra(self, letra , order = (False,"") ):
		palabras = Todo.objects.exclude(nombre__startswith = letra)
		
		if(order[0]):
			palabras=palabras.order_by(order[1])

		return palabras

	def getPalabrasExectTerminarLetra(self, letra , order = (False,"") ):
		palabras = Todo.objects.exclude(nombre__endswith = letra)
		
		if(order[0]):
			palabras=palabras.order_by(order[1])

		return palabras


	def getPalabrasExectList(self,lista, order = (False,"") ):
		palabras = Todo.objects.all()
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
		frases = Frases.objects.all()
		if(order[0]):
			frases = frases.order_by(order[1])
		return frases

	def getFrasesAleatoria(self, limite = 1 ,  order = (False,"") ):
		count = Frases.objects.all().count()		
		

		if(not(limite == None)):
			slice = random.random() * (count - limite)
			frases = Frases.objects.all()[slice: slice+limite]	
		else:
			frases = Frases.objects.all()		
		

		return frases

	def getFrasesPalabraId(self, id):
		frase = []
		return frase


	def getFrasesPalabraNombre(self, nombre, order = (False,"") ):
		frases = Frases.objects.filter(frase__contains = nombre) 
		if(order[0]):
			frases = frases.order_by(order[1])
		return frases

	def getFrasesExectPalabraNombre(self, nombre , order = (False,"") ):
		frases = Frases.objects.exclude(frase__contains = nombre) 
		if(order[0]):
			frases = frases.order_by(order[1])
		return frases

	def getFrasesExectPalabraId(self, nombre):
		frases = []
		return frases

	def getFrasesExectPalabra(self, palabra , order = (False,"") ):
		frases = []
		"""Frases.objects.exclude(frase__contains = nombre) 
								if(order[0]):
									frases = frases.order_by(order[1])"""
		return frases


	def getFrasesEmpezarCon(self, algo , order = (False,"") ):
		frases = Frases.objects.filter(nombre__startswith = algo)
		
		if(order[0]):
			frases = frases.order_by(order[1])

		return frases

	def getFrasesTerminarCon(self, algo , order = (False,"") ):
		frases = Frases.objects.filter(nombre__endswith = algo)
		
		if(order[0]):
			frases = frases.order_by(order[1])

		return frases

	def getFrasesLetras(self, letras, order = (False,"") ):
		frases = Frases.objects.all()
		qset=[]		
		for letra in letras:
			if(letra.LENGTH == 1):
				qset.append(
					Q(frase__contains = palabra) 
				)
		
		frases = frases.filter(reduce(operator.or_,qset))
		if(order[0]):
			frases = frases.order_by(order[1])
		return frases


	def getFrasesExectLetras(self, letras, order = (False,"") ):
		frases = Frases.objects.all()
		qset=[]		
		for letra in letras:
			if(letra.LENGTH == 1):
				qset.append(
					Q(frase__contains = letra) 
				)
		frases = frases.exclude(reduce(operator.or_,qset))
		if(order[0]):
			frases = frases.order_by(order[1])
		return frases


	def getFrasesPalabras(self, palabras, order = (False,"") ):
		frases = Frases.objects.all()
		qset=[]		
		for palabra in palabras:
			if(isinstance(palabra, Todo)):
				qset.append(
					Q(frase__contains = palabra.nombre) 
				)
			elif(isinstance(palabra, str)):	
				qset.append(
					Q(frase__contains = palabra) 
				)			
		frases = frases.filter(reduce(operator.or_,qset))
		if(order[0]):
			frases = frases.order_by(order[1])
		return frases



	def getFrasesExectPalabras(self, letras, order = (False,"") ):
		frases = Frases.objects.all()
		qset=[]		
		for palabra in palabras:
			if(isinstance(palabra, Todo)):
				qset.append(
					Q(frase__contains = palabra.nombre) 
				)
			elif(isinstance(palabra, str)):	
				qset.append(
					Q(frase__contains = palabra) 
				)				
		frases = frases.exclude(reduce(operator.or_,qset))
		if(order[0]):
			frases = frases.order_by(order[1])
		return frases



	def getFrasesNumeroPalabras(self, numero, order = (False,"") ):
		frases =[]

		if(order[0]):
			frases = Frases.objects.raw("SELECT EstructuraFrase , Frase , Calificacion , PalabraSeparadas , EstructuraEtiqueta  FROM frases WHERE wordcount(Frase,' ',"+str(numero)+") ORDER BY "+order[1]+"") #Frases.objects.filter(frase__size = numero)
		else:
			frases = Frases.objects.raw("SELECT EstructuraFrase , Frase , Calificacion , PalabraSeparadas , EstructuraEtiqueta FROM frases WHERE wordcount(Frase,' ',"+str(numero)+")") #Frases.objects.filter(frase__size = numero)
				
		return frases

	def getFrasesNumeroLetras(self, numero, order = (False,"") ):
		frases =[]
		if(order[0]):
			frases = Frases.objects.raw("SELECT EstructuraFrase , Frase , Calificacion , PalabraSeparadas , EstructuraEtiqueta FROM frases WHERE LENGTH(REPLACE(Frase,' ', '')) = "+str(numero)+" ORDER BY "+order[1]+"")
		else:
			frases = Frases.objects.raw("SELECT EstructuraFrase , Frase , Calificacion , PalabraSeparadas , EstructuraEtiqueta FROM frases WHERE LENGTH(REPLACE(Frase,' ', '')) = "+str(numero)+"")
		return frases

