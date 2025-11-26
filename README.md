# Parcial Django - Prácticas completas

Proyecto Django que reúne 11 prácticas (login, CRUDs, media, PDF, email, carrito en sesión, API REST con DRF/Swagger, scraping, dashboard con Chart.js, deploy en Render).

## Requisitos
- Python 3.10+
- pip
- (Opcional) virtualenv

## Instalación local
```bash
python -m venv .venv
.\.venv\Scripts\activate  # en Windows (PowerShell)
# source .venv/bin/activate  # en Linux/Mac
pip install -r requirements.txt
```

### Variables de entorno
Crear `.env` en la raíz (ya hay uno de ejemplo):
```
SECRET_KEY=pon_un_valor_seguro
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_app_password
DEFAULT_FROM_EMAIL=tu_email@gmail.com
# Brevo (si usas API en vez de SMTP)
BREVO_API_KEY=tu_api_key_de_brevo
BREVO_SENDER_EMAIL=remitente@tu_dominio.com
BREVO_SENDER_NAME=Parcial Django
```

## Migraciones y datos
```bash
python manage.py migrate
python manage.py createsuperuser  # opcional
```

## Ejecutar en desarrollo
```bash
python manage.py runserver
```
Visita `http://127.0.0.1:8000/`.

## Rutas principales (resumen por práctica)
1. **Auth básica**: `/registro/`, `/login/`, `/logout/`, `/panel/` (protegido).
2. **CRUD FBV Tareas**: `/tareas/`, `/tareas/crear/`, `/tareas/<id>/editar/`, `/tareas/<id>/borrar/`.
3. **CRUD CBV Tareas**: `/tareas_cbv/` + crear/editar/borrar/detalle.
4. **Galería (media)**: `/galeria/`, `/galeria/subir/` (ImageField).
5. **PDF (ReportLab)**: `/reportes/`, botón “Descargar PDF”.
6. **Contacto (email)**: `/contacto/` envía a `EMAIL_HOST_USER`.
7. **Carrito en sesión**: `/productos/`, `/carrito/`, agregar/quitar; admins pueden crear productos en `/productos/nuevo/`.
8. **API REST DRF**: `/api/libros/`, `/api/libros/<id>/`; Swagger en `/swagger/`.
9. **Scraper**: `/scraper/?q=algo` (Wikipedia con requests + BeautifulSoup).
10. **Dashboard/Chart.js**: `/estadisticas/` (registra visitas vía middleware).
11. **Deploy**: preparado para Render con `gunicorn`, `dj-database-url`, `render.yaml`.

## Admin
- `/admin/` (usa los estáticos estándar). Crear superusuario si no existe.

## Email
- Por defecto consola. Para SMTP real (ej. Gmail) cambia en `.env`:
  - `EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend`
  - Usa App Password (sin espacios) en `EMAIL_HOST_PASSWORD`.

## Deploy en Render (Blueprint o manual)
- `render.yaml` incluido.
- Comando de build (si se configura manual):
  ```bash
  pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate --noinput
  ```
- Start: `gunicorn parcial.wsgi:application`
- Variables en Render:
  - `DATABASE_URL` (Postgres)
  - `SECRET_KEY`
  - `ALLOWED_HOSTS` (tu dominio `.onrender.com`)
  - `DEBUG=False`
  - (opcional) email y superusuario (`DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_PASSWORD` si quieres crearlo en build).
- Nota media: el filesystem de Render es efímero; las imágenes subidas a `media/` se perderán en redeploy. Para producción real usar S3/Cloudinary.

## Notas de codificación
- `STATIC_URL=/static/`, `STATIC_ROOT=staticfiles` (no versionado).
- `MEDIA_URL=/media/`, `MEDIA_ROOT=media` (no versionado).
- Middleware `VisitaMiddleware` ignora fallas si la tabla aún no existe (evita 500 antes de migrar).

## Pruebas rápidas
- CRUD FBV/CBV: crear/editar/borrar tareas.
- Galería: subir imagen y ver en `/galeria/`.
- Reportes: crear y descargar PDF.
- Contacto: enviar formulario (con backend de consola o SMTP real).
- Carrito: agregar productos, ver totales, crear producto si eres admin.
- API: usar `/swagger/` para GET/POST/PUT/PATCH/DELETE de libros.
- Scraper: `/scraper/?q=Django` (usa User-Agent para evitar 403).
- Dashboard: navegar el sitio y luego `/estadisticas/` para ver gráficos.
