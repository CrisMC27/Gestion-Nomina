# Generated by Django 3.2.8 on 2024-10-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nominas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='desprendible',
            name='total_hed',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='desprendible',
            name='total_hedd',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='desprendible',
            name='total_hen',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='desprendible',
            name='total_hend',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
