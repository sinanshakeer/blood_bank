from django.db import models

# Create your models here.
class Camp(models.Model):
    camp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    details = models.CharField(max_length=45)
    date = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'camp'