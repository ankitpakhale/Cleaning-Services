# Generated by Django 2.1.5 on 2021-10-01 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(default=''),
        ),
    ]