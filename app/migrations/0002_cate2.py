# Generated by Django 4.0 on 2022-01-13 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cate2',
            fields=[
                ('cat2_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat2_name', models.CharField(max_length=30)),
                ('cat1_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cat1')),
            ],
        ),
    ]
