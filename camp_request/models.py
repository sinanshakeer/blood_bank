from django.db import models
from camp.models import Camp
# Create your models here.
class CampRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    # camp_id = models.IntegerField()
    camp=models.ForeignKey(Camp,on_delete=models.CASCADE)
    request = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'camp_request'