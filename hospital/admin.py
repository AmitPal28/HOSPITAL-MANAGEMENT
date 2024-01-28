from django.contrib import admin
from .models import Hospital
# Register your models here.

class HospitalAdmin(admin.ModelAdmin):
   # Use of Admin Customerize.
   list_display=('patient_name','patient_id','patient_number','patient_admit')
   list_editable=('patient_admit','patient_id')
   search_fields=('patient_name',)
   list_filter=('patient_admit',)


admin.site.register(Hospital,HospitalAdmin)