from django.contrib import admin
from .models import person,insurance_dt,medical_history,current_status
# Register your models here.
admin.site.register(person)
admin.site.register(insurance_dt)
admin.site.register(medical_history)
admin.site.register(current_status)