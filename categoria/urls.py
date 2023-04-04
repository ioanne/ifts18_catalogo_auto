from django.urls import path


from categoria.views import CategoriaTemplateView

urlpatterns = [
    path("", CategoriaTemplateView.as_view(), name="index_categoria"),
]
