from django.db import models

class Person(models.Model):
    companies_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Title = models.CharField(max_length=30)
    Email = models.EmailField(blank=True)
    #birth_date = models.DateField()
    url = models.CharField(max_length=30)
    

# Create your models here.
