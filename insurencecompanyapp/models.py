from django.db import models

# Create your models here.
class Company(models.Model):
    
    insurence_company_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    detales = models.TextField()
    
    def __str__(self):
        return self.name
    
