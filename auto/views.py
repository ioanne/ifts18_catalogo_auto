from django.shortcuts import render
from django.views.generic import TemplateView

from auto.models import Auto


class AutoTemplateView(TemplateView):
    """ Vista basada en clases para listar todos los autos """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autos'] = Auto.objects.all()
        return context


class ListarFiatTemplateView(TemplateView):
    """ Vista basada en clases para listar los autos de la marca Fiat """
    template_name = 'fiat_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autos'] = Auto.objects.filter(marca__nombre="Fiat")
        return context


def fucion_autos(request):
    """ Lista basada en funciones para listar todos los autos """
    return render(request, 'index.html', {
        'autos': Auto.objects.all(),
    })
