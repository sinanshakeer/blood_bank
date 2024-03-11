from django.db import models
from student.models import Student
# Create your models here.

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    # student_id = models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    latitude = models.CharField(max_length=45)
    longitude = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'location'


