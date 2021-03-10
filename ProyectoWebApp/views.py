from django.shortcuts import render, HttpResponse

# Create your views here.


def home(req):
    return HttpResponse("Inicio")


def servicios(req):
    return HttpResponse("Servicios")

def tienda(req):
    return HttpResponse("Inicio")

def blog(req):
    return HttpResponse("Inicio")

def contacto(req):
    return HttpResponse("Contacto")
