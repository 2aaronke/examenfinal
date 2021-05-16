from django.db import models

# Create your models here.

class vuelo(models.Model):
   subtotal= models.IntegerField()
   total= models.IntegerField()
   descuento= models.IntegerField()
   
