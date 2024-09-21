from django.db import models
from django.utils import timezone  # Import timezone

# DB- dr_book

# Create your models here.
class Doctor(models.Model):
    d_name=models.CharField(max_length=50)
    d_email=models.EmailField()
    d_contact=models.IntegerField()
    d_uname=models.CharField(max_length=25)
    d_pwd=models.IntegerField()

    class Meta:
        db_table = "doctor"

    def __str__(self):
        return self.d_name

class Patient(models.Model):

    p_name=models.CharField(max_length=50)
    p_contact=models.IntegerField()
    p_age = models.IntegerField()
    p_uname=models.CharField(max_length=25)
    p_pwd=models.CharField(max_length=100)
    class Meta:
        db_table = "patient"

    def __str__(self):
        return self.p_name


class booking(models.Model):
    d_name= models.CharField(max_length=50)
    p_name=models.CharField(max_length=50)
    date=models.DateField(default=timezone.now,null=True,blank=True)
    time=models.TimeField(null=True,blank=True)
    # datetime=models.DateTimeField()
    contactno=models.IntegerField()
    description=models.CharField(max_length=250)
    class Meta:
        db_table = "booking"
    def __str__(self):
        return self.p_name


