from .models import Visita


class VisitaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        respuesta = self.get_response(request)
        ruta = request.path
        if not ruta.startswith(("/static/", "/media/", "/admin/")):
            Visita.objects.create(pagina=ruta)
        return respuesta
