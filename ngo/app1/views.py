from django.shortcuts import render
from .models import cause
# Create your views here.
def  index(request):
    cause1 = cause()
    cause1.name = "hrithiks fund"
    cause1.goal = 20000
    cause1.img = 'passion_1.png'
    cause1.raised = 15000

    cause2 = cause()
    cause2.name = "cause2"
    cause2.goal = 30000
    cause2.raised = 25000
    cause2.img = 'passion_2.png'


    cause3 = cause()
    cause3.name = "cause3"
    cause3.goal = 40000
    cause3.raised = 35000
    cause3.img = 'passion_3.png'

    
    causes = [cause1,cause2,cause3]
    return render(request, "index.html",{'causes':causes})

def education(request):
    return render(request, "education.html")

def  adopt(request):
    return render(request, "adopt.html")

def  health(request):
    return render(request, "health.html")

def  disaster(request):
    return render(request, "disaster.html")
    
def volunteer(request):
    return render(request,"volunteer_reg.html")


