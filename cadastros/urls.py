from django.urls import path
from .views import PacienteCreate, ConsultaCreate

urlpatterns = [
    path('cadastrar/paciente', PacienteCreate.as_view(), name="cadastrar-paciente"),
    path('cadastrar/consulta', ConsultaCreate.as_view(), name="cadastrar-consulta"),
]