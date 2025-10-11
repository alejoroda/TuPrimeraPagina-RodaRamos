from django.urls import path, include
from pagina import views
from django.contrib import admin
app_name = "pagina"
urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('about/', views.about, name="about"),
    path('perfil/', views.perfil, name='perfil'),
    path('pages/', views.pages, name="pages"),
    path('pages/create/', views.post_create, name="post_create"),
    path('producto/<int:pk>/', views.producto_detail, name='producto_detail'),
    path('producto/<int:id>/editar/', views.producto_editar, name='producto_editar'),
    path('producto/<int:id>/eliminar/', views.producto_eliminar, name='producto_eliminar'),
    path('comentario/<int:pk>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
    path('respuesta/<int:pk>/eliminar/', views.eliminar_respuesta, name='eliminar_respuesta'),
    path('', include('django.contrib.auth.urls')),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('productos-cbv/', views.ProductoListView.as_view(), name='productos_cbv'),
]
