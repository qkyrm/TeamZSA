# Generated by Django 5.0 on 2023-12-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0002_allproduct'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AllProduct',
        ),
        migrations.AlterField(
            model_name='things',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
