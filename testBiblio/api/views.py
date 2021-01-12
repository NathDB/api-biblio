from django.shortcuts import render

# Create your views here.

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from api.models import Api
from api.serializers import ApiSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def api_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    return 0

@api_view(['GET', 'PUT', 'DELETE'])
def api_detail(request, pk):
    # find tutorial by pk (id)
    try:
        api = Api.objects.get(pk=pk)
    except Api.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET / PUT / DELETE tutorial
