from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout





def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['PassWord1']
        password2 = request.POST['PassWord2']
        if(password1!=password2):
            return HttpResponse("Password does not match")
        my_user = User.objects.create_user(username, email, password1)
        my_user.save()
        return redirect('login')
    return render(request,'signup.html')

def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        pass1 = request.POST['password1']
        print(username, pass1)
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return render(request, "R.html")
        else:
            return HttpResponse("Invalid username or password")
    return render(request, 'login.html')

@login_required(login_url='login') # This is a decorator
def logout_view(request):
    logout(request)
    return redirect('/')


def index(request):
    return render(request, 'home.html')

def Resume(request):
    return render(request, 'resume.html')
def Projects(request):
    return render(request, 'Projects.html')
def About(request):
    return render(request, 'About.html')
def soon(request):
    return render(request, 'uploadedSoon.html')

# @login_required(login_url='login') # This is a decorator
# def Magic(request):
#     return render(request, 'Magic.html')

