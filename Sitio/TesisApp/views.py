from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    return render(request,'index.html')

def lista_status_propuesta(request):
    status_propuesta = Status_Propuesta.objects.all()
    return render(request,'status_propuesta.html',{'status_propuesta':status_propuesta})

def crear_status_propuesta(request):
    form_status_p = Status_PropuestaForm(request.POST or None)
    if form_status_p.is_valid():
        form_status_p.save()
        return redirect('lista_status_propuesta')

    return render(request, 'status_propuestaForm.html', {'form_status_p': form_status_p})

def modificar_status_propuesta(request, id):
    status_propuesta = Status_Propuesta.objects.get(id=id)
    form = Status_PropuestaForm(request.POST or None, instance=status_propuesta)
    if form.is_valid():
        form.save()
        return redirect('lista_status_propuesta')

    return render(request, 'status_propuestaForm.html',{'form_status_p':form,'status_p':status_propuesta})

def lista_term(request):
    term = Term.objects.all()
    return render(request, 'lista_term.html',{'term':term})

def crear_term(request):
    form = TermForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_term')
    return render(request,'termForm.html', {'form_term':form})

def modificar_term(request,id):
    term = Term.objects.get(id=id)
    form = TermForm(request.POST or None, instance=term)
    if form.is_valid():
        form.save()
        return redirect('lista_term')
    return render(request,'termForm.html',{'form_term':form,'term':term})

def lista_status_tg(request):
    status_tg = Status_TG.objects.all()
    return render(request, 'lista_status_tg.html', {'status_tg':status_tg})

def crear_status_tg(request):
    form = Status_TGForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_status_tg')
    return render(request, 'status_tgForm.html', {'form_stg':form})

def modificar_status_tg(request,id):
    status_tg = Status_TG.objects.get(id=id)
    form = Status_TGForm(request.POST or None, instance=status_tg)
    if form.is_valid():
        form.save()
        return redirect('lista_status_tg')
    return render(request, 'status_tgForm.html', {'form_stg':form,'status_tg':status_tg})

def lista_tipo_persona(request):
    tipo_p = Tipo_Persona.objects.all()
    return render(request, 'lista_tipo_persona.html',{'tipo_p':tipo_p})

def crear_tipo_persona(request):
    form = TipoPersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_tipo_persona')
    return render(request,'tipo_personaForm.html',{'form_tp':form})

def modificar_tipo_persona(request, id):
    tipo_p = Tipo_Persona.objects.get(id=id)
    form = TipoPersonaForm(request.POST or None, instance=tipo_p)
    if form.is_valid():
        form.save()
        return redirect('lista_tipo_persona')
    return render(request,'tipo_personaForm.html',{'form_tp':form,'tipo_p':tipo_p})

def lista_persona(request):
    persona = Persona.objects.all().prefetch_related('TIPO_PERSONA')
    return render(request, 'lista_persona.html',{'persona':persona})

def lista_persona_ci(request):
    persona = Persona.objects.all().order_by('CI').prefetch_related('TIPO_PERSONA')
    return render(request, 'lista_persona.html',{'persona':persona})
    
def lista_persona_nombre(request):
    persona = Persona.objects.all().order_by('NOMBRES').prefetch_related('TIPO_PERSONA')
    return render(request, 'lista_persona.html',{'persona':persona})

def lista_persona_apellido(request):
    persona = Persona.objects.all().order_by('APELLIDOS').prefetch_related('TIPO_PERSONA')
    return render(request, 'lista_persona.html',{'persona':persona})

def crear_persona(request):
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_persona')
    return render(request,'personaForm.html', {'form_p':form})

def modificar_persona(request, id):
    persona = Persona.objects.get(id=id)
    form = PersonaForm(request.POST or None, instance=persona)
    if form.is_valid():
        form.save()
        return redirect('lista_persona')
    return render(request,'personaForm.html', {'form_p':form, 'persona':persona})

def lista_propuesta(request):
    propuesta = Propuesta.objects.all().prefetch_related('TERM','STATUS','ALUMNO1','ALUMNO2','TUTOR_A','TUTOR_E')
    return render(request,'lista_propuesta.html',{'propuesta':propuesta})

def crear_propuesta(request):
    form = PropuestaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_propuesta')
    return render(request, 'propuestaForm.html', {'form_p':form})

def modificar_propuesta(request, codigo):
    propuesta = Propuesta.objects.get(CODIGO=codigo)
    form = PropuestaForm(request.POST or None, instance =propuesta)
    if form.is_valid():
        form.save()
        return redirect('lista_propuesta')
    return render(request,'propuestaForm.html', {'form_p':form, 'propuesta':propuesta})

def lista_tg(request):
    tg = TG.objects.all().prefetch_related('TERM','STATUS','PROPUESTA').order_by('PROPUESTA')
    return render(request, 'lista_tg.html', {'tg':tg})

def crear_tg(request):
    form = TGForm(request.POST or None)
    if form.is_valid():
        tg = form.save(commit=False)
        tg.CODIGO = "TG"+str(tg.PROPUESTA.CODIGO)
        tg.save()
        return redirect('lista_tg')
    return render(request, 'tgForm.html',{'form_tg':form})

def modificar_tg(request, codigo):
    tg = TG.objects.get(CODIGO=codigo)
    form = TGForm(request.POST or None, instance=tg)
    if form.is_valid():
        tg = form.save(commit=False)
        tg.CODIGO = "TG"+str(tg.PROPUESTA.CODIGO)
        tg.save()
        return redirect('lista_tg')
    return render(request, 'tgForm.html',{'form_tg':form,'tg':tg})

def lista_defensa(request):
    defensa = Defensa.objects.all().prefetch_related('TG','JURADO1','JURADO2','JURADO_S')
    return render(request,'lista_defensa.html',{'defensa':defensa})

def crear_defensa(request):
    form = DefensaForm(request.POST or None)
    if form.is_valid():
        defensa = form.save(commit=False)
        defensa.CODIGO = "D"+str(defensa.TG.CODIGO)
        defensa.save()
        return redirect('lista_defensa')
    return render(request, 'defensaForm.html', {'form_d':form})

def modificar_defensa(request,codigo):
    defensa = Defensa.objects.get(CODIGO=codigo)
    form = DefensaForm(request.POST or None, instance=defensa)
    if form.is_valid():
        defensa = form.save(commit=False)
        defensa.CODIGO = "D"+str(defensa.TG.CODIGO)
        defensa.save()
        return redirect('lista_defensa')
    return render(request, 'defensaForm.html', {'form_d':form, 'defensa':defensa})
