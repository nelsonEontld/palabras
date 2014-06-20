from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.core import serializers
from django.http import HttpResponse
from PalabrasFrasesEtiqueta import *


def vistaDePrueba(request):
    palabra=[]#PalabrasFrasesEtiqueta().getPalabrasExectList(('happy','dog'),(True,'idtodo'))
    '''palabra = PalabrasFrasesEtiqueta().getPalabras()
    palabra = PalabrasFrasesEtiqueta().getPalabrasAleatoria(3)
    palabra = PalabrasFrasesEtiqueta().getPalabraId(1)
    palabra = PalabrasFrasesEtiqueta().getPalabrasNombre('dog')
    palabra = PalabrasFrasesEtiqueta().getPalabrasNombreContains('ave')
    palabra = PalabrasFrasesEtiqueta().getPalabrasPorLetra('de')
    palabra = PalabrasFrasesEtiqueta().getPalabrasEmpezarLetra('f')
    palabra = PalabrasFrasesEtiqueta().getPalabrasTerminarLetra('h')
    palabra = PalabrasFrasesEtiqueta().getPalabrasNumeroLetras(4)
    palabra = PalabrasFrasesEtiqueta().getPalabrasExectId(2)
    palabra = PalabrasFrasesEtiqueta().getPalabrasExectNombre('cat')
    palabra = PalabrasFrasesEtiqueta().getPalabrasExectPalabra(PalabrasFrasesEtiqueta().getPalabraId(2))
    palabra = PalabrasFrasesEtiqueta().getPalabrasExectLetra('jhd')
    palabra = PalabrasFrasesEtiqueta().getPalabrasExectEmpezarLetra('f')
    palabra = PalabrasFrasesEtiqueta().getPalabrasExectTerminarLetra('d')
    palabra = PalabrasFrasesEtiqueta().getPalabrasExectList(('happy','dog'),(True,'id'))'''
    frases =[] #PalabrasFrasesEtiqueta().getFrasesPalabraNombre('happy')
    '''frases =  PalabrasFrasesEtiqueta().getFrases()
    frases =  PalabrasFrasesEtiqueta().getFrasesAleatoria(2)
    frases =  PalabrasFrasesEtiqueta().getFrasesPalabraId(2)
    frases =  PalabrasFrasesEtiqueta().getFrasesPalabraNombre('hoja')
    frases =  PalabrasFrasesEtiqueta().getFrasesExectPalabraNombre('elephant')
    frases =  PalabrasFrasesEtiqueta().getFrasesExectPalabraId(1)
    frases =  PalabrasFrasesEtiqueta().getFrasesExectPalabra(PalabrasFrasesEtiqueta().getPalabraId(2))
    frases =  PalabrasFrasesEtiqueta().getFrasesEmpezarCon('hoa')
    frases =  PalabrasFrasesEtiqueta().getFrasesTerminarCon('alo')
    frases =  PalabrasFrasesEtiqueta().getFrasesLetras('hjj')
    frases =  PalabrasFrasesEtiqueta().getFrasesPalabras('dj')
    frases =  PalabrasFrasesEtiqueta().getFrasesExectPalabras(('happy','dog'))
    frases =  PalabrasFrasesEtiqueta().getFrasesNumeroPalabras(2)'''
    #frases =  PalabrasFrasesEtiqueta().getFrasesExectNumeroPalabras(2)
    #frases =  PalabrasFrasesEtiqueta().getFrasesNumeroLetras(5
    estudiantesPublico = EstudiantePublico.objects.all()
    estudiantesColegio = EstudianteColegio.objects.all()
    secretarias = Secretaria.objects.all()
    return render_to_response('palabrasFrases/principal.html',{ 'EstudiantesPublico' : estudiantesPublico ,'EstudiantesColegio' : estudiantesColegio ,'Secretarias': secretarias}, RequestContext(request))



def busquedaAjaxView(request):
    nombre = request.GET['nombre']
    frases = [] #PalabrasFrasesEtiqueta().getFrasesPalabraNombre(nombre)
    dato = serializers.serialize('json', frases , fields =('estructurafrase','frase'))
    print dato
    return HttpResponse( dato, mimetype = 'application/json')