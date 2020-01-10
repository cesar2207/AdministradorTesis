from django.contrib import admin
from .models import Defensa, Persona,Propuesta,Status_Propuesta,Status_TG,Term,TG,Tipo_Persona
# Register your models here.
admin.site.register(Status_Propuesta)
admin.site.register(Term)
admin.site.register(Tipo_Persona)
admin.site.register(Status_TG)
admin.site.register(Persona)
admin.site.register(Propuesta)
admin.site.register(TG)
admin.site.register(Defensa)