from tkinter import CASCADE
from django.db import models

# Create your models here.

#customer -- saloon -- reserve



class Saloon (models.Model):
    saloon_no = models.CharField(max_length=10)
    saloon_name = models.CharField(max_length=50)
    date = models.DateTimeField()
    def __str__(self):
        return self.saloon_name
    



class Custmer (models.Model):
    name  = models.CharField(max_length=50)
    phone_no  = models.CharField(max_length=20)
    def __str__(self):
        return self.name



class Reserve (models.Model):
    custmer = models.ForeignKey(Custmer,on_delete=models.CASCADE, related_name=('reservation'))
    saloon = models.ForeignKey(Saloon,on_delete=models.CASCADE, related_name=('reservation'))
   

