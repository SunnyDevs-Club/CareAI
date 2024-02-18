from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    full_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.PROTECT)
    organization = models.ForeignKey(Organization, related_name='organizations',  on_delete=models.PROTECT)
    rating = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    phone_number = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='doctor_photos/')
    latitude = models.DecimalField(max_digits=12, decimal_places=6)
    longitude = models.DecimalField(max_digits=12, decimal_places=6)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('A', 'Approved'),
        ('P', 'Pending'),
        ('R', 'Rejected')
    ]
        
    doctor = models.ForeignKey(Doctor, related_name='appointments',  on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name='appointments', on_delete=models.PROTECT)
    date_time = models.DateTimeField()
    symptoms_desc = models.TextField(null=True, blank=True)
    mri_image = models.ImageField(upload_to='mri_images/', null=True, blank=True)
    x_ray_image = models.ImageField(upload_to='xray_images/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='P')
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name()


