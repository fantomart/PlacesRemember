# Generated by Django 2.1.7 on 2019-03-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlaceRememberApplication', '0010_auto_20190312_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remember',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='PlaceRememberApplication/photos', verbose_name='Фото'),
        ),
    ]
