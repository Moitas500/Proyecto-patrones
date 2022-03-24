# Generated by Django 2.2.27 on 2022-03-24 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0003_auto_20220321_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cliente', to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to='shop.Product')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vendedor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ('id',),
            },
        ),
    ]
