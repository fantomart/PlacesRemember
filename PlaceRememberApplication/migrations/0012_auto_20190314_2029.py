# Generated by Django 2.1.7 on 2019-03-14 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlaceRememberApplication', '0011_auto_20190312_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='remember',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=3, default=-25.344, max_digits=6),
        ),
        migrations.AddField(
            model_name='remember',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=3, default=131.036, max_digits=6),
        ),
    ]
