from django.shortcuts import render
from .models import Proyecto

def portfolio(request):
    proyectos = Proyecto.objects.all()
    return render(request, "portfolio/portfolio.html", {"proyectos": proyectos})
