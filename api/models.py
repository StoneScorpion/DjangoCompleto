from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    lastname = models.CharField(max_length=50, verbose_name='Apellidos')
    phone = models.CharField(max_length=10, verbose_name='Teléfono')
    birthday = models.CharField(max_length=11, verbose_name='Fecha de Nacimiento')

    def __str__(self):
        return "Paciente: {0} {1}".format(self.name, self.lastname)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"


class Medicine(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    amount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Cantidad', default=0)
    laboratory = models.CharField(max_length=50, verbose_name='Laboratorio')
    expiration = models.CharField(max_length=10, verbose_name='Caducidad')

    def __str__(self):
        return "Medicina: {0} {1}".format(self.name, self.laboratory)

    class Meta:
        verbose_name = "Medicina"
        verbose_name_plural = "Medicinas"


class Service(models.Model):
    name = models.CharField(max_length=50, verbose_name='Servicio')
    laboratory = models.CharField(max_length=50, verbose_name='Áreas')
    description = models.CharField(max_length=200, verbose_name='Descripción')
    photo = models.ImageField(verbose_name='Agregar Foto', null=True, upload_to='imgServicios')

    def __str__(self):
        return "Servicio: {0} {1}".format(self.name, self.laboratory)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
