from django.db import models
from django.contrib.auth.models import User

class OfferingCompany(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # other fields

class DemandingCompany(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # other fields