from rest_framework import serializers
from livres.models import Livre


class LivreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Livre
        fields = ('id',
                  'titre',
                  'auteur',
                  'description')