from django.db import models

# Create your models here.


GENDER_CHOICES =[
    ('M','MALE'),
    ('F','FEMAIL'),
    ('O','OTHER'),
    
]
class Patient(models.Model):

    patient_id = models.IntegerField(primary_key =True)
    first_name = models.CharField("Patient FIRST NAME:",max_length=100) # this is manidatory
    last_name = models.CharField("Patient LAST NAML:",max_length=100,null=True,blank=True) # this is manidatory
    slug = models.SlugField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=GENDER_CHOICES,max_length=6)
    dateofbirth = models.DateTimeField(auto_now=True)
    mobile_number = models.CharField(max_length=10,verbose_name="Patients Mobile Number")
    email = models.EmailField()
    address = models.TextField()
    profileimage = models.ImageField(upload_to = "images/patient/")
    
    def __str__(self):
        return self.first_name +" " + self.last_name
    
    class Meta:
        verbose_name_plural = "PATIENT INFORMATION "
    
    