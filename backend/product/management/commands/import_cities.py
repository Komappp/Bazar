import json
from typing import List
from django.core.management import BaseCommand
from product.models import City, Region


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
            region_model = Region(
                name=region['name']
            )
            region_model.save()
            for city in region['cities']:
                city_model = City(
                    name=city['name'],
                    lat=city['lat'],
                    lng=city['lng'],
                    region=region_model
                )
                city_model.save()
        print('Данные загружены в базу')