from django.shortcuts import redirect, render
from .forms import PostForm
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
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            if request.user.is_authenticated:
                producto.autor = request.user
                producto.save()
                return redirect('pagina:posts')
            else:
                form.add_error(None, "Debes iniciar sesión para crear un producto.")
    else:
        form = PostForm()
    return render(request, 'post_create.html', context={'form': form})