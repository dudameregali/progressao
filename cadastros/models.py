from django.db import models

# Create your models here.

class Pasciente(models.Model):
    nome = models.CharField(max_length=50)
    dataNascimento = models.DateField()

    def __str__(self) -> str:
        return super().__str__()

class Consulta(models.Model):
    dataConsulta = models.DateField()
    horarioConsulta = models.TimeField()
    hospital = models.CharField(max_length=50)
    paciente = models.ForeignKey(Pasciente, on_delete=models.PROTECT)
    acompanhante = models.BooleanField()
    observacao = models.CharField(max_length=255)

    def __str__(self) -> str:
        return super().__str__()
        