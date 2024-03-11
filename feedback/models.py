from django.db import models
from student.models import Student

# Create your models here.
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    # student_id = models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'feedback'