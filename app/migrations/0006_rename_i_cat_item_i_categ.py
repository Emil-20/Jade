# Generated by Django 4.0 on 2022-01-14 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='i_cat',
            new_name='i_categ',
        ),
    ]
