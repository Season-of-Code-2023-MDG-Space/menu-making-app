from django.shortcuts import render,redirect
from .forms import signupform
from .forms import NormalVeggie, GravyVeggie, SnacksMany, SweetsMany
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .models import Normal, Gravy, Sweets, Snacks
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.template import loader

@csrf_exempt

# Create your views here.

def signupview(request):
    if request.method=='POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:login')
        
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
    return render(request, 'login.html')
    
def Next(request):
    return render(request, 'next.html')

def Profile(request):
    return render(request, 'profile.html')

def Createchart(request):
    context={}
    context["dataset1"] = Normal.objects.all()
    context["dataset2"] = Gravy.objects.all()
    context["dataset3"] = Snacks.objects.all()
    context["dataset4"] = Sweets.objects.all()
    
    return render(request, 'createchart.html', context)

#def Uploadmenu(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Categories(name=n)
            t.save()

        
    else:
        form = CreateNewList()
    return render(request, 'uploadmenu.html', {"form":form})

#def index(request, id):
    ls = Categories.objects.get(id=id)
    
    if request.method == "POST":
        print(request.POST)
        if request.POST.get("save"):
            for item in ls.items_set.all:
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif request.POST.get("newItem"):
            txt = request.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")

    return render(request, "list.html",{"ls":ls})

def my_form(request):
    context = {}
    form1 = NormalVeggie(request.POST or None)
    form2 = GravyVeggie(request.POST or None)
    form3 = SnacksMany(request.POST or None)
    form4 = SweetsMany(request.POST or None)
    if form1.is_valid():
        form1.save()

    context['form1']= form1
    context["dataset1"] = Normal.objects.all()

    if form2.is_valid():
        form2.save()

    context['form2']= form2
    context["dataset2"] = Gravy.objects.all()

    if form3.is_valid():
        form3.save()

    context['form3']= form3
    context["dataset3"] = Snacks.objects.all()
    
    if form4.is_valid():
        form4.save()

    context['form4']= form4
    context["dataset4"] = Sweets.objects.all()
    template = loader.get_template('uploadmenu.html')
    return HttpResponse(template.render(context, request)) 

#def my_form_view(request):
   # context = {}
    #context["dataset"] = Normal.objects.all()

    #return render(request, "uploadmenu.html", context)

def delete(request, id):
    normalone = Normal.objects.get(id=int(id))
    normalone.delete()
    return HttpResponseRedirect(reverse_lazy('myapp:my_form'))

def delete2(request, id):
    gravyone = Gravy.objects.get(id=int(id))
    gravyone.delete()
    return HttpResponseRedirect(reverse_lazy('myapp:my_form'))

def delete3(request, id):
    snacksone = Snacks.objects.get(id=int(id))
    snacksone.delete()
    return HttpResponseRedirect(reverse_lazy('myapp:my_form'))

def delete4(request, id):
    sweetsone = Sweets.objects.get(id=int(id))
    sweetsone.delete()
    return HttpResponseRedirect(reverse_lazy('myapp:my_form'))