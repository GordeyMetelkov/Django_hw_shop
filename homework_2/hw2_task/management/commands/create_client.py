from django.core.management.base import BaseCommand
from ...models import Client
from random import choice, randint

class Command(BaseCommand):
    help = "Create new client"


    def handle(self, *args, **kwargs):
        cities = ['Moscow', 'Minsk', 'Bobruisk', 'London']
        streets = ['First', 'Red-lights', 'Broken-lights', 'General', "Five-rivers"]
        for i in range(5):
            client = Client(
                client_name = f'Name {i+1}',
                email = f'Name{i+1}@mail.hi',
                phone_number =f'+7-{i+1}{i+1}{i+1}-'
                              f'{i+1}{i+1}{i+1}-{i+1}{i+1}-{i+1}{i+1}',
                adress =f'{choice(cities)}, '
                        f'{choice(streets)} str., {randint(1, 118)}',
            )
            client.save()
