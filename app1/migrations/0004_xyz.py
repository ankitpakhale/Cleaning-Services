# Generated by Django 2.1.5 on 2021-09-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20210908_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='xyz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.PositiveIntegerField()),
            ],
        ),
    ]