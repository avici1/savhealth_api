from django.db import models

# Create your models here.
class person(models.Model):
    first_name = models.CharField(null=True,max_length=30)
    last_name = models.CharField(null=False,max_length=30)
    dob = models.CharField(null=True,max_length=20)
    sex = models.CharField(null=True,max_length=12)
    place_of_issue = models.CharField(null=True,max_length=50)
    Nid = models.BigIntegerField(default=00000000000000000000)
    fprint_data = models.CharField(null=True,max_length=1000)
    
    def __str__(self):
        return self.first_name
class insurance_dt(models.Model):
    first_name = models.CharField(null=True, max_length=30)
    last_name = models.CharField(null=False, max_length=30)
    dob = models.CharField(null=True, max_length=20)
    sex = models.CharField(null=True, max_length=12)
    nid = models.CharField(null=True, max_length=40)
    policy_no = models.CharField(null=True, max_length=30)
    card_no = models.CharField(null=True, max_length=30)
    valid = models.CharField(null=True, max_length=30)
    patient_contrib = models.CharField(null=True, max_length=30)
    insurance_compny = models.CharField(null=True, max_length=30)
    
    def __str__(self):
        return self.first_name
class medical_history(models.Model):
        chiefComplaint = models.TextField()
        pastMedicalHistory = models.TextField()
        familyHistory = models.TextField()
        drugAndAllergyHistory = models.TextField()
        socialHistory = models.TextField()
        nid = models.CharField(null=True,max_length=16)
      
        def __str__(self):
            return self.nid
class hospitals(models.Model):
     latitude = models.FloatField(default=0.00000)
     longitude = models.FloatField(default=0.00000)
     hospitals_name = models.CharField(default="empty",max_length=50)
     speciality = models.CharField(default="empty",max_length=40)
     availability_status = models.CharField(default="empty",max_length=40)
     ho_id = models.CharField(default="empty",max_length=40)
       
     def __str__(self):
            return self.ho_id