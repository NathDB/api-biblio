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

    #ROUTES VERS LES LISTES

    url('biblio/listes$', views.liste_list),
    url('biblio/listes/(?P<pk>[0-9]+)$', views.liste_detail),

    #ROUTES VERS LES LIVRES_SUGGERES

    url('biblio/livres_sugg$', views.livre_sugg_list),
    url('biblio/livres_sugg/(?P<pk>[0-9]+)$', views.livre_sugg_detail),

    #url('biblio/update_profil/(?P<pk>[0-9]+)$', views.update_profile),

    #ROUTES VERS LES LIVRES_SUGGERES

    url('biblio/livres_sugg$', views.livre_sugg_list),
    url('biblio/livres_sugg/(?P<pk>[0-9]+)$', views.livre_sugg_detail),

]