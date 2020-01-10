from django.urls import path
from . import views
from django.shortcuts import render, redirect


urlpatterns = [
    path('', views.index, name='index'),
    path('lista_status_propuesta', views.lista_status_propuesta, name='lista_status_propuesta'),
    path('crear_status_propuesta', views.crear_status_propuesta, name='crear_status_propuesta'),
    path('modificar_status_propuesta/<int:id>/', views.modificar_status_propuesta, name="modificar_status_propuesta"),
    path('lista_term', views.lista_term, name='lista_term'),
    path('crear_term', views.crear_term, name='crear_term'),
    path('modificar_term/<int:id>/', views.modificar_term, name='modificar_term'),
    path('lista_status_tg', views.lista_status_tg, name='lista_status_tg'),
    path('crear_status_tg', views.crear_status_tg, name='crear_status_tg'),
    path('modificar_status_tg/<int:id>/', views.modificar_status_tg, name='modificar_status_tg'),
    path('lista_tipo_persona', views.lista_tipo_persona, name='lista_tipo_persona'),
    path('crear_tipo_persona', views.crear_tipo_persona, name='crear_tipo_persona'),
    path('modificar_tipo_persona/<int:id>/', views.modificar_tipo_persona, name='modificar_tipo_persona'),
    path('lista_persona', views.lista_persona, name='lista_persona'),
    path('lista_persona_ci', views.lista_persona_ci, name='lista_persona_ci'),
    path('lista_persona_nombre', views.lista_persona_nombre, name='lista_persona_nombre'),
    path('lista_persona_apellido', views.lista_persona_apellido, name='lista_persona_apellido'),
    path('crear_persona', views.crear_persona, name='crear_persona'),
    path('modificar_persona/<int:id>/', views.modificar_persona, name='modificar_persona'),
    path('lista_propuesta', views.lista_propuesta, name='lista_propuesta'),
    path('crear_propuesta', views.crear_propuesta, name='crear_propuesta'),
    path('modificar_propuesta/<int:codigo>/', views.modificar_propuesta, name='modificar_propuesta'),
    path('lista_tg', views.lista_tg, name='lista_tg'),
    path('crear_tg', views.crear_tg, name='crear_tg'),
    path('modificar_tg/<codigo>/', views.modificar_tg, name='modificar_tg'),
    path('lista_defensa', views.lista_defensa, name='lista_defensa'),
    path('crear_defensa', views.crear_defensa, name='crear_defensa'),
    path('modificar_defensa/<codigo>/', views.modificar_defensa, name='modificar_defensa')
    
]
