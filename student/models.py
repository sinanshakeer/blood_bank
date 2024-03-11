from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    admission_no = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    course = models.CharField(max_length=45)
    year = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    dob = models.DateField()
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    bloodgroup = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'student'

