# Generated by Django 2.1.5 on 2021-11-27 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_order_oemail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='person',
        ),
        migrations.AddField(
            model_name='order',
            name='contact',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='order',
            name='services',
            field=models.CharField(default='', max_length=500),
        ),
    ]
