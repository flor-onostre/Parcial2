from django.urls import path
from . import views

urlpatterns = [
    path("tareas_cbv/", views.TareaListView.as_view(), name="tareas_cbv_lista"),
    path("tareas_cbv/crear/", views.TareaCreateView.as_view(), name="tareas_cbv_crear"),
    path("tareas_cbv/<int:pk>/", views.TareaDetailView.as_view(), name="tareas_cbv_detalle"),
    path("tareas_cbv/<int:pk>/editar/", views.TareaUpdateView.as_view(), name="tareas_cbv_editar"),
    path("tareas_cbv/<int:pk>/borrar/", views.TareaDeleteView.as_view(), name="tareas_cbv_borrar"),
]
