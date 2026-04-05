from django.db import models
from django.contrib.auth.models import User





class Record(models.Model):
    first_name=models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email= models.EmailField(max_length=255)
    address= models.CharField(max_length=100)
    phone= models.CharField(max_length=20)
    city= models.CharField(max_length=255)
    province= models.CharField(max_length=200)
    country= models.CharField(max_length=125)
    created_at= models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
                               
                               
                               
                               
                               
        

    def __str__(self):
        return self.first_name + ' ' +self.last_name
    

   
                                   








# Create your models here.
