from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    dataNascimento = models.DateField()

    def __str__(self):
        return "{}".format(self.nome)

class Consulta(models.Model):
    dataConsulta = models.DateField()
    horarioConsulta = models.TimeField()
    hospital = models.CharField(max_length=50)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    acompanhante = models.BooleanField()
    observacao = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.paciente.nome, self.dataConsulta)
