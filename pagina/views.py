from django.shortcuts import redirect, render
from .forms import PostForm, ComentarioForm  # <--- añade ComentarioForm aquí
from .models import Producto, Perfil, Comentario, Respuesta
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Producto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserForm, PerfilForm
from django.contrib import messages


def home(request):
    productos = Producto.objects.order_by('-fechapublicacion')[:8]  # últimos 8 productos
    return render(request, 'home.html', {'productos': productos})
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect ("pagina:pages")
    else:
            form = RegisterForm()
    return render(response, 'register.html', {"form": form})
def about(request):
    return render(request, 'about.html')
def pages(request):
    productos = Producto.objects.all()
    query = request.GET.get('q') if request.user.is_authenticated else None
    categoria = request.GET.get('categoria') if request.user.is_authenticated else None
    if query:
        productos = productos.filter(nombre__icontains=query)
    if categoria and categoria != '':
        productos = productos.filter(categoria__categoria__icontains=categoria)
    categorias = ["Comedor", "Sillones y Sillas", "Decoración de Interior", "Baño", "Iluminación", "Cortinas", "Oficina", "Otros"]
    return render(request, 'pages.html', {'productos': productos, 'query': query, 'categoria': categoria, 'categorias': categorias})
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            if request.user.is_authenticated:
                producto.autor = request.user
                producto.save()
                return redirect('pagina:producto_detail', pk=producto.id)  # <--- usa pk
            else:
                form.add_error(None, "Debes iniciar sesión para crear un producto.")
    else:
        form = PostForm()
    return render(request, 'post_create.html', context={'form': form})

def perfil(request):
    return render(request, 'perfil.html')
from django.shortcuts import get_object_or_404
from .models import Comentario

def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    comentarios = producto.comentarios.all().order_by('-fecha')
    form = ComentarioForm()  # Siempre inicializa el formulario

    if request.method == 'POST':
        if 'comentario' in request.POST:
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.producto = producto
                comentario.autor = request.user
                comentario.save()
                return redirect('pagina:producto_detail', pk=producto.pk)
        elif 'respuesta_btn' in request.POST:
            comentario_id = request.POST.get('comentario_id')
            respuesta_texto = request.POST.get('respuesta')
            comentario = Comentario.objects.get(id=comentario_id)
            Respuesta.objects.create(
                comentario=comentario,
                autor=request.user,
                texto=respuesta_texto
            )
            return redirect('pagina:producto_detail', pk=producto.pk)
        # Si ninguna condición se cumple, form sigue inicializado

    return render(request, 'producto_detail.html', {
        'producto': producto,
        'comentarios': comentarios,
        'form': form,
    })
@login_required
def producto_editar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.user != producto.autor and not request.user.is_superuser:
        raise PermissionDenied("No tienes permiso para editar este producto.")
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('pagina:producto_detail', id=producto.id)
    else:
        form = PostForm(instance=producto)
    return render(request, 'producto_editar.html', {'form': form, 'producto': producto})

@login_required
def editar_perfil(request):
    user = request.user
    perfil, _ = Perfil.objects.get_or_create(user=user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)
        password_form = PasswordChangeForm(user, request.POST)
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            if password_form.is_valid() and request.POST.get('old_password'):
                password_form.save()
                update_session_auth_hash(request, user)  # Mantiene la sesión activa
            return redirect('pagina:perfil')
    else:
        user_form = UserForm(instance=user)
        perfil_form = PerfilForm(instance=perfil)
        password_form = PasswordChangeForm(user)
    return render(request, 'editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form,
        'password_form': password_form,
    })

class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'pages.html'
    context_object_name = 'productos'

@login_required
def producto_eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.user != producto.autor and not request.user.is_superuser:
        raise PermissionDenied("No tienes permiso para eliminar este producto.")
    if request.method == 'POST':
        producto.delete()
        return redirect('pagina:pages')
    return render(request, 'producto_confirmar_eliminar.html', {'producto': producto})

def eliminar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    producto = comentario.producto
    if request.user == producto.autor or request.user.is_superuser:
        comentario.delete()
        messages.success(request, "Comentario eliminado.")
    return redirect('pagina:producto_detail', pk=producto.pk)

def eliminar_respuesta(request, pk):
    respuesta = get_object_or_404(Respuesta, pk=pk)
    comentario = respuesta.comentario
    producto = comentario.producto
    if request.user == producto.autor or request.user.is_superuser:
        respuesta.delete()
        messages.success(request, "Respuesta eliminada.")
    return redirect('pagina:producto_detail', pk=producto.pk)