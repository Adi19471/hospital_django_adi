from django.db import models

from hospital .models import Hospitals 

from patient .models import Patient

from insurencecompanyapp .models import Company

from datetime import datetime 


# Create your models here.
class ClaimStatus(models.Model):
    claim_status_code = models.CharField(max_length=90)
    status_description = models.TextField()
    
    def __str__(self):
        return self.claim_status_code
    
    
    

class Claim(models.Model):
    claim_number = models.IntegerField(primary_key=True)
    claim_status = models.ForeignKey(ClaimStatus, on_delete=models.CASCADE)
    hospital_id = models.ForeignKey(Hospitals, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    detailes = models.TextField()
    Claim_datees = models.DateField()
    
    def __str__(self):
        return self.claim_status
    
    