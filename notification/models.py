from django.db import models

# Create your models here.
class Notifiaction(models.Model):
    notifiaction_id = models.AutoField(primary_key=True)
    notification = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = True
        db_table = 'notifiaction'