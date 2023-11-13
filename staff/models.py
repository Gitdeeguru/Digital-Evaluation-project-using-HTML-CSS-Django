from django.db import models

# Create your models here.

class Staff(models.Model):
    staff_name = models.CharField(max_length=50)
    staff_id = models.IntegerField() # primary/unique key
    staff_branch = models.CharField(max_length=50)
    staff_gender = models.CharField(max_length=10)
    staff_password = models.CharField(max_length=50)