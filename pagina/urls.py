from django.urls import path
from pagina import views
app_name = "pagina"
urlpatterns = [
    path('', views.home, name="home"),
]
