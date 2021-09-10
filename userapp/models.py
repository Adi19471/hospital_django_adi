from django.db import models
from datetime import datetime
# Create your models here.

from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_CHOISE = {
        ('M' ,'MALE'),
        ('F', 'FEMALE'),
        ('OTHERS' ,'OTHER CATEGERY')
    }
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    age = models.PositiveIntegerField()
    image = models.ImageField(upload_to="images/user",blank=True,null=True)
    biodata = models.TextField(max_length=500,blank=True,null=True)
    gender = models.CharField(choices=GENDER_CHOISE,max_length=20,blank=True,null=True)
    BirthDay = models.DateTimeField(default=datetime.now,blank=True,null=True)
    
    