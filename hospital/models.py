from django.db import models

# Create your models here.
class Hospital(models.Model):
    # for patients
    patient_name= models.CharField(max_length=50)
    patient_id= models.CharField(max_length=200)
    patient_number= models.IntegerField(max_length=10)
    patient_address= models.CharField(max_length=200)
    patient_admit= models.BooleanField(default=True)
    patient_ward=models.CharField(max_length=10)


    def __str__(self):
        return self.patient_name
    
    
    
'''
    # for staff
    staff_name= models.CharField(max_length=50)
    staff_id= models.CharField(max_length=200)
    staff_number= models.IntegerField(max_length=10)
    staff_address= models.CharField(max_length=200)

    #for doctor
    doctor_name= models.CharField(max_length=50)
    doctor_id= models.CharField(max_length=50)
    doctor_number= models.IntegerField(max_length=10)
    doctor_address= models.CharField(max_length=200)
    doctor_specialization= models.CharField(max_length=50)


'''
