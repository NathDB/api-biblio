from django.conf.urls import url
from api import views

urlpatterns = [
    #Route vers tous les livres
    url('^api/api$', views.api_list),
    #Route vers un livre en fct de l'id
    url('^api/api/(?P<pk>[0-9]+)$', views.api_detail)
]