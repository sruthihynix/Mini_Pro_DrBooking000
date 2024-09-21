from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Patient,Doctor,booking
from django.utils import timezone
from django.utils.dateparse import parse_datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
	return render(request, 'signup.html') #in signup goto register fun and register details

# after user regn it connect to login page
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # name of patient
        age = request.POST.get('age')
        contact = request.POST.get('contact')
        uname = request.POST.get('username')
        pwd1 = request.POST.get('password1')
        pwd2 = request.POST.get('password2')  # confirm pwd
        print(name)
        if pwd1 != pwd2:
            return HttpResponse("Password do not match")
        else:
            # model name:Patient
            # Create and save the dr_book ob
            patient = Patient(p_name=name, p_age=age, p_contact=contact, p_uname=uname, p_pwd=pwd1)
            patient.save()
        return HttpResponse("User registured sucesssfully")
    # return redirect('login')
    return render(request, 'login.html')


def loginpage(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        print(uname)
        check_patient=Patient.objects.filter(p_uname=uname,p_pwd=pwd)
        print(check_patient)
        if check_patient:
            request.session['p_username']=uname # session
            return redirect('booking') # here go to booking page
        else:
            return HttpResponse("invalid username")
    return render(request, 'login.html')


def bookingPage(request):
    if request.method == 'POST':
        d_name = request.POST.get('d_name')
        p_name = request.POST.get('p_name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        contactno = request.POST.get('contactno')
        description = request.POST.get('description')

        # Simple validation
        if not all([d_name, p_name, date , time, contactno, description]):
            return HttpResponse("All fields are required.")

        try:
            # Create and save the booking object- booking_info
            booking_info = booking(
                d_name=d_name,
                p_name=p_name,
                date=date,
                time=time,
                contactno=contactno,
                description=description
            )
            booking_info.save()
            return HttpResponse("Booking details submitted successfully!")
            # messages.success(request, "Booking details submitted successfully!")
            return redirect('index')  # Redirect to index or any other page
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}")

    return render(request, 'booking.html')


# doctor can view patient appointment list when dr  login
def appo_list(request):
    # Retrieve all booking entries
    appointments = booking.objects.all()
    return render(request, 'appo.html', {'appointments': appointments})
