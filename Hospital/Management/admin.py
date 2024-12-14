from django.contrib import admin
from Management.models.user import User
from Management.models.patient import Patient
# Register your models here.
admin.site.register(User)
admin.site.register(Patient)