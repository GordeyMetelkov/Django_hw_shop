from django.contrib import admin

from .models import Client, Product, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'email', 'phone_number', 'adress', 'registry_date',]
    list_filter = ['registry_date',]
    list_display_links = ('id', 'client_name')
    readonly_fields = ['registry_date']
    fieldsets = (('Публичные данные', {'classes': ['collapse'],
                                       'fields': ['client_name']}),
                 ('Данные сайта', {'classes': ['collapse'],
                                   'fields': ['registry_date']}),
                 ('Приватные данные', {'classes': ['collapse'],
                                       'fields': ['email', 'phone_number', 'adress']}))

@admin.action(description="Сбросить количество в ноль")
def reset_count(modeladmin, request, queryset):
    queryset.update(product_count=0)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'product_count', 'additions_date', 'image',]
    list_filter = ['additions_date',]
    readonly_fields = ['additions_date']
    fieldsets = (('Информация о товаре', {'fields': ['product_name', 'description']}),
                 ('Отчетность', {'fields': ['price', 'product_count']}),
                 ('Дополнительная информация', {'fields': ['additions_date', 'image']}))
    search_fields = ['description']
    search_help_text = 'Поиск по описанию'
    actions = [reset_count]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_price']
    readonly_fields = ['client', 'order_registry_date']

