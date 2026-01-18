from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta


class Donor(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    AVAILABILITY_STATUS = [
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.IntegerField()
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    district = models.CharField(max_length=50)
    upazila = models.CharField(max_length=50)
    last_donation_date = models.DateField()
    availability_status = models.CharField(max_length=15, choices=AVAILABILITY_STATUS, default='Available')
    registration_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.blood_group}"
    
    @property
    def days_since_last_donation(self):
        today = timezone.now().date()
        return (today - self.last_donation_date).days
    
    @property
    def is_eligible(self):
        return self.days_since_last_donation >= 90
    
    @property
    def eligibility_status(self):
        if self.is_eligible:
            return "Eligible to Donate"
        else:
            remaining_days = 90 - self.days_since_last_donation
            return f"Not Eligible ({remaining_days} days remaining)"
    
    class Meta:
        ordering = ['-registration_date']