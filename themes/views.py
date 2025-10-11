from django.shortcuts import render, redirect
from . models import Registrations
from django.contrib.messages import success, error

def index(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            client_data = Registrations.objects.create(name=name, email=email, mobile_number=phone, message=message)
            client_data.save()
            success_msg = 'Successfully Registered'
            success(request, success_msg)
            return redirect('index')
        except Exception as e:
            error_msg = 'Error While Registering'
            error(request, error_msg)
            return redirect('index')
    return render(request, 'index.html')