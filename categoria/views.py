from django.shortcuts import render
from django.views.generic import TemplateView

from categoria.models import Categoria


class CategoriaTemplateView(TemplateView):
    """ Vista basada en clases para listar todos los autos """
    template_name = 'index_categoria.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
