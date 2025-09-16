from django.shortcuts import render

# from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hola, Alejo! Esta es la primera APP")
    return render(request, 'home.html')
