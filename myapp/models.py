from django.db import models

# Create your models here.

class form(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    def __str__(self):
        return self.firstname

class maid_registerm(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    contactnumber=models.CharField(max_length=200)
    fees=models.CharField(max_length=200)

class user_registerm(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    contactnumber=models.CharField(max_length=200)
    fees=models.CharField(max_length=200)


