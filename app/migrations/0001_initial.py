# Generated by Django 4.0 on 2022-01-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cat1',
            fields=[
                ('cat1_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat1_name', models.CharField(max_length=30)),
            ],
        ),
    ]
