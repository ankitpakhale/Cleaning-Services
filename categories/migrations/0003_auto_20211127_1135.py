# Generated by Django 2.1.5 on 2021-11-27 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_mycart_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('adddress', models.CharField(default='', max_length=200)),
                ('service_date', models.DateField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField(default=None)),
            ],
        ),
        migrations.RemoveField(
            model_name='orders',
            name='person',
        ),
        migrations.AddField(
            model_name='mycart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.AddField(
            model_name='order',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.MyCart'),
        ),
    ]