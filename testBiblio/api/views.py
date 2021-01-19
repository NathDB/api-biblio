from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from api.models import Api
from api.serializers import ApiSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def api_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    #Pour récup un objet avec une condition
    if request.method == 'GET':
        apis = Api.objects.all()

        titre = request.GET.get('titre', None)
        if titre is not None:
            apis = apis.filter(titre__icontains=titre)

        apis_serializer = ApiSerializer(apis, many=True)
        return JsonResponse(apis_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    #Pour créer un nouvel objet
    elif request.method == 'POST':
        api_data = JSONParser().parse(request)
        api_serializer = ApiSerializer(data=api_data)
        if api_serializer.is_valid():
            api_serializer.save()
            return JsonResponse(api_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def api_detail(request, pk):
    # find tutorial by pk (id)
    try:
        api = Api.objects.get(pk=pk)
    except Api.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

        #recup un seul objet en fonction de son id
    if request.method == 'GET':
        api_serializer = ApiSerializer(api)
        return JsonResponse(api_serializer.data)

    elif request.method == 'PUT':
        api_data = JSONParser().parse(request)
        api_serializer = ApiSerializer(api, data=api_data)
        if api_serializer.is_valid():
            api_serializer.save()
            return JsonResponse(api_serializer.data)
        return JsonResponse(api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Supprimer un objet
    elif request.method == 'DELETE':
        supp = Api.objects.get(pk=pk)
        supp.delete()
        return JsonResponse({'message': '{} Tutorial was deleted successfully!'.format(supp)}, status=status.HTTP_204_NO_CONTENT)

    # GET / PUT / DELETE tutorial
