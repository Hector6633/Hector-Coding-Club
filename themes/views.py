from django.shortcuts import render, redirect
from . models import Registrations
from django.contrib.messages import success, error
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            client_data = Registrations.objects.create(name=name, email=email, mobile_number=phone, message=message)
            client_data.save()
            subject = "Hector Coding Club"
            message = f"Dear {name},\nThank You for your registration with Hector Coding Club. We will get back to you as soon as possible. Your registration details are as follows:\nName: {name}\nEmail: {email}\nMobile Number: {phone}\nThis is an automated email.\nPlease keep this email for your records and do not forward or share any other person.\nTo get started, please visit our website at https://hectorclub.pythonanywhere.com/ and use our services.\nBest regards,\nHector Coding Club"
            recipient = email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [recipient],
                fail_silently=False,
            )
            success_msg = 'Successfully Registered'
            success(request, success_msg)
            return redirect('index')
        except Exception as e:
            error_msg = 'Error While Registering'
            error(request, error_msg)
            return redirect('index')
    return render(request, 'index.html')