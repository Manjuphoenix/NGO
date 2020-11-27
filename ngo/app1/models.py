from django.db import models

# Create your models here.
class cause(models.Model):
    name = models.CharField(max_length=100)
    goal = models.IntegerField
    raised = models.IntegerField
    img = models.ImageField(upload_to = 'pics')
    ext_link = models.CharField(max_length=100)