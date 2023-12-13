from django.forms import ModelForm #se diferencia que es una clase porque en este
#caso aparece en azul en vez de verde y a su vez empieza con mayuscula
from .models import Task #donde en models que es la forma en que se estructura lo
#pertinente a bd se crean preferiblemente los modelos que se quieren usar para form

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
#se crea el modelo en el cual estara basado este form, el cual podria tener varios modelos
#luego se importa de donde se traera dicho modelo y se le asigna a la varible llamada
#por medio de la nueva clase y luego por medio de fields se eligen los campos
#especificos que se quieren usar o llamar de todo el form creado en model a usar aca
#todos estos ya creados previamente en models.py
#luego se llama en views este form creado