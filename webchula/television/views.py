from django.shortcuts import render
from television import models as md

def index(request):
    return render(request, "index.html")

def series(request):
    service = md.ServiceSeries()
    listaSeries = service.getSeries()
    informacion = {
        "listaseries":listaSeries
    }
    return render(request, "series.html", informacion)

def personajes(request):
    if('idserie' in request.GET):
        service = md.ServiceSeries()
        idserie = int(request.GET['idserie'])
        personajes = service.getPersonajeSerie(idserie)
        informacion = {
            "personajes":personajes
        }
        return render(request, "personajes.html", informacion)
    else:
        return render(request, "personajes.html")
    
def insertar(request):
    service = md.ServiceSeries()
    series = service.getSeries()
    if('cajanombre' in request.POST):
        nom = request.POST['cajanombre']
        img = request.POST['cajaimg']
        idserie = int(request.POST['cajaidserie'])
        service.insertarPersonaje(nom, img, idserie)
        informacion = {
            "series":series
        }
        return render(request, "insertar.html", informacion)
    else:
        informacion = {
            "series":series
        }
        return render(request, "insertar.html", informacion)

# Create your views here.
