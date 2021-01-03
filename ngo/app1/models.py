from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
#class User:
'''class Index(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=100)

class cause(models.Model):
    name = models.CharField(max_length=100)
    goal = models.CharField(max_length=100)
    raised = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')
    ext_link = models.CharField(max_length=100)
'''
class Volunteer(models.Model):
    name = models.CharField(max_length=20,)
    country = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    #id = models.ForeignKey(Contributors, )

    #def __str__(self):
    #    return ("Name: " +(name)+ "Email: " +(email))


class Contributors(models.Model):
    dob = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)
    email = models.EmailField(default=None)

class Objects(models.Model):
    obj_name = models.CharField(max_length=15)
    obj_price = models.CharField(max_length=5)
    image = models.ImageField(upload_to = 'orders')


class Donation(models.Model):
    name = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)
    mail = models.EmailField()
    amt = models.CharField(max_length=10)
    nationality = models.CharField(max_length=20)

class Events(models.Model):
    eventName = models.CharField(max_length=100, default=None)
    organizer = models.CharField(max_length=30, default=None)
    eventType = models.CharField(max_length=30, default=None)
    date = models.DateField(default=None)
    place = models.CharField(max_length=20)

class Adopt(models.Model):
    name = models.CharField(max_length=30, null=False)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, null=False)

'''class Education(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=10)
    email = models.EmailField(default=None)
    message = models.CharField(max_length=250, default=None)'''