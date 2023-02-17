from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Paciente, Consulta

from django.urls import reverse_lazy

#### Inclusão ####

class PacienteCreate(CreateView):
    model = Paciente
    fields = ['nome', 'dataNascimento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-paciente')

class ConsultaCreate(CreateView):
    model = Consulta
    fields = ['dataConsulta', 'horarioConsulta', 'hospital', 'paciente', 'acompanhante', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-consulta')

#### Alteração ####

class PacienteUpdate(UpdateView):
    model = Paciente
    fields = ['nome', 'dataNascimento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-paciente')

class ConsultaUpdate(UpdateView):
    model = Consulta
    fields = ['dataConsulta', 'horarioConsulta', 'hospital', 'paciente', 'acompanhante', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-consulta')

#### Apagar ####

class PacienteDelete(DeleteView):
    model = Paciente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-paciente')

class ConsultaDelete(DeleteView):
    model = Consulta
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-consulta')

#### Listar ####

class PacienteList(ListView):
    model = Paciente
    template_name = 'cadastros/listas/paciente.html'

class ConsultaList(ListView):
    model = Consulta
    template_name = 'cadastros/listas/consulta.html'