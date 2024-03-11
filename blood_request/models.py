from django.db import models
from hospital.models import Hospital
# Create your models here.
class BloodRequest(models.Model):
    blood_id = models.AutoField(primary_key=True)
    # hospital_id = models.IntegerField()
    hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE)
    bloodgroup = models.CharField(max_length=45)
    unit = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'blood_request'