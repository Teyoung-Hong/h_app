from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    pass
    admin.site.register(Customer)

