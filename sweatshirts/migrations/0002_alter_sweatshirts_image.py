# Generated by Django 5.0 on 2023-12-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweatshirts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sweatshirts',
            name='image',
            field=models.ImageField(upload_to='products'),
        ),
    ]