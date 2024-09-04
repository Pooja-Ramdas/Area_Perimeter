from django.shortcuts import render , redirect
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def loginreq(request):
    if request.method == "POST":
        username = request.POST['loginusername']
        password = request.POST['loginpassword']
        
        loginUser = authenticate(request , username = username , password = password)
        if loginUser is not None:
            userl = login(request , loginUser)
            messages.success(request , "You are successfully logged in !")
            return redirect('/')
        else:
            messages.info(request , "Username or Password is incorrect !")
            return redirect('login')
    else:
        return render(request , 'login.html')
    
def logoutreq(request):
    logout(request)
    messages.success(request, "Logged out successfully !")
    return redirect('/')