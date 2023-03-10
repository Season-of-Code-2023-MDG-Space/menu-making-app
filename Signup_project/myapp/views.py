from django.shortcuts import render,redirect
from .forms import signupform
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login


@csrf_exempt

# Create your views here.

def signupview(request):
    if request.method=='POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = signupform()
    return render(request, 'signup.html',{'form':form})


def Login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('next')
    else:
        return render(request, 'login.html')
    
def Next(request):
    return render(request, 'next.html')

def Profile(request):
    return render(request, 'profile.html')

def Createchart(request):
    return render(request, 'createchart.html')

def Uploadmenu(request):
    return render(request, 'uploadmenu.html')