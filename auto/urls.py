from django.urls import path

from auto.views import AutoTemplateView, ListarFiatTemplateView, fucion_autos


urlpatterns = [
    path("", AutoTemplateView.as_view(), name="index"),
    path("listar_fiat", ListarFiatTemplateView.as_view(), name="listar_fiat"),
    path("funcion_autos", fucion_autos, name="funcion_autos")
]
