from django.db import models

# Business Account Model
class BusinessAccount(models.Model):
    TRANSPORTER = 'TR'
    CLIENT = 'CL'
    BUSINESS_TYPE_CHOICES = [
        (TRANSPORTER, 'Transporter'),
        (CLIENT, 'Client'),
    ]
    business_name = models.CharField(max_length=255)
    business_type = models.CharField(
        max_length=2,
        choices=BUSINESS_TYPE_CHOICES,
        default=TRANSPORTER,
    )
    email = models.EmailField()
    password = models.CharField(max_length=255)
    contact_info = models.TextField()

# Truck Offer Model
class TruckOffer(models.Model):
    business = models.ForeignKey(BusinessAccount, on_delete=models.CASCADE)
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability_status = models.BooleanField(default=True)

# Transport Request Model
class TransportRequest(models.Model):
    business = models.ForeignKey(BusinessAccount, on_delete=models.CASCADE)
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)

# Admin Dashboard Model
class AdminDashboard(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
