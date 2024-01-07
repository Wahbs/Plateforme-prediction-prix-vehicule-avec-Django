from django.shortcuts import render, redirect
import pickle
import pandas as pd
import numpy as np
from prix_voiture.forms import *
from prix_voiture.models import *
# Create your views here.


def fonction_map_pred(new_data, colonnes):
    prediction = pd.DataFrame(columns = colonnes)
    new_data = new_data.astype({'annee': float, 'kilometrage': float})
    prediction.loc[0] = 0
    prediction.loc[1] = 0
    for i in range(0, len(new_data)):
        for colon in new_data:
            if new_data[colon].dtype == 'object':
                if new_data[colon][i] in prediction.columns:
                    nom_marque = new_data[colon][i]
                    prediction[nom_marque][i] = 1.0
            else:
                prediction[colon][i] = new_data[colon][i]
    prediction = prediction.fillna(0.0)
    return prediction


def accueil(request):
    output = ""
    text = ''
    if request.method == 'POST':
        # Nouvelles données à prédire
        new_data = pd.DataFrame({
            'annee': [request.POST['annee'],],
            'kilometrage': [request.POST['kilometrage'],],
            'boite_vitesse': [request.POST['boite_vitesse'],],
            'carburant': [request.POST['carburant'],],
            'marque': [request.POST['marque'],],
        })
        colonnes = ['annee', 'kilometrage', 'BMW', 'CHEVROLET', 'CHRYSLER', 'FERRARI',
                   'FIAT', 'FORD', 'HONDA', 'HUMMER', 'HYUNDAI', 'INFINITI', 'JAGUAR',
                   'JEEP', 'KIA', 'LEXUS', 'MAZDA', 'MERCEDES', 'MITSUBISHI', 'NISSAN',
                   'OPEL', 'PEUGEOT', 'RENAULT', 'TOYOTA', 'VOLKSWAGEN', 'Manuelle',
                   'Bicarburation essence bioéthanol', 'Diesel', 'Essence', 'Hybrides',
                   'Électrique']
        annee = request.POST['annee']
        kilometrage = request.POST['kilometrage']
        boite_vitesse = request.POST['boite_vitesse']
        carburant = request.POST['carburant']
        marque = request.POST['marque']
        text = ''
        err = 0
        if annee == '' or kilometrage == '' or marque == '':
            text = 'Veuillez renseigner toutes les informations !'
            err += 1
        else : 
            if not annee.isdigit() or not kilometrage.isdigit():
                text = 'Annee et Kilometrage doivent être numerique !'
                err += 1
        if err == 0:
            print("Chargement...")
            modele = pickle.load(open('random_forest.pkl', 'rb'))
            print(fonction_map_pred(new_data, colonnes))
            print("---------------------------------------------------------------------------")
            pred = modele.predict(fonction_map_pred(new_data, colonnes))
            print(pred)
            output = round(pred[0])

            context = {
                'output': output, 'marque': marque, 'annee': annee,'boite_vitesse': boite_vitesse,
                'carburant': carburant, 'kilometrage': kilometrage,
            }
            return render(request, 'Affiche_sortie.html', context)

    return render(request, 'index.html', {'output': output, 'text': text})


def ajout_voiture(request):
    Voiture = details_voiture.objects.all()
    form_ajout = form_ajout_voiture()
    toutes_les_voitures = []

    for v in Voiture:
        toutes_les_voitures.append(v.marque)

    if request.method == 'POST':
        form_ajout = form_ajout_voiture(request.POST)
        if form_ajout.is_valid():
            voiture = form_ajout.save(commit=False)
            voiture.save()
            return redirect('accueil')

    return render(request, 'ajout_voiture.html', {'form_ajout': form_ajout})