# Generated by Django 5.0.3 on 2024-03-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw2_task', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', height_field=250, upload_to='', width_field=250),
        ),
    ]
