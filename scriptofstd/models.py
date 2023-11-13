from django.db import models

# Create your models here.

class Scriptofstd(models.Model):
    script_usn = models.CharField(max_length=50)
    script_id = models.CharField(max_length=50) # primary/unique key
    script_subject_code = models.CharField(max_length=50)
    script_ist_marks = models.IntegerField(null=True)
    script_second_marks = models.IntegerField(null=True)
    script_final_marks = models.IntegerField(null=True)
    script_upload_datetime = models.DateTimeField(null=True)
    script_evaluation_date = models.DateTimeField(null=True)
    script_progress = models.CharField(max_length=50, null=True)
    script_pdf = models.FileField(upload_to='uploads/', null=True)
    script_evaluated_by = models.IntegerField(null=True)