from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=10, null=True)
    full_name = models.CharField(max_length=100, blank=True)  # Allow blank to handle missing data
    mobile = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], null=True)
    birthdate = models.DateField( null=True)

class ContactForm(models.Model):
    user_profile = models.ForeignKey(User_Profile, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)