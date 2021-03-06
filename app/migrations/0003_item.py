# Generated by Django 4.0 on 2022-01-13 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cate2'),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('i_id', models.AutoField(primary_key=True, serialize=False)),
                ('i_name', models.CharField(max_length=30)),
                ('i_desc', models.CharField(max_length=30)),
                ('i_price', models.CharField(max_length=30)),
                ('i_offerprice', models.CharField(max_length=30)),
                ('i_pic', models.ImageField(default='', upload_to='img/%y')),
                ('cat1_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cat1')),
                ('cat2_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cate2')),
            ],
        ),
    ]
