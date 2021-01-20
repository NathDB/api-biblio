from django.db import models

#Modèle Categorie
class Categorie(models.Model):
    intitule = models.CharField(max_length=70)

#Modèle Livre
class Livre(models.Model):
    titre = models.CharField(max_length=70)
    auteur = models.CharField(max_length=70)
    description = models.CharField(max_length=200)
    categories = models.ManyToManyField(Categorie) #Relation ManyToMany entre Livre<->Catégorie => crée automatiquement une table pivot
