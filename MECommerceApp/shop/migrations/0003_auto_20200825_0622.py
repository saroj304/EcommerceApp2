# Generated by Django 3.0.8 on 2020-08-25 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200825_0605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='prouct_name',
            new_name='proudct_name',
        ),
    ]
