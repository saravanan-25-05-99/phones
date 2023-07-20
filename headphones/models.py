from django.db import models

class Product(models.Model):
    model_name = models.CharField(max_length=120)
    price = models.FloatField()
    image = models.ImageField(upload_to="images")
    quantity = models.SmallIntegerField()
    seller_detail = models.CharField(max_length=50)
    warranty = models.CharField(max_length=50)
    specification = models.TextField()
    memory = models.CharField(
        max_length=4,
        choices=(('1','2 GB'),('2','3 GB'),('3','4 GB')),default='1')
    date=models.DateField(auto_now=True)
    
class Student(models.Model):
    firstname=models.CharField(max_length=120)
    lastname=models.CharField(max_length=120)
    course=models.CharField(max_length=3)
    gender=models.CharField(max_length=10)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    email=models.EmailField()
class Laptop(models.Model):
    laptopname=models.CharField(max_length=50)
    laptopmodel=models.CharField(max_length=50)
    price=models.FloatField()
    color=models.CharField(max_length=10)
    description=models.TextField()
    warranty=models.CharField(max_length=50)
    memory = models.CharField(
        max_length=4,
        choices=(('1','4 GB'),('2','8 GB'),('3','16 GB')),default='1')
    
    
    