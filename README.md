# TuPrimeraPagina-RodaRamos
# MiProyectoDjango

Aplicación web desarrollada con **Django** que permite gestionar productos y registrar usuarios.  
Incluye autenticación de usuarios, formularios con Bootstrap 4 y administración de productos.

---

## Características

- Registro e inicio de sesión de usuarios.  
- Creación, edición y eliminación de productos.  
- Formularios estilizados con **django-crispy-forms** y **Bootstrap 4**.  
- Panel de administración de Django.  
- Implementación siguiendo el patrón **MVT (Model - View - Template)**.

---

## Instalación

```bash
git clone https://github.com/TU-USUARIO/TU-REPO.git
cd TU-REPO
### Crear y activar un entorno virtual
python -m venv venv
# En Windows
venv\Scripts\activate
# En Linux/Mac
source venv/bin/activate
pip install -r requirements.txt
python manage.py createsuperuser
python manage.py runserver
acceder a: http://localhost:8000/
```

## Estructura
```
MiProyectoDjango/
│── MiProyectoDjango/
│   │── __init__.py
│   │── asgi.py
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│
│── pagina/
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── forms.py
│   │── models.py
│   │── tests.py
│   │── urls.py
│   │── views.py
│   │
│   └── migrations/
│       │── __init__.py
│       │── 0001_initial.py
│       │── 0002_categoria_prod....py
│
│── templates/
│   │── base.html
│   │── home.html
│   │── post_create.html
│   │── posts.html
│   │── register.html
│   │
│   └── registration/
│       │── logged_out.html
│       │── login.html
│
│── db.sqlite3
│── manage.py
│── .gitignore
│── pyvenv.cfg```
