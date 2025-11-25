from .models import Visita
from django.db import ProgrammingError, OperationalError


class VisitaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        respuesta = self.get_response(request)
        ruta = request.path
        if not ruta.startswith(("/static/", "/media/", "/admin/")):
            try:
                Visita.objects.create(pagina=ruta)
            except (ProgrammingError, OperationalError):
                # Si las migraciones no se han aplicado aún (p.ej. despliegue nuevo), evitamos romper la app.
                pass
        return respuesta
