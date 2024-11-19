from django.db import models

# Create your models here.
class Ville(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Equipement(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Annonce(models.Model):
    title = models.CharField(max_length=200,null=True)
    price = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=200,null=True)
    datetime = models.DateTimeField()
    nb_rooms = models.IntegerField(null=True)
    nb_baths = models.IntegerField(null=True)
    surface_area = models.FloatField(null=True)
    link = models.URLField()
    ville = models.ForeignKey(Ville,on_delete=models.CASCADE,related_name='annonces')
    equipements = models.ManyToManyField(Equipement,through='AnnonceEquipement', related_name='annonces')


class AnnonceEquipement(models.Model):
    annonce = models.ForeignKey(Annonce,on_delete=models.CASCADE,related_name='equipements_associes')
    equipement = models.ForeignKey(Equipement,on_delete=models.CASCADE,related_name='annonces_associes')


    class Meta:
        unique_together = ('annonce','equipement')

    def __str__(self):
        return f'{self.annonce.title} - {self.equipement}'