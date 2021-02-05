from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#Modèle User
class Profil(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.SmallIntegerField()
    avatar = models.ImageField()
    dateNaissance = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    pays = models.CharField(max_length=30, blank=True)

#Méthodes permettant d'associer un user à un profil, de mettre à jour et de créer un profil quand un user est créé
@receiver(post_save, sender=User)
def create_user_profil(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profil(sender, instance, **kwargs):
    instance.profil.save()

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
    nom = models.CharField(max_length=70)
    livres = models.ManyToManyField(Livre) #Relation ManyToMany entre Livre<->Liste => crée automatiquement une table pivot
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

# #Modèle Historique -> voir système de notifs Ionic
# class Historique(models.Model):
#     titre = models.CharField(max_length=70)
#     livres = models.ManyToManyField(Livre) #Relation ManyToMany entre Livre<->Liste => crée automatiquement une table pivot
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


