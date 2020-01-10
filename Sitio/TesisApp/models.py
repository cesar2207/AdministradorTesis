from django.db import models

class Status_Propuesta(models.Model):
    STATUS_PROPUESTA = models.CharField(max_length=15)

class Term(models.Model):
    TERM = models.CharField(max_length=15)

class Status_TG(models.Model):
    STATUS_TG = models.CharField(max_length=40)

class Tipo_Persona(models.Model):
    TIPO_PERSONA = models.CharField(max_length=15)

class Persona(models.Model):
    APELLIDOS = models.CharField(max_length=50)
    NOMBRES = models.CharField(max_length=50)
    CI = models.IntegerField()
    TIPO_PERSONA = models.ForeignKey(Tipo_Persona, on_delete=models.CASCADE, related_name='tipoPersona')
    CORREO_UCAB = models.CharField(max_length=30, blank=True)
    CORREO_P = models.CharField(max_length=30)
    TELEFONO1 = models.CharField(max_length=15)
    TELEFONO2 = models.CharField(max_length=15, blank=True)
    OBSERVACIONES = models.CharField(max_length=100, blank=True)

class Propuesta(models.Model):
    CODIGO = models.IntegerField(primary_key=True)
    TITULO =  models.CharField(max_length=150)
    FECHA_ENTREGA = models.DateTimeField("FECHA ENTREGA")
    TERM = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='termPropuesta')
    STATUS = models.ForeignKey(Status_Propuesta, on_delete=models.CASCADE, related_name='statusPropuesta')
    ALUMNO1 =   models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='alumno1')      
    ALUMNO2 =   models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='alumno2', blank=True, null=True)
    TUTOR_A =   models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='tutorA')
    TUTOR_E =   models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='tutorE', blank=True, null=True)


class TG(models.Model):
    CODIGO = models.CharField(primary_key=True, max_length=50)
    TITULO = models.CharField(max_length=100)
    PROPUESTA = models.ForeignKey(Propuesta, on_delete=models.CASCADE, related_name='propuesta')
    TERM = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='termTG')
    STATUS = models.ForeignKey(Status_TG, on_delete=models.CASCADE, related_name='termTG')
    NRC = models.CharField(max_length=10)
    DESCRIPCION = models.CharField(max_length=50)
    CAT_TEMATICA = models.CharField(max_length=50)
    FECHA_ENTREGA = models.DateTimeField("FECHA ENTREGA")
    NOMBRE_EMPRESA = models.CharField(max_length=50)

class Defensa(models.Model):
    CODIGO = models.CharField(primary_key=True, max_length=30)
    TG = models.ForeignKey(TG, on_delete=models.CASCADE, related_name='TG')
    FECHA_DEFENSA = models.DateTimeField("FECHA DEFENSA")
    JURADO1 = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='jurado1')
    JURADO2 = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='jurado2')
    JURADO_S = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='juradoS')
    ASIST_J1 = models.IntegerField()
    ASIST_J2 = models.IntegerField()
    ASIST_JS = models.IntegerField()
    CALIFICACION = models.IntegerField()
    M_PUBLIC = models.IntegerField()
    M_HONOR = models.IntegerField()
    CORRECCIONES = models.IntegerField()
    FECHA_CORREC = models.DateTimeField("FECHA CORRECCIONES")
    NOTA_CARGADA = models.IntegerField()
    OBSERVACIONES = models.CharField(max_length=200)
# Create your models here.
