# Generated by Django 2.1.5 on 2021-11-27 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20211127_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='oemail',
            field=models.EmailField(default='', max_length=254),
        ),
    ]