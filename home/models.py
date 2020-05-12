from django.db import models
class Patient (models.Model):
       PatientName = models.CharField(max_length=200)
       PatientAge = models.DateField()
       PatientID = models.IntegerField()
       Allergies=models.TextField()
       ChronicDisease=models.BooleanField()
       History=models.TextField()

    
def  __str__(self):
    return self.PatientName
