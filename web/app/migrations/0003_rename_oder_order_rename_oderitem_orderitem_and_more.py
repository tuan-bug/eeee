# Generated by Django 4.2.2 on 2023-07-11 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oder',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='OderItem',
            new_name='OrderItem',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='date_oder',
            new_name='date_order',
        ),
    ]