from django.core.management.base import BaseCommand
from ...models import Product
from random import choice, randint
from django.utils import lorem_ipsum


class Command(BaseCommand):
    help = "Create new product"

    def handle(self, *args, **kwargs):
        for i in range(5):
            product = Product(
                product_name=f'product {i + 1}',
                description=lorem_ipsum.paragraphs(3, common=False),
                price=randint(0, 99) / 100 + randint(0, 9999),
                product_count=randint(1, 30),
            )
            product.save()
