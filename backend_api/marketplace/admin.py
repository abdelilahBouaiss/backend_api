from django.contrib import admin
from .models import BusinessAccount, TruckOffer, TransportRequest, AdminDashboard

admin.site.register(BusinessAccount)
admin.site.register(TruckOffer)
admin.site.register(TransportRequest)
admin.site.register(AdminDashboard)