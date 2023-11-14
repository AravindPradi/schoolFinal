from django.shortcuts import render, redirect
from django.http import JsonResponse

from credentials.models import UserProfile
from .forms import RegistrationForm
from .models import Branch, District
import json


def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user_profile,created = UserProfile.objects.get_or_create(user=request.user)
            user_profile.form_filled = True
            user_profile.save()
            message = "Application Accepted"
            if message == "Application Accepted":
                return render(request,'new.html')
        else:
            message = "Application Submission Failed"
    else:
        form = RegistrationForm()
        message = ""
    return render(request, 'regsform.html', {'form': form,'message': message })


def branch(request):
    data = json.loads(request.body)
    branches = Branch.objects.filter(district__id=data['user_id'])
    print(branches)
    return JsonResponse(list(branches.values("id", "name")), safe=False)



