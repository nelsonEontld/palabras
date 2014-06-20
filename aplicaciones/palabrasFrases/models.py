from __future__ import unicode_literals
from django.db import models


class Calificacion(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True)
    #auto_create_schema = True

    class Meta:
        db_table = 'contenido_idioma"."Calificacion'

class Idioma(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45, blank=True)
    class Meta:

        db_table = 'geolocalizacion"."Idioma'

class Imagen(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=30)
    ruta = models.CharField(unique=True, max_length=45, blank=True)
    class Meta:
        db_table = 'multimedia"."Imagen'

class Sonido(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45)
    ruta = models.CharField(unique=True, max_length=45, blank=True)
    class Meta:

        db_table = 'multimedia"."Sonido'


class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=30)
    ruta = models.CharField(unique=True, max_length=45, blank=True)
    class Meta:

        db_table = 'multimedia"."Video'

class Etiqueta(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True)
    idioma = models.ForeignKey('Idioma', db_column='Idioma_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Etiqueta'



class Palabra(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    idioma = models.ForeignKey(Idioma, db_column='Idioma_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Palabra'



class DefinicionPalabra(models.Model):
    palabra = models.ForeignKey('Palabra', db_column='Palabra_id', primary_key=True) # Field name made lowercase.
    definicion = models.CharField(unique=True, max_length=255)
    idioma = models.ForeignKey('Idioma', db_column='Idioma_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Definicion_Palabra'

class Estado(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True)
    class Meta:

        db_table = 'contenido_idioma"."Estado'

class Frase(models.Model):
    id = models.IntegerField(primary_key=True)
    clausula = models.CharField(unique=True, max_length=255)
    calificacion = models.ForeignKey(Calificacion, db_column='Calificacion_id') # Field name made lowercase.
    idioma = models.ForeignKey('Idioma', db_column='Idioma_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Frase'

class FraseRespondeFrase(models.Model):
    frase = models.ForeignKey(Frase, db_column='Frase_id') # Field name made lowercase.
    frase_id1 = models.ForeignKey(Frase, db_column='Frase_id1',related_name='topic_content_type') # Field name made lowercase.
    estado = models.ForeignKey(Estado, db_column='Estado_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Frase_Responde_Frase'

class FraseTieneEtiqueta(models.Model):
    frase = models.ForeignKey(Frase, db_column='Frase_id') # Field name made lowercase.
    etiqueta = models.ForeignKey(Etiqueta, db_column='Etiqueta_id') # Field name made lowercase.
    estado = models.ForeignKey(Estado, db_column='Estado_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Frase_Tiene_Etiqueta'



class EstructuraFrase(models.Model):
    frase = models.ForeignKey('Frase', db_column='Frase_id', primary_key=True) # Field name made lowercase.
    palabras = models.CharField(unique=True, max_length=45)
    class Meta:

        db_table = 'contenido_idioma"."Estructura_Frase'

class EstructuraFraseEtiquetas(models.Model):
    frase = models.ForeignKey('Frase', db_column='Frase_id', primary_key=True) # Field name made lowercase.
    etiquetas = models.CharField(max_length=500)
    class Meta:

        db_table = 'contenido_idioma"."Estructura_Frase_Etiquetas'


class EtiquetaTieneEtiqueta(models.Model):
    etiqueta_id_index = models.ForeignKey(Etiqueta, db_column='Etiqueta_id_index') # Field name made lowercase.
    etiqueta = models.ForeignKey(Etiqueta, db_column='Etiqueta_id',related_name='topic_content_type') # Field name made lowercase.
    estado = models.ForeignKey(Estado, db_column='Estado_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Etiqueta_Tiene_Etiqueta'

class EtiquetaTieneImagen(models.Model):
    etiqueta = models.ForeignKey(Etiqueta, db_column='Etiqueta_id') # Field name made lowercase.
    imagen = models.ForeignKey('Imagen', db_column='Imagen_id') # Field name made lowercase.
    estado = models.ForeignKey(Estado, db_column='Estado_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Etiqueta_Tiene_Imagen'

class EtiquetaTieneSonido(models.Model):
    etiqueta = models.ForeignKey(Etiqueta, db_column='Etiqueta_id') # Field name made lowercase.
    sonido = models.ForeignKey('Sonido', db_column='Sonido_id') # Field name made lowercase.
    estado = models.ForeignKey(Estado, db_column='Estado_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Etiqueta_Tiene_Sonido'

class TipoEtiqueta(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45, blank=True)
    idioma = models.ForeignKey(Idioma, db_column='Idioma_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Tipo_Etiqueta'


class EtiquetaTieneTipoEtiqueta(models.Model):
    etiqueta = models.ForeignKey(Etiqueta, db_column='Etiqueta_id') # Field name made lowercase.
    tipo_etiqueta = models.ForeignKey('TipoEtiqueta', db_column='Tipo_Etiqueta_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Etiqueta_Tiene_Tipo_Etiqueta'

class EtiquetaTieneVideo(models.Model):
    etiqueta = models.ForeignKey(Etiqueta, db_column='Etiqueta_id') # Field name made lowercase.
    video = models.ForeignKey('Video', db_column='Video_id') # Field name made lowercase.
    estado = models.ForeignKey(Estado, db_column='Estado_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Etiqueta_Tiene_Video'





class PalabraTieneEtiqueta(models.Model):
    palabra = models.ForeignKey(Palabra, db_column='Palabra_id') # Field name made lowercase.
    etiqueta = models.ForeignKey(Etiqueta, db_column='Etiqueta_id') # Field name made lowercase.
    estado = models.ForeignKey(Estado, db_column='Estado_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Palabra_Tiene_Etiqueta'

class PalabraTieneImagen(models.Model):
    palabra = models.ForeignKey(Palabra, db_column='Palabra_id') # Field name made lowercase.
    imagen = models.ForeignKey(Imagen, db_column='Imagen_id') # Field name made lowercase.
    estado = models.ForeignKey(Estado, db_column='Estado_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Palabra_Tiene_Imagen'

class PalabraTieneSonido(models.Model):
    palabra = models.ForeignKey(Palabra, db_column='Palabra_id') # Field name made lowercase.
    sonido = models.ForeignKey('Sonido', db_column='Sonido_id') # Field name made lowercase.
    estado = models.ForeignKey(Estado, db_column='Estado_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Palabra_Tiene_Sonido'

class PalabraTieneVideo(models.Model):
    palabra = models.ForeignKey(Palabra, db_column='Palabra_id') # Field name made lowercase.
    video = models.ForeignKey('Video', db_column='Video_id') # Field name made lowercase.
    estado = models.ForeignKey(Estado, db_column='Estado_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Palabra_Tiene_Video'



class TraduccionDeEtiqueta(models.Model):
    etiqueta_origen = models.ForeignKey(Etiqueta, db_column='Etiqueta_origen', related_name='etiqueta_distinta') # Field name made lowercase.
    etiqueta_destino = models.ForeignKey(Etiqueta, db_column='Etiqueta_destino') # Field name made lowercase.
    idioma = models.ForeignKey(Idioma, db_column='Idioma_id') # Field name made lowercase.
    class Meta:
        db_table = 'contenido_idioma"."Traduccion_De_Etiqueta'


class TraduccionDePalabra(models.Model):
    palabra_origen = models.ForeignKey(Palabra, db_column='Palabra_origen_id') # Field name made lowercase.
    palabra_destino = models.ForeignKey(Palabra, db_column='Palabra_destino_id',related_name='palabra_distinta') # Field name made lowercase.
    idioma_destino = models.ForeignKey(Idioma, db_column='Idioma_destino_id') # Field name made lowercase.
    class Meta:

        db_table = 'contenido_idioma"."Traduccion_De_Palabra'