from django.urls import path

from . import views

urlpatterns = [ #path aponta para a classe index dentro de views e isso se chamará index.
    path('', views.index, name='index'),
]