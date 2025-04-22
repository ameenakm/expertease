from django.db import models

# Create your models here.
class category(models.Model):
    categoryname=models.CharField(max_length=20)
    date=models.DateField(auto_now_add=True)
class subcategory(models.Model):
    categorynm=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    subcategorynm=models.CharField(max_length=20)
class freelancers(models.Model):
    name=models.CharField(max_length=20)
    date=models.DateField(auto_now_add=True)
    place=models.CharField(max_length=20)
    categoryname = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    subcategoryname = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
    specilization=models.CharField(max_length=30)
    bi=models.CharField(max_length=100)
    image=models.FileField(upload_to='img',null=True)
    wi=models.CharField(max_length=100)
    wimage=models.FileField(upload_to='img',null=True)
    cn=models.IntegerField(null=True)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)