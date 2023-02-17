from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Paciente, Consulta

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

#### Inclusão ####

class PacienteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Paciente
    fields = ['nome', 'dataNascimento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-paciente')

class ConsultaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Consulta
    fields = ['dataConsulta', 'horarioConsulta', 'hospital', 'paciente', 'acompanhante', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-consulta')

#### Alteração ####

class PacienteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Paciente
    fields = ['nome', 'dataNascimento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-paciente')

class ConsultaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Consulta
    fields = ['dataConsulta', 'horarioConsulta', 'hospital', 'paciente', 'acompanhante', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-consulta')

#### Apagar ####

class PacienteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Paciente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-paciente')

class ConsultaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Consulta
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-consulta')

#### Listar ####

class PacienteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Paciente
    template_name = 'cadastros/listas/paciente.html'

class ConsultaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Consulta
    template_name = 'cadastros/listas/consulta.html'