from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime

from .forms import EditProductForm, AddImageForm
from .models import Order, Client, Product


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

def get_product(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    return render(request, 'hw2_task/product.html', {'product': product})


def edit_product(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    if request.method == 'POST':
        form = EditProductForm(request.POST)
        form2 = AddImageForm(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            data = form.cleaned_data
            data2 = form2.cleaned_data
            product.product_name = data['product_name']
            product.description = data['description']
            product.price = data['price']
            product.product_count = data['product_count']
            product.image = data2['image']
            fs = FileSystemStorage()
            fs.save(product.image.name, product.image)
            product.save()
            return redirect('get_product', product_id)
    else:
        form = EditProductForm()
        form2 = AddImageForm()
    return render(
        request,
        'hw2_task/edit_product.html',
        {'form': form, 'form2': form2}
    )

def index(request):
    return render(request, 'hw2_task/index.html')