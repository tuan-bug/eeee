# Generated by Django 4.2.2 on 2023-07-21 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_remove_slide_category_slide'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='category_slide',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.category'),
        ),
    ]