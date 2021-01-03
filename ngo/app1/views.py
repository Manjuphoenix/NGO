from django.shortcuts import render, redirect
from .models import *
# Create your views here.

global value

def  index(request):
    '''cause1 = cause()
    cause1.name = "Deepak"
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
    cause3.img = 'passion_3.png'''
    count = int(Volunteer.objects.count())
    donCount = int(Donation.objects.count())
    event = int(Events.objects.count())

    value = 0
    don = 0
    donations = Donation.objects.all()
    for i in range(donCount):
        don = int(donations[i].amt) + don
    value = don

    
    #causes = [cause1,cause2,cause3]
    if request.method == "POST":
        FName = request.POST.get("fname")
        LName = request.POST.get("lname")
        Email = request.POST.get("email")
        Message = request.POST.get("message")
        form = Index.objects.create(fname = FName, lname = LName, email = Email, message = Message)
        print(FName + LName + Email + Message)
        form.save()
        return redirect("/")
    return render(request, "index.html",{ 'count': count, 'value': value, 'event': event})


def  adopt(request):
    if request.method == "POST":
        Name = request.POST.get("name")
        Address = request.POST.get("address")
        Phone = request.POST.get("phone")
        form = Adopt.objects.create(name = Name, address = Address, phone = Phone)
        form.save()
        return redirect("/")
    return render(request, "adopt.html")

def  donation(request):
    #count = int(Donation.objects.count())
    #print(count)
    #for i in range(count):
     #   print(Donation.amount[i])
    #print(amount)
    count = int(Donation.objects.count())
    value = 0
    donations = Donation.objects.all()
    if request.method == "POST":
        Name = request.POST.get("name")
        Phone = request.POST.get("phone")
        Mail = request.POST.get("mail")
        don = 0
        Amt = request.POST.get("amt")
        Nationality = request.POST.get("nationality")
        #amount = sum(Donation.amt)
        print(donations[0].amt)
        for i in range(count):
            don = int(donations[i].amt) + don
        value = don + int(Amt)
        print(don + int(Amt))
        form = Donation.objects.create(name = Name, phone = Phone, mail = Mail, amt = Amt, nationality = Nationality)
        form.save()
        return redirect("/")
    #print(amount)
    return render(request, "donation.html")

def  events(request):
    if request.method == "POST":
        Organizer = request.POST.get("organizer")
        Title = request.POST.get("eventName")
        Type = request.POST.get("type")
        Date = request.POST.get("date")
        Place = request.POST.get("place")
        form = Events.objects.create( eventName = Title, organizer = Organizer, eventType = Type, date = Date, place = Place )
        form.save()
        return redirect("/")
    return render(request, "events.html")
    
def volunteer(request):
    if request.method == "POST":
        #print('working')
        User_name = request.POST.get("name")
        Email = request.POST.get("mail")
        Phone = request.POST.get("phone")
        Country = request.POST.get("country")
        #print(User_name,Email,Phone,Country)
        form = Volunteer.objects.create(name = User_name, email = Email, phone = Phone, country = Country)
        form.save()
        return redirect("/")
    return render(request,"volunteer_reg.html")

def vollist(request):
    context = {}
    volunteers = Volunteer.objects.all()
    #Vol["name"] = volunteer.objects.all()
    vol = {
        "volunteers": volunteers
    }
    count = int(Volunteer.objects.count())
    print(volunteers[1])
    #vol1 = volunteers[0].name
    return render(request, "vollist.html", {"volunteers": volunteers, "vol": vol, 'count': count})