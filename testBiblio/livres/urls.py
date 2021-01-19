from django.conf.urls import url
from livres import views

urlpatterns = [
    #Route vers tous les livres
    url('livres$', views.livre_list),
    #Route vers un livre en fct de l'id
    url('livres/(?P<pk>[0-9]+)$', views.livre_detail)
]