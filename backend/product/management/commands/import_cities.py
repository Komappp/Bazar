import json
from typing import List
from django.core.management import BaseCommand
from product.models import City


class Command(BaseCommand):
    help = "Loads data from ingredients.csv"

    def handle(self, *args, **options):
        if City.objects.exists():
            print('Данные загружены ....выход')
            return

        print('Загрузка городов в базу данных')

        with open("data/by-cities.json", "r") as read_file:
            data = json.load(read_file)
        data_clean: List = data[0]['regions']
        for region in data_clean:
            for city in region['cities']:
                print(city['name'])
                # city_model = City(
                #     name=city['name'],
                #     lat=city['lat'],
                #     lng=city['lng'],
                #     region=region['name']
                # )
                # city_model.save()