#from django.http import HttpResponse
from django.shortcuts import render
import datetime


# Create a view for home
def home(request):
    if request.method== 'POST':
        check=request.POST['check']
        print(check)
    print("home function is called from view")
    #return HttpResponse("<h1>  This is my home page</h1>")
    return render(request,"home.html",{})

# Create a view for about
def about(request):
    isActive=True
    if request.method== 'POST':
        check= request.POST.get('check')
        print(check)
        if check is None: isActive= False
        else: isActive= True

    date= datetime.datetime.now()
    name="LearnDjangoforBackend"
    list_of_problems=[ 'Aptitude','Communication','Computerfundamental','CodingSkills']
    student={ 
        'std_name': "Shivam seth",
        'std_college': "REC Azamgarh",
        'std_city':  "Farrukhabad",
        'std_course': "Information Technology",
        'std_rollno':  1873613051,
        }
    
    print("about function is called from view")

    #dynamic data 
    data={
        'date': date,
        'isActive': isActive,
        'name': name,
        'list_of_problems': list_of_problems,
        'student_data': student,
    }
    #return HttpResponse("<h1>  This is my about page</h1>")
    return render(request,"about.html",data)


# Create a view for services
def services(request):
    print("services function is called from view")
    #return HttpResponse("<h1>  This is my services page</h1>")
    return render(request,"services.html",{})