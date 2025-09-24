from django.shortcuts import render

from .models import Producto

# from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hola, Alejo! Esta es la primera APP")
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def posts(request):
    productos = Producto.objects.all()
    return render(request, 'posts.html', {'productos': productos})
def post_create(request):
    return render(request, 'post_create.html')