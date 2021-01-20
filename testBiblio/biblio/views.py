from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from biblio.models import Livre
from biblio.models import Categorie
from biblio.serializers import LivreSerializer
from biblio.serializers import CategorieSerializer
from rest_framework.decorators import api_view

#CRUD LIVRES
@api_view(['GET', 'POST', 'DELETE'])
def livre_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    #Pour récup un objet avec une condition
    if request.method == 'GET':
        livres = Livre.objects.all()

        titre = request.GET.get('titre', None)
        if titre is not None:
            livres = livres.filter(titre__icontains=titre)

        livres_serializer = LivreSerializer(livres, many=True)
        return JsonResponse(livres_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    #Pour créer un nouvel objet
    elif request.method == 'POST':
        livre_data = JSONParser().parse(request)
        livre_serializer = LivreSerializer(data=livre_data)
        if livre_serializer.is_valid():
            livre_serializer.save()
            return JsonResponse(livre_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(livre_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def livre_detail(request, pk):
    # find livre by pk (id)
    try:
        livre = Livre.objects.get(pk=pk)
    except Livre.DoesNotExist:
        return JsonResponse({'message': 'Ce livre n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

    #recup un seul objet en fonction de son id
    if request.method == 'GET':
        livre_serializer = LivreSerializer(livre)
        return JsonResponse(livre_serializer.data)

    elif request.method == 'PUT':
        livre_data = JSONParser().parse(request)
        livre_serializer = LivreSerializer(livre, data=livre_data)
        if livre_serializer.is_valid():
            livre_serializer.save()
            return JsonResponse(livre_serializer.data)
        return JsonResponse(livre_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Supprimer un objet
    elif request.method == 'DELETE':
        supp = Livre.objects.get(pk=pk)
        supp.delete()
        return JsonResponse({'message': '{} La livre a bien été supprimé !'.format(supp)}, status=status.HTTP_204_NO_CONTENT)

#CRUD CATEGORIES
@api_view(['GET', 'POST', 'DELETE'])
def categorie_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    #Pour récup un objet avec une condition
    if request.method == 'GET':
        categories = Categorie.objects.all()

        intitule = request.GET.get('intitule', None)
        if intitule is not None:
            categories = categories.filter(intitule__icontains=intitule)

        categories_serializer = CategorieSerializer(categories, many=True)
        return JsonResponse(categories_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    #Pour créer un nouvel objet
    elif request.method == 'POST':
        categorie_data = JSONParser().parse(request)
        categorie_serializer = CategorieSerializer(data=categorie_data)
        if categorie_serializer.is_valid():
            categorie_serializer.save()
            return JsonResponse(categorie_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(categorie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def categorie_detail(request, pk):
    # find categorie by pk (id)
    try:
        categorie = Categorie.objects.get(pk=pk)
    except Categorie.DoesNotExist:
        return JsonResponse({'message': 'Cette catégorie n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

    #recup un seul objet en fonction de son id
    if request.method == 'GET':
        categorie_serializer = CategorieSerializer(categorie)
        return JsonResponse(categorie_serializer.data)

    elif request.method == 'PUT':
        categorie_data = JSONParser().parse(request)
        categorie_serializer = CategorieSerializer(categorie, data=categorie_data)
        if categorie_serializer.is_valid():
            categorie_serializer.save()
            return JsonResponse(categorie_serializer.data)
        return JsonResponse(categorie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Supprimer un objet
    elif request.method == 'DELETE':
        supp = Categorie.objects.get(pk=pk)
        supp.delete()
        return JsonResponse({'message': '{} La catégorie a bien été supprimée !'.format(supp)}, status=status.HTTP_204_NO_CONTENT)
