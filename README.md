# agregame la news

## 📝 Descripción

Este proyecto es una aplicación web desarrollada con Django. Está diseñada para compartir artículos de blogs y mantener a los visitantes actualizados con las últimas noticias.

## 🚀 Características Generales
- **Api**: Api para obtener datos de la aplicación.
- **Blog**: Sistema de gestión de contenidos para artículos.
- **Noticias**: Sección para publicar y mostrar noticias actualizadas.
- **Administración**: Panel de administración de Django para gestionar contenidos.

##  🚀🚀 Características Extras
- **Modo Oscuro/Claro**: Implementación de un modo oscuro para una experiencia de usuario más cómoda en condiciones de poca luz.
- **Responsive Design**: Diseño adaptable para dispositivos móviles y tabletas.
- **Multilenguaje**: Soporte para español como idioma principal.
- **Seguridad**: Configuraciones de seguridad para producción.
- **Logging**: Sistema de registro de errores.
- **Caché**: Implementación de caché local o Redis para mejorar el rendimiento.
## 🛠 Tecnologías Utilizadas

- Python 3.13
- Django 5.1.2
- Bootstrap 5.3
- SQLite (base de datos por defecto, puedes seleccionar POSTGRESQL)
- HTML5
- CSS3
- JavaScript

## 📋 Prerrequisitos

- Python 3.13
- pip (gestor de paquetes de Python)

## 🔧 Instalación

1. Clona el repositorio:
```
git clone https://github.com/llopgui/agregamela.news.git
cd agregamela.news
```

2. Crea y activa un entorno virtual:

##### En Linux o macOS
```
python3 -m venv venv 
source venv/bin/activate
```

##### En Windows
```
python -m venv venv 
source venv/Scripts/activate
```

3. Instala las dependencias:

##### En Linux o macOS
```
pip install -r requirements.txt
```

##### En Windows (si tienes problemas con pip, intenta con pip3)
```
pip3 install -r requirements.txt
```

1. Copia el archivo `.env.example` y renombralo a `.env`, luego configura las variables de entorno a tus necesidades.

2. Realiza las migraciones:
```
python manage.py makemigrations
python manage.py migrate
```

1. Crea un superusuario:
```
python manage.py createsuperuser
```

## 🚀 Uso

1. Inicia el servidor de desarrollo:
```
python manage.py runserver
```

2. Abre tu navegador y visita [http://localhost:8000](http://localhost:8000)

3. Para acceder al panel de administración, visita [http://localhost:8000/admin](http://localhost:8000/admin) e ingresa con las credenciales del superusuario.

## 📁 Estructura del Proyecto

- `api/`: Aplicación para la api.
- `blog/`: Aplicación para el sistema de blog.
- `portal/`: Aplicación para la sección de noticias.
- `templates/`: Plantillas HTML compartidas.
- `static/`: Archivos estáticos (CSS, JavaScript, imágenes).
- `media/`: Archivos subidos por los usuarios.
- `agregamela_news/`: Configuraciones principales del proyecto.

## ⚙️ Configuración

- El archivo `settings.py` contiene todas las configuraciones del proyecto.
- Las variables de entorno se cargan desde el archivo `.env`.
- La depuración está activada por defecto en desarrollo.
- Se utiliza SQLite como base de datos por defecto durante el desarrollo.

## 🔐 Seguridad

- Configuraciones de seguridad comentadas para producción en `settings.py`.
- Se recomienda activar estas configuraciones al desplegar en un entorno de producción.

## 📧 Configuración de Correo Electrónico

- La configuración de correo electrónico está comentada en `settings.py`.
- Descomenta y configura las variables de entorno correspondientes para activar el envío de correos durante el desarrollo.

## 🔍 Logging

- Los errores se registran en el archivo `logs/django_error.log`.

## 💾 Caché

- Se utiliza caché en memoria local para mejorar el rendimiento, se puede activar Redis durante el desarrollo.

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue o realiza un pull request con tus sugerencias.

## 📄 Licencia

Este proyecto está bajo la Licencia CC BY-NC-SA. Ver el archivo `LICENSE` para más detalles.
