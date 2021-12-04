from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import *
from api.models import *


# Create your views here.
class IndexView(TemplateView):
    model = Medic, Service
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Medicos'
        context['title'] = 'Servicios'
        context['listMedicos'] = Medic.objects.all()
        context['listServicios'] = Service.objects.all()
        return context
