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
    phone = models.IntegerField(null=False,blank=False)
    def __str__(self):
        return self.name



class Facility(models.Model):
    title = models.CharField( max_length=50,null=False,blank=False)
    def __str__(self):
        return self.title


class Availability(models.Model):
    hospital =  models.ForeignKey(Hospital,on_delete=models.CASCADE,related_name='availbilities')  
    facility =  models.ForeignKey(Facility,on_delete=models.CASCADE,related_name='availbilities')
    total = models.IntegerField(null=False,blank=False, default=0)
    available = models.IntegerField(null=False,blank=False,default=0)  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.hospital.name}-{self.facility.title}'