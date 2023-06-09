from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')



def about(request):
    if request.method == 'post':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,

        }
        message = '''
        New message{}
        from{}
        
        
        '''
        format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['smazigah@gmail.com'])
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def forgot(request):
    return render(request, 'forgot.html')


def services(request):
    return render(request, 'services.html')


def logout_view(request):
    logout(request)
    return redirect('index')
