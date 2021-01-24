from django.conf.urls import url
from biblio import views
from django.urls import path

urlpatterns = [

    #ROUTES VERS LES LIVRES

    url('biblio/livres$', views.livre_list), #route vers tous les livres
    url('biblio/livres/(?P<pk>[0-9]+)$', views.livre_detail), #Route vers un livre en fct de l'id


    #ROUTES VERS LES CATEGORIES

    url('biblio/categories$', views.categorie_list), #Route vers une catégorie en fct de l'id
    url('biblio/categories/(?P<pk>[0-9]+)$', views.categorie_detail), #Route vers une catégorie en fct de l'id

    #Routes vers les pages auth0
    path('api/public', views.public),
    path('api/private', views.private),
    path('api/private-scoped', views.private_scoped),
]