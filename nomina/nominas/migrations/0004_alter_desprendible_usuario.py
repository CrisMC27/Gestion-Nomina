# Generated by Django 3.2.8 on 2024-10-22 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nominas', '0003_auto_20241022_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desprendible',
            name='usuario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='nominas.usuario'),
        ),
    ]
