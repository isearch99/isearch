# Generated by Django 3.0.4 on 2020-04-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_destination_price'),
    ]
 
    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
