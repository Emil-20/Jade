from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class cat1(models.Model):
    cat1_id=models.AutoField(primary_key=True)
    cat1_name=models.CharField(max_length=30)

class cate2(models.Model):
    cat2_id=models.AutoField(primary_key=True)
    cat1_id=models.ForeignKey(cat1, on_delete=models.CASCADE)
    cat2_name=models.CharField(max_length=30)

class item(models.Model):
    i_id=models.AutoField(primary_key=True)
    i_categ=models.CharField(max_length=30)
    i_name=models.CharField(max_length=30)
    i_desc=models.CharField(max_length=30)
    i_price=models.CharField(max_length=30)
    i_offerprice=models.CharField(max_length=30)
    i_pic=models.ImageField(upload_to="img/%y", default='')


