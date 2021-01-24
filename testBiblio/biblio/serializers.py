from rest_framework import serializers
from biblio.models import Livre
from biblio.models import Categorie

class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = ('id',
                  'titre',
                  'auteur',
                  'description',
                  'categories')

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('id',
                  'intitule')

