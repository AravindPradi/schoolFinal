from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from credentials.models import UserProfile


# Create your views here
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if username == "":
            if password == "" and cpassword == "":
                messages.info(request,'Fill all the  Fields')
                return redirect('credentials:register')
            elif password != "" and cpassword != "":
                messages.info(request, 'Fill all the  Fields')
                return redirect('credentials:register')
        elif username != "":
            if password == "" and cpassword == "":
                messages.info(request, 'Fill all the  Fields')
                return redirect('credentials:register')
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('credentials:login')
        else:
            messages.info(request, "Password not Matching")
            return redirect('credentials:register')

    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            if user_profile.form_filled:
                return redirect('ebankapp:index')
            else:
                return redirect('credentials:alogin')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('credentials:login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def alogin(request):
    return render(request, 'alogin.html')
