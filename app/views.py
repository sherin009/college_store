from django.contrib import auth, messages
from django.shortcuts import render, redirect
from .models import User
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')


    return render(request, 'login.html')



def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']

        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username):
                messages.info(request, 'Username Taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Registered successfully')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    return render(request, 'login.html')



def new_page(request):
    return render(request, 'new_page.html')


