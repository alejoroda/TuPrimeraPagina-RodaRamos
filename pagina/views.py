from django.shortcuts import render

# from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hola, Alejo! Esta es la primera APP")
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def posts(request):
    return render(request, 'posts.html')