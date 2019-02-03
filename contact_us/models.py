from django.db import models

# Create your models here.
class contact(models.Model):
    description=models.CharField(max_length=300, null=True)
    address=models.CharField(max_length=250, null=True)
    email=models.EmailField(max_length=250, null=True)
    phone_no=models.CharField(max_length=100, null=True)
    workingDay_start=models.CharField(max_length=100, null=True)
    workingDay_end = models.CharField(max_length=100, null=True)
    workingTime_start = models.IntegerField(null=True)
    workingTime_startZone = models.CharField(max_length=50, null=True)
    workingTime_end = models.IntegerField(null=True)
    workingTime_endZone = models.CharField(max_length=50, null=True)
    status=models.NullBooleanField(default=True)

    def __str__(self):
        return self.email

class contactMessages(models.Model):
    senderName=models.CharField(max_length=100, null=True)
    sender_phoneNo=models.CharField(max_length=100, null=True)
    sender_email=models.EmailField(max_length=100, null=True)
    msg_subject=models.CharField(max_length=150, null=True)
    msg=models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.senderName