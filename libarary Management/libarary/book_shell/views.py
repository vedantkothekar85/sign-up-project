from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.


@csrf_exempt
def test(request):
    var = request.POST.get('name')
    return JsonResponse({'var': var})

@csrf_exempt
def signup(request):
    if request.method ==  "POST":
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        conf_pass = request.POST.get('conf_pass')
        
        send_data = New_signup(username=username, email=email, dob=dob, password=password, conf_pass=conf_pass)
        print(send_data)
        if len(password) == len(conf_pass) and password == conf_pass:
            send_data.save()
            return HttpResponse("success")
        
    return render(request, 'signup.html')

@csrf_exempt
def login(request):
    return HttpResponse("Login")
