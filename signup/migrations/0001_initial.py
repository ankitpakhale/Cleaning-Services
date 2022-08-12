# Generated by Django 4.0.6 on 2022-08-12 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
                ('number', models.PositiveIntegerField(default='')),
                ('password', models.CharField(default='', max_length=15)),
                ('confirmPassword', models.CharField(default='', max_length=15)),
            ],
        ),
    ]
