from django.shortcuts import render
import datetime
from .models import Order, Client


def get_all_orders_by_client(request, client_id):
    orders = Order.objects.filter(client__pk=client_id)
    client = Client.objects.filter(pk=client_id).first()
    context = {'orders': orders, 'client': client}
    return render(request, 'hw2_task/orders_by_client.html', context)

def get_orders_by_time(request, client_id, time):
    client = Client.objects.filter(pk=client_id).first()
    check_date = datetime.date.today() - datetime.timedelta(days=time)
    orders = Order.objects.filter(client__pk=client_id)
    result = []
    for order in orders:
        if order.order_registry_date > check_date:
            result.append(order)
    context = {'orders': result, 'client': client, 'time': time}
    return render(request, 'hw2_task/orders_by_time.html', context)
