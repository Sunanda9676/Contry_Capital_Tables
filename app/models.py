from django.db import models

# Create your models here.
class Country(models.Model):
    countryname=models.CharField(max_length=120)
    cid=models.IntegerField(primary_key=True)
    def __str__(self):
        return self.countryname
    
class Capital(models.Model):
    capitalname=models.CharField(max_length=120) 
    cid=models.OneToOneField(Country,on_delete=models.CASCADE) 
    def __str__(self):
        return self.capitalname

