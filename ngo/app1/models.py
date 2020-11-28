from django.db import models

# Create your models here.
class cause(models.Model):
    name = models.CharField(max_length=100)
    goal = models.IntegerField
    raised = models.IntegerField
    img = models.ImageField(upload_to = 'pics')
    ext_link = models.CharField(max_length=100)

class Volunteer(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=15)
    phone = models.IntegerField
    email = models.EmailField

class Contributors(models.Model):
    dob = models.IntegerField
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=15)
    phone = models.IntegerField
    email = models.EmailField

class Objects(models.Model):
    obj_id = models.IntegerField
    obj_name = models.CharField(max_length=15)
    obj_price = models.IntegerField


class Contributions(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField
    amt = models.IntegerField
    nationality = models.CharField(max_length=20)

class Events(models.Model):
    event_id = models.IntegerField
    title = models.CharField
    date = models.DateField
    place = models.CharField(max_length=20)