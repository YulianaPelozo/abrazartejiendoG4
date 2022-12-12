from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return render(request, 'index.html', {})

def info(request):
    return HttpResponse("<h1>Información acerca de nosotros: </h1>")

def index(request):
    return render(request, 'index1.html', {})