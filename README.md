# TuPrimeraPagina-RodaRamos
# MiProyectoDjango

Aplicación web desarrollada con **Django** que permite gestionar productos y registrar usuarios.  
Incluye autenticación de usuarios, formularios modernos con Bootstrap, comentarios y respuestas, imágenes por defecto y administración de productos.

---

## Características

- Registro e inicio de sesión de usuarios.
- Creación, edición y eliminación de productos (inmuebles).
- Imagen por defecto para productos y perfiles si el usuario no sube una.
- Comentarios y respuestas en los detalles de cada producto.
- Solo el autor del producto o el admin puede eliminar comentarios y respuestas.
- Búsqueda y filtrado de productos por nombre y categoría.
- Diseño moderno, monocromático y responsivo con Bootstrap.
- Página de perfil de usuario con edición y foto.
- Página "About Us" estilizada y con logo.
- Panel de administración de Django.
- Implementación siguiendo el patrón **MVT (Model - View - Template)**.

---

## Instalación

```bash
git clone https://github.com/TU-USUARIO/TU-REPO.git
cd TU-REPO
# Crear y activar un entorno virtual
python -m venv venv
# En Windows
venv\Scripts\activate
# En Linux/Mac
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
# Acceder a: http://localhost:8000/
```

## Estructura
```
MiProyectoDjango/
│
├── MiProyectoDjango/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── pagina/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
│       └── ...
│
├── static/
│   └── img/
│       ├── profilepage.webp
│       ├── defaultpost.jpg
│       ├── logo.webp
│       └── bannerpage.jpg
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── post_create.html
│   ├── posts.html
│   ├── producto_detail.html
│   ├── perfil.html
│   ├── about.html
│   ├── register.html
│   ├── ...
│   └── registration/
│       ├── logged_out.html
│       ├── login.html
│
├── db.sqlite3
├── manage.py
├── .gitignore
├── requirements.txt
└── [README.md](http://_vscodecontentref_/1)
```
