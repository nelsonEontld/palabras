from django.db import models

# Create your models here.

class Etiqueta(models.Model):
    idetiqueta = models.IntegerField(db_column='IDEtiqueta', primary_key=True) # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True) # Field name made lowercase.
    traduccionespaniol = models.CharField(db_column='TraduccionEspaniol', max_length=50, blank=True) # Field name made lowercase.
    traduccionkoreano = models.CharField(db_column='TraduccionKoreano', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'etiqueta'


class Todo(models.Model):
    idtodo = models.IntegerField(db_column='IDTodo', primary_key=True) # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'todo'

class Frases(models.Model):
    estructurafrase = models.TextField(db_column='EstructuraFrase', primary_key=True, max_length=500) # Field name made lowercase.
    frase = models.TextField(db_column='Frase', blank=True) # Field name made lowercase.
    calificacion = models.CharField(db_column='Calificacion', max_length=20, blank=True) # Field name made lowercase.
    palabraseparadas = models.TextField(db_column='PalabraSeparadas', blank=True) # Field name made lowercase.
    estructuraetiqueta = models.TextField(db_column='EstructuraEtiqueta', max_length=500, blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'frases'


class TodoEtiqueta(models.Model):
    idtodo = models.ForeignKey(Todo, db_column='IDTodo') # Field name made lowercase.
    idetiqueta = models.ForeignKey(Etiqueta, db_column='IDEtiqueta') # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'todo_etiqueta'
