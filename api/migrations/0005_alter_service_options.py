# Generated by Django 3.2.8 on 2021-10-14 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_service'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
    ]
