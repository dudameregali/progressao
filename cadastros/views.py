from django.views.generic.edit import CreateView, UpdateView

from .models import Paciente, Consulta

from django.urls import reverse_lazy

class PacienteCreate(CreateView):
    model = Paciente
    fields = ['nome', 'dataNascimento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ConsultaCreate(CreateView):
    model = Consulta
    fields = ['dataConsulta', 'horarioConsulta', 'hospital', 'paciente', 'acompanhante', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

# class PacienteUpdate(UpdateView):
#     model = Paciente
#     fields = ['nome', 'dataNascimento']
#     template_name = 'cadastros/form.html'
#     success_url = reverse_lazy('index')

# class ConsultaUpdate(UpdateView):
#     model = Consulta
#     fields = ['dataConsulta', 'horarioConsulta', 'hospital', 'paciente', 'acompanhante', 'observacao']
#     template_name = 'cadastros/form.html'
#     success_url = reverse_lazy('index')