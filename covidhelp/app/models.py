from django.db import models

# Create your models here.
class State(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.name
    


class City(models.Model):
    state=models.ForeignKey(State, on_delete=models.CASCADE,related_name='cities')
    name=models.CharField(max_length=50,null=False,blank=False)
    def __str__(self):
        return self.name

class Hospital(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    address=models.CharField(max_length=200,null=False,blank=False)
    city = models.ForeignKey(City,on_delete=models.CASCADE,related_name='hospitals')  
    phone = models.IntegerField(max_length=10,null=False,blank=False)
    def __str__(self):
        return self.name



class Services(models.Model):
    hospital = models.OneToOneField(Hospital,primary_key=True,on_delete=models.CASCADE) 
    oxygen_bed_total = models.IntegerField(default=0)
    aoygen_bed_availble = models.IntegerField(default=0)
    oxygen_cylender_total= models.IntegerField(default=0)
    oxygen_cylender_available = models.IntegerField(default=0)
    ventilator_total= models.IntegerField(default=0)
    ventilator_availbale = models.IntegerField(default=0)
    def __str__(self):
        return self.hospital.name


