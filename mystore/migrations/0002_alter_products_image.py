# Generated by Django 4.2.13 on 2024-06-15 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, upload_to='../../static/images'),
        ),
    ]