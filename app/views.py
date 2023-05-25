from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Student


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')  # Replace 'home' with the appropriate URL name for your home page
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'login.html')
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username taken')
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

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def addStudent(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        mail_id = request.POST['mail_id']
        address = request.POST['address']
        department = request.POST['department']
        courses = request.POST['courses']
        purpose = request.POST['purpose']

        student = Student(name=name, dob=dob, age=age, gender=gender, phone_number=phone_number,
                          mail_id=mail_id, address=address, department=department, courses=courses,
                          purpose=purpose)
        student.save()
        messages.success(request, 'Details submitted successfully')

        return redirect('dashboard')  # Redirect to a success page after saving the data

    return render(request, 'dashboard.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
