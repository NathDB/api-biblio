from rest_framework import serializers
from biblio.models import Livre
from biblio.models import Categorie
from biblio.models import Liste
from biblio.models import LivreSuggere

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

class ListeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('id',
                  'titre',
                  'livres',
                  'user')

class LivreSuggereSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivreSuggere
        fields = ('id',
                  'titre',
                  'auteur',
                  'description',
                  'categories')

