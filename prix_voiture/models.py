from django.db import models

# Create your models here.

class details_voiture(models.Model):
    def __str__(self):
        return f'{self.marque}'

    boite_choice = [
        ('Automatique', 'Automatique'), ('Manuelle', 'Manuelle'),
    ]
    carburant_choice = [
        ('Essence', 'Essence'), ('Electrique', 'Electrique'), ('Diesel', 'Diesel'), ('Hybrides', 'Hybrides'),
        ('Bicarburation essence bioéthanol', 'Bicarburation essence bioéthanol'),
        ('Bicarburation essence / gpl', 'Bicarburation essence / gpl')
    ]

    marque = models.CharField(max_length=100, verbose_name='Marque', blank=False)
    annee = models.IntegerField(verbose_name='Année de sortie', blank=True)
    kilometrage = models.IntegerField(verbose_name='Kilometrage', blank=True)
    boite_vitesse = models.CharField(max_length=25, choices=boite_choice,
                                          verbose_name='Boite vitesse', blank=True)
    carburant = models.CharField(max_length=50, choices=carburant_choice, verbose_name='type carburant', blank=True)
    prix = models.IntegerField(verbose_name='prix', blank=True)

    class Meta:
        ordering = ('marque',)

