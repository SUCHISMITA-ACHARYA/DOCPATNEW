from django.contrib import admin
from .models import User, Record, Patient
# Register your models here.
admin.site.register(User)
admin.site.register(Record)
admin.site.register(Patient)