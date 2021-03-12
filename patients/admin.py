from django.contrib import admin
from . models import Patient

# Register your models here.
class PatientModelAdmin(admin.ModelAdmin):
    list_display 		= ["user","active", "patient_name", "patient_id",  "heart_rate", "blood_pressure", "respiratory_rate", "temperature", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user", "patient_name"]
    list_editable		= ["active" , "heart_rate", "respiratory_rate", "blood_pressure", "temperature"]
    list_filter			= ["updated", "timestamp", "patient_id"]
    search_fields		= ["patient_name", "heart_rate", "patient_id"]
    class Meta:
        model = Patient
        
admin.site.register(Patient, PatientModelAdmin)