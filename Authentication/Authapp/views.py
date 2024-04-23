from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

@login_required(login_url='log_in')
def home(request):
    return render(request,'home.html')

def register(request):
        form=UserCreationForm(request.POST)
        if request.method=="POST":
           if form.is_valid():
            form.save()
            messages.success(request,'register successfully!!!')
            
            return redirect('register')
        else:
                form=UserCreationForm()   
        return render(request,'auth/register.html',{'form':form}) 
    
    
def log_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
            
            
    return render(request,'auth/login.html')  

def log_out(request):
    logout(request)
    return redirect(log_in)

@login_required(login_url='log_in')
def change_password(request):
    cf=PasswordChangeForm(user=request.user)
    if request.method=="POST":
        cf=PasswordChangeForm(user=request.user,data=request.POST)
        if cf.is_valid():
            cf.save()
            return redirect('log_in')
            
    return render(request,'auth/change_password.html',{'cf':cf})


