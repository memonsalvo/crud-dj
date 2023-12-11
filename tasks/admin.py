from django.contrib import admin
from .models import Task
#se crea una clase que trae los datos del modelo creado
class TaskAdmin(admin.ModelAdmin): 
    readonly_fields = ('created',) 
    #cuales campos son de solo lectura y quiero ver en pantalla osea no se puede
    #modificar solo ver el dato o la info que se esta llamando
# Register your models here.
admin.site.register(Task, TaskAdmin)