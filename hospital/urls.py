from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("home/", hospital_home),
    path("add-patient/", add_patient),
    path("delete-patient/<int:patient_id>",delete_patient),
    path("update-patient/<int:patient_id>",update_patient),
    path("do-update-patient/<int:patient_id>",do_update_patient),
    path("feedback/",feedback),
   
]
 