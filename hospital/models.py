from django.db import models

# Create your models here.
class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    register_no = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    started_date = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'hospital'