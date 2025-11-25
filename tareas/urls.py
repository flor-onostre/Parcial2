from django.urls import path
from . import views

urlpatterns = [
    path("tareas/", views.lista_tareas, name="tareas_lista"),
    path("tareas/crear/", views.crear_tarea, name="tareas_crear"),
    path("tareas/<int:pk>/editar/", views.editar_tarea, name="tareas_editar"),
    path("tareas/<int:pk>/borrar/", views.borrar_tarea, name="tareas_borrar"),
]
