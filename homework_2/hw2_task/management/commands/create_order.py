from django.core.management.base import BaseCommand
from ...models import Product, Order, Client
from random import choice, randint
from django.utils import lorem_ipsum


class Command(BaseCommand):
    help = "Create new order"

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        products = Product.objects.all()
        for _ in range(1):
            order = Order(
                client=choice(clients),
            )
            order.save()
            price = 0
            prod_set = set()
            for _ in range(3):
                flag = True
                while flag:
                    product = choice(products)
                    if product in prod_set:
                        flag = True
                    elif product.product_count == 0:
                        flag = True
                    else:
                        order.products.add(product)
                        price += product.price
                        product.product_count -= 1
                        product.save()
                        prod_set.add(product)
                        flag = False
            order.total_price = price
            order.save()

