# Generated by Django 2.1.5 on 2021-10-01 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20210920_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default='', max_length=6)),
                ('description', models.CharField(default='', max_length=90)),
            ],
        ),
    ]