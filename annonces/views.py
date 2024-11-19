from django.shortcuts import render
from django.http import HttpResponse
from .forms import ScrapingForm
import sys
import os
from django.db import transaction, IntegrityError

from annonces.scraping.scraper import ApartmentDataScraper,ApartmentLinkScraper,random_datetime
from .models import Annonce,AnnonceEquipement,Equipement,Ville
from django.db import InternalError
from datetime import datetime



def index(request):
    return HttpResponse("Bienvenue sur la page d'annonces")



# Create your views here.

def start_scraping(request):
    if request.method == 'POST':
        form = ScrapingForm(request.POST)
        if form.is_valid():
            pages = form.cleaned_data['pages']
            niche = form.cleaned_data['niche']

            object_scrape_link = ApartmentLinkScraper(niche, pages)
            les_liens = object_scrape_link.scrape_links()
            object_scrap_data = ApartmentDataScraper(les_liens)
            data_dict = object_scrap_data.scrape_data()

            object_scrap_data.save_data_to_csv(r'C:\Users\Youcode\Desktop\database_avito_vehecule\projet_annonces\annonces\data_csv\data.csv')

            try:
                with transaction.atomic():
                    for annonce_data in data_dict:
                        # Vérifier ou créer la ville
                        ville_name = annonce_data.get('location', 'Unknown')
                        ville, created = Ville.objects.get_or_create(name=ville_name)

                        # Générer une date aléatoire si elle est absente
                        annonce_datetime = annonce_data.get('datetime')
                        if not annonce_datetime:
                            annonce_datetime = random_datetime()
                        else:
                            annonce_datetime = datetime.strptime(annonce_datetime, "%Y-%m-%d %H:%M:%S")

                        # Créer l'annonce
                        annonce = Annonce(
                            title=annonce_data['title'],
                            price=annonce_data['price'],
                            datetime=annonce_datetime,
                            nb_rooms=annonce_data['nb_rooms'],
                            nb_baths=annonce_data['nb_baths'],
                            surface_area=annonce_data['surface_area'],
                            link=annonce_data['link'],
                            ville=ville,
                        )
                        annonce.save()

                        # Gérer les équipements
                        equipements = annonce_data.get('equipement', '').split('/')
                        for equip_name in equipements:
                            equip_name = equip_name.strip()
                            if equip_name:
                                equipement, created = Equipement.objects.get_or_create(name=equip_name)
                                AnnonceEquipement.objects.create(annonce=annonce, equipement=equipement)

                return HttpResponse("Scraping et sauvegarde réussis dans la base de données.")
            except IntegrityError as e:
                return HttpResponse(f"Erreur lors de l'insertion des données : {str(e)}")
        else:
            return HttpResponse("Formulaire invalide.")
    else:
        form = ScrapingForm()

    return render(request, 'start_scraping.html', {'form': form})




