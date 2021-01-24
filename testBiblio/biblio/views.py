from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from biblio.models import Livre
from biblio.models import Categorie
from biblio.serializers import LivreSerializer
from biblio.serializers import CategorieSerializer
from rest_framework.decorators import api_view

#Auth0
from functools import wraps
import jwt
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

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

# auth0authorization/views.py
def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token

def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response
        return decorated
    return require_scope

@api_view(['GET'])
@permission_classes([AllowAny])
def public(request):
    return JsonResponse({'message': 'Hello from a public endpoint! You don\'t need to be authenticated to see this.'})

#Route privée, après authentification de l'user
@api_view(['GET'])
def private(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated to see this.'})

#Route ultra privée, nécessitant un accès grant, ici permission de lire les messages (=admin)
@api_view(['GET'])
@requires_scope('read:messages')
def private_scoped(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this.'})