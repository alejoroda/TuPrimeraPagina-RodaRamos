from django.urls import path, include
from pagina import views
from django.contrib import admin
app_name = "pagina"
urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('posts/', views.posts, name="posts"),
    path('posts/create/', views.post_create, name="post_create"),
    path('', include('django.contrib.auth.urls')),
]
