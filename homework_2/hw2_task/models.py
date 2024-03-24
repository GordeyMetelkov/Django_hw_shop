from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    phone_number = models.CharField(max_length=16)
    adress = models.TextField()
    registry_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.client_name)


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_count = models.IntegerField(default=0)
    additions_date = models.DateField(auto_now_add=True)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(default=0, max_digits=8,decimal_places=2)
    order_registry_date = models.DateField(auto_now_add=True)

