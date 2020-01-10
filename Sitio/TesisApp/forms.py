from django import forms
from .models import *

class Status_PropuestaForm(forms.ModelForm):
    class Meta:
        model = Status_Propuesta
        fields = ['STATUS_PROPUESTA']

class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = ['TERM']

class Status_TGForm(forms.ModelForm):
    class Meta:
        model = Status_TG
        fields = ['STATUS_TG']

class TipoPersonaForm(forms.ModelForm):
    class Meta:
        model = Tipo_Persona
        fields = ['TIPO_PERSONA']

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['APELLIDOS','NOMBRES','CI','TIPO_PERSONA','CORREO_UCAB','CORREO_P','TELEFONO1','TELEFONO2','OBSERVACIONES'] 

class PropuestaForm(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = ['TITULO','FECHA_ENTREGA','TERM','STATUS','ALUMNO1','ALUMNO2','TUTOR_A','TUTOR_E']

class TGForm(forms.ModelForm):
    class Meta:
        model = TG
        fields = ['CODIGO','TITULO','PROPUESTA','TERM','STATUS','NRC','DESCRIPCION','CAT_TEMATICA','FECHA_ENTREGA','NOMBRE_EMPRESA']

class DefensaForm(forms.ModelForm):
    class Meta:
        model = Defensa
        fields = ['CODIGO','TG','FECHA_DEFENSA','JURADO1','JURADO2','JURADO_S','ASIST_J1','ASIST_J2','ASIST_JS','CALIFICACION','M_PUBLIC','M_HONOR','CORRECCIONES','FECHA_CORREC','NOTA_CARGADA','OBSERVACIONES']

