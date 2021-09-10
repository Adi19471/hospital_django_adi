from django.db import models

from datetime import datetime
# Create your models here.


class Hospital_Type(models.Model):
    type_name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    
    def __str__(self):
        return self.type_name
    
    
class Hospitals(models.Model):
    
    hospital_id = models.IntegerField()
    category = models.ForeignKey('Hospital_Type',on_delete=models.CASCADE)
    htype = models.CharField(max_length=300)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=300)

    address = models.TextField()
    updateDate = models.DateField(default = datetime.now)
    logo = models.ImageField(upload_to="images/",blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "HOSPITAL INFO "
    
    