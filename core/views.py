from django.shortcuts import render
from .forms import ContactForm


from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def portfolio(request):
    return render(request, "core/portfolio.html")

def contact(request):
    return render(request, "core/contact.html")

from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    mensaje_enviado = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            mensaje_enviado = True
            form = ContactForm() 
    else:
        form = ContactForm()

    return render(request, "core/contact.html", {
        "form": form,
        "mensaje_enviado": mensaje_enviado
    })
