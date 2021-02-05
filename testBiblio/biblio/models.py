from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#Modèle Profil
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.SmallIntegerField(default=0)
    avatar = models.ImageField(null=True)
    dateNaissance = models.DateField(null=True, default='', blank=True)
    bio = models.TextField(max_length=500, default='Coucou', blank=True)
    pays = models.CharField(max_length=30, default='France', blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user=instance)
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


