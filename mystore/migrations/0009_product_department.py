# Generated by Django 4.2.13 on 2024-09-12 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0008_profile_old_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='department',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
    ]