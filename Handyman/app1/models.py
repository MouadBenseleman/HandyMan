from django.db import models

# models.py
from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)


class MaintenanceTechnician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    experience_years = models.IntegerField()

class Contact(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    technician = models.ForeignKey(MaintenanceTechnician, on_delete=models.CASCADE)
    message = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


