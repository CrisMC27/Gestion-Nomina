# Generated by Django 3.2.8 on 2024-10-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nominas', '0006_auto_20241026_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cedula',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='celular',
            field=models.IntegerField(),
        ),
    ]
