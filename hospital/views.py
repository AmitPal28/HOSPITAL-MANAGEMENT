from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Hospital
from .form import FeedbackForm

# Create your views here.
def hospital_home(request):

    patients=Hospital.objects.all()
    return render(request,"hospital/home.html",{
        'patients' : patients
        })


def add_patient(request):
    if request.method=="POST":
        
        #datafetch
        patientName=request.POST.get("patientName")
        patientId=request.POST.get("patientId")
        patientNumber=request.POST.get("patientNumber")
        patientAddress=request.POST.get("patientAddress")
        patientAdmit=request.POST.get("patientAdmit")
        patientWard=request.POST.get("patientWard")
         
         #validate
        

        #create model object and set the data
        h=Hospital()
        h.patient_name=patientName
        h.patient_id=patientId
        h.patient_number=patientNumber
        h.patient_address=patientAddress
        h.patient_ward=patientWard

        if patientAdmit is None:
            h.patient_admit=False
        else:
            h.patient_admit=True


        #save the object
        h.save()
        
        #prepare msg
        print("Data is coming..")
        return redirect("/hospital/home/")
    return render(request,"hospital/add_patient.html",{})



def delete_patient(request,patient_id):
    #print(patient_id)
    patient=Hospital.objects.get(pk=patient_id)
    patient.delete()
    return redirect("/hospital/home/")


def update_patient(request,patient_id):
    #print(patient_id)
    patient=Hospital.objects.get(pk=patient_id)
    return render(request,"Hospital/update_patient.html", {
        'patient':patient
    })


#used for update handler
def do_update_patient(request,patient_id):
    if request.method=='POST':
         #datafetch
        patientName=request.POST.get("patientName")
        patientId=request.POST.get("patientId")
        patientNumber=request.POST.get("patientNumber")
        patientAddress=request.POST.get("patientAddress")
        patientAdmit=request.POST.get("patientAdmit")
        patientWard=request.POST.get("patientWard")
         
        p=Hospital.objects.get(pk=patient_id)
        #create model object and set the data
        p.patient_name=patientName
        p.patient_id=patientId
        p.patient_number=patientNumber
        p.patient_address=patientAddress
        p.patient_ward=patientWard

        if patientAdmit is None:
            p.patient_admit=False
        else:
            p.patient_admit=True

        p.save()
    return redirect("/Hospital/home/")


def feedback(request):
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
           # form.save() ---Not work ---
            print(form.cleaned_data['email'])
            print(form.cleaned_data['name'])
            print(form.cleaned_data['feedback'])

            print("Data saved !..")
        else:
            return render(request,"hospital/feedback.html",{'form':form})

    else:
        form = FeedbackForm()
    return render(request,"hospital/feedback.html",{'form':form})