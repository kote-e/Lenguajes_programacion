# Proyecto Django - Guía de Inicio
## 1. Crear un entorno virtual

### Crear entorno virtual:

``` python -m venv venv ```

### Activar entorno virtual
Windows (CMD)
``` venv\Scripts\activate ```
Windows (PowerShell)
``` .\venv\Scripts\Activate.ps1```

### Desactivar entorno virtual
``` deactivate ```

## 2. Instalar Django
``` pip install django ```

### Verificar instalación:

``` django-admin --version ```

### Guardar dependencias:

``` pip freeze > requirements.txt``` 

### Instalar dependencias desde requirements.txt:

```pip install -r requirements.txt ```
## 3. Crear un proyecto Django
```django-admin startproject proyecto . ```

**¿Para qué sirve?:** 

Crea la estructura principal del proyecto Django.

## 4. Ejecutar el servidor de desarrollo
``` python manage.py runserver 0.0.0.0:8000 ```

**¿Para qué sirve?**

Inicia el servidor local de Django en el puerto 8000.

## 5. Crear una aplicación
``` python manage.py startapp logica ```

**¿Para qué sirve?**

Crea una aplicación llamada "logica" dentro del proyecto.

Luego debe agregarse en INSTALLED_APPS dentro de settings.py.

INSTALLED_APPS = [
    ...
    'logica',
]
## 6. Crear migraciones
``` python manage.py makemigrations ```

**¿Para qué sirve?**

Genera archivos de migración a partir de los modelos definidos en models.py.

## 7. Aplicar migraciones
``` python manage.py migrate ```

**¿Para qué sirve?**

Aplica las migraciones a la base de datos y crea/modifica las tablas necesarias.

## 8. Ver migraciones pendientes
``` python manage.py showmigrations ```

**¿Para qué sirve?**

Muestra todas las migraciones y cuáles han sido aplicadas.

## 9. Crear un superusuario
``` python manage.py createsuperuser ```

**¿Para qué sirve?**

Crea un usuario administrador para acceder al panel de administración.

## 10. Acceder al panel de administración

### Una vez ejecutado el servidor:

``` http://localhost:8000/admin ```

Ingresar con las credenciales del superusuario.

## 11. Abrir la consola interactiva de Django
``` python manage.py shell ```

**¿Para qué sirve?**

Permite ejecutar código Python utilizando los modelos y configuraciones del proyecto.

## 12. Recolectar archivos estáticos (Producción)
``` python manage.py collectstatic ```

**¿Para qué sirve?**

Reúne todos los archivos estáticos (CSS, JS, imágenes) en una sola carpeta para despliegue.

## 13. Verificar errores de configuración
``` python manage.py check```

**¿Para qué sirve?**

Revisa posibles errores en la configuración del proyecto.

## 14. Generar requirements.txt actualizado
``` pip freeze > requirements.txt ```

**¿Para qué sirve?**

Guarda todas las dependencias instaladas para que otros desarrolladores puedan replicar el entorno.

## Flujo típico de trabajo
### Primera vez que clono el proyecto
``` git clone <repositorio> ```
```cd <repositorio>```

```python -m venv venv```

# Activar entorno virtual
``` venv\Scripts\activate```

``` pip install -r requirements.txt```

``` python manage.py migrate```

``` python manage.py runserver 0.0.0.0:8000```

**Cuando agrego o modifico modelos:**
```python manage.py makemigrations```

``` python manage.py migrate```


**Cuando instalo una nueva librería:**
```pip install nombre_paquete```

``` pip freeze > requirements.txt```
**Estructura básica**
proyecto/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── proyecto/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── logica/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    └── migrations/