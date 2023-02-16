from django.urls import path
from .views import PacienteCreate, ConsultaCreate
from .views import PacienteUpdate, ConsultaUpdate
from .views import PacienteDelete, ConsultaDelete

urlpatterns = [
    path('cadastrar/paciente', PacienteCreate.as_view(), name="cadastrar-paciente"),
    path('cadastrar/consulta', ConsultaCreate.as_view(), name="cadastrar-consulta"),

    path('editar/paciente/<int:pk>', PacienteUpdate.as_view(), name="editar-paciente"),
    path('editar/consulta/<int:pk>', ConsultaUpdate.as_view(), name="editar-consulta"),

    path('excluir/paciente/<int:pk>', PacienteDelete.as_view(), name="excluir-paciente"),
    path('excluir/consulta/<int:pk>', ConsultaDelete.as_view(), name="excluir-consulta"),
]