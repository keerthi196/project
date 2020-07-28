from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

# Create your models here.
class Login(models.Model):
    e_mail=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

# class Employee(models.Model):
#     firstname=models.CharField(max_length=50)
#     e_mail=models.CharField( max_length=50)
#     password=models.CharField(max_length=20)
#     mobilenumber=models.CharField(max_length=10)
#     area=models.CharField(max_length=50)
#     city=models.CharField(max_length=20)

class Admin(models.Model):
    shopname = models.TextField(primary_key=True)
    firstname = models.TextField()
    e_mail = models.TextField()
    mobilenumber = models.TextField()
    password = models.TextField()
    area=models.TextField()
    city=models.TextField()

class categories(models.Model):
    shopname=models.TextField()
    category=models.TextField()
    productname=models.TextField()
    price=models.TextField()
    brand=models.TextField()
    quantity=models.TextField()

class setname(models.Model):
    name=models.TextField(primary_key=True)


class Place_order_Monthly(models.Model):
    servicetype=models.TextField()
    shopname=models.TextField()
    customername=models.TextField()
    productname=models.TextField()
    price=models.TextField()
    brand=models.TextField()
    quantity=models.TextField()

class Place_order_Day(models.Model):
    servicetype=models.TextField()
    shopname=models.TextField()
    customername=models.TextField()
    productname=models.TextField()
    price=models.TextField()
    brand=models.TextField()
    quantity=models.TextField()


class monthlcart(models.Model):
    productname=models.CharField(max_length=20)
    brand=models.CharField(max_length=10)
    quantity= models.CharField(max_length=4)
    price=models.CharField(max_length=10)

class deliverySide(models.Model):
    customername=models.TextField(primary_key=True)
    amount=models.TextField()


class daycart(models.Model):
    productname=models.CharField(max_length=20)
    brand=models.CharField(max_length=10)
    quantity= models.CharField(max_length=4)
    price=models.CharField(max_length=10)

class userregister(models.Model):
    firstname=models.CharField(max_length=50)
    e_mail=models.CharField( max_length=50)
    password=models.CharField(max_length=20)
    mobilenumber=models.CharField(max_length=10)
    area=models.CharField(max_length=50)
    city=models.CharField(max_length=20)

class UserRegisterWithPK(models.Model):
    firstname = models.TextField()
    e_mail = models.TextField(primary_key=True)
    mobilenumber = models.TextField()
    password = models.TextField()
    area=models.TextField()
    city=models.TextField()

class Usermonthlycart(models.Model):
    Username = models.TextField()
    productname=models.TextField()
    brand=models.TextField()
    quantity= models.TextField()
    price=models.TextField()

class UserDayCart(models.Model):
    Username = models.TextField()
    productname=models.TextField()
    brand=models.TextField()
    quantity= models.TextField()
    price=models.TextField()

    
class deliveryboyregister(models.Model):
    firstname=models.CharField(max_length=50)
    e_mail=models.CharField( max_length=50)
    password=models.CharField(max_length=20)
    mobilenumber=models.CharField(max_length=10)
    area=models.CharField(max_length=50)
    city=models.CharField(max_length=20)

class oils(models.Model):
    productname=models.CharField(max_length=20)
    brand=models.CharField(max_length=10)
    quantity= models.CharField(max_length=4)
    price=models.CharField(max_length=10)

class breakfast(models.Model):
    productname=models.CharField(max_length=20)
    brand=models.CharField(max_length=10)
    quantity= models.CharField(max_length=4)
    price=models.CharField(max_length=10)

class cooldrink(models.Model):
    productname=models.CharField(max_length=20)
    brand=models.CharField(max_length=10)
    quantity= models.CharField(max_length=6)
    price=models.CharField(max_length=10)

class dryfruits(models.Model):
    productname=models.CharField(max_length=20)
    brand=models.CharField(max_length=10)
    quantity= models.CharField(max_length=4)
    price=models.CharField(max_length=10)

class detergent(models.Model):
    productname=models.CharField(max_length=20)
    brand=models.CharField(max_length=10)
    quantity= models.CharField(max_length=4)
    price=models.CharField(max_length=10)

class homecleaners(models.Model):
    productname=models.CharField(max_length=20)
    brand=models.CharField(max_length=10)
    quantity= models.CharField(max_length=4)
    price=models.CharField(max_length=10)

class kitchencleaners(models.Model):
    productname=models.CharField(max_length=20)
    brand=models.CharField(max_length=10)
    quantity= models.CharField(max_length=4)
    price=models.CharField(max_length=10)

class liquiddetergents(models.Model):
    productname=models.CharField(max_length=20)
    brand=models.CharField(max_length=10)
    quantity= models.CharField(max_length=4)
    price=models.CharField(max_length=10)

class masalas(models.Model):
    productname=models.CharField(max_length=20)
    brand=models.CharField(max_length=10)
    quantity= models.CharField(max_length=4)
    price=models.CharField(max_length=10)

class rice(models.Model):
    productname=models.CharField(max_length=20)
    brand=models.CharField(max_length=10)
    quantity= models.CharField(max_length=4)
    price=models.CharField(max_length=10)

class snacks(models.Model):
    productname=models.CharField(max_length=20)
    brand=models.CharField(max_length=10)
    quantity= models.CharField(max_length=4)
    price=models.CharField(max_length=10)

class syrups(models.Model):
    productname=models.CharField(max_length=20)
    brand=models.CharField(max_length=10)
    quantity= models.CharField(max_length=4)
    price=models.CharField(max_length=10)


