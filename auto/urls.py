from django.urls import path

from auto.views import AutoTemplateView, ListarFiatTemplateView, fucion_autos

# localhost / 127.0.0.1
# localhost:8000/autos/
urlpatterns = [
    # localhost:8000/autos/
    path("", AutoTemplateView.as_view(), name="index"),
    # localhost:8000/autos/listar_fiat/
    path("listar_fiat", ListarFiatTemplateView.as_view(), name="listar_fiat"),
    # localhost:8000/autos/funcion_autos/
    path("funcion_autos", fucion_autos, name="funcion_autos")
]
