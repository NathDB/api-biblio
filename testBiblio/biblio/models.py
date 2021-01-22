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

#Modèle LivreSuggere
class LivreSuggere(models.Model):
    titre = models.CharField(max_length=70)
    auteur = models.CharField(max_length=70)
    description = models.CharField(max_length=200)
    categories = models.ManyToManyField(Categorie) #Relation ManyToMany entre LivreSuggere<->Catégorie => crée automatiquement une table pivot

#Modèle Liste
class Liste(models.Model):
    titre = models.CharField(max_length=70)
    livres = models.ManyToManyField(Livre) #Relation ManyToMany entre Livre<->Liste => crée automatiquement une table pivot
    #id_user = models.ForeignKey('User', on_delete=models.CASCADE)

#Modèle User
# class User(models.Model):
#     nom = models.CharField(max_length=70)
#     prenom = models.CharField(max_length=70)
#     age = models.PositiveSmallIntegerField()
#     mail = models.EmailField()
#     mdp = models.CharField(max_length=20)
#     score = models.PositiveSmallIntegerField()
#     avatar = models.ImageField()

#Modèle Historique
#class Historique(models.Model):
    #id_user = models.ForeignKey('User', on_delete=models.CASCADE)
    #notification = models.CharField(max_length=200)
