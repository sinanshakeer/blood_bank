from django.db import models

# Create your models here.
class Awareness(models.Model):
    awareness_id = models.AutoField(primary_key=True)
    awareness = models.CharField(max_length=45)      
    date = models.DateField()
    time = models.TimeField()
    details = models.CharField(max_length=45)        

    class Meta:
        managed = True
        db_table = 'awareness'