from django.db import models
from django.contrib.auth.models import User #se importa user de views.py

# Create your models here.
class Task(models.Model): #para que django pueda crear la tabla se hace dicho import
    title = models.CharField(max_length=100)  
    description = models.TextField(blank=True) #sino pasan datos el campo estara vacio 
    created = models.DateTimeField(auto_now_add=True) #fecha y hora de guardado por defecto
    datecompleted = models.DateTimeField(null=True) # va ser un campo vacio inicialmente
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + '- by' + self.user.username
    #con esto se personaliza el panel de admin al poner el nombre de quien lo hizo
    #o a que bd esta vinculado