from django.shortcuts import render,redirect
from .forms import signupform
from .forms import NormalVeggie, GravyVeggie, SnacksMany, SweetsMany, MenuItemForm, CreateNewChart
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .models import Normal, Gravy, Sweets, Snacks, MenuItem, Post, MenuName, Charts
from django.http import HttpResponse, HttpResponseRedirect, response
from django.urls import reverse_lazy
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import requests
from spoonacular import API
import json

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
            return redirect('myapp:profile')

    return render(request, 'login.html')
    
def Next(request):
    return render(request, 'next.html')

def Profile(request):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    meals = ['Breakfast', 'Lunch', 'Dinner']
    menu_chart = {}

    for day in days:
            menu_chart[day] = {}
            for meal in meals:
                menu_avialable = MenuItem.objects.filter(day=day[:3].lower(), meal=meal.lower(), owner=request.user)
                if menu_avialable:
                    menu_chart[day][meal] = menu_avialable[0].item
                else:
                    menu_chart[day][meal] = '-'
    return render(request, 'profile.html', {"menu_chart":menu_chart})

    

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
    if form1.is_valid() and form1.cleaned_data['fullname']:
        normall = form1.save(commit=False)
        normall.owner = request.user
        normall.save()
        
    
    context['form1']= form1
    context["dataset1"] = Normal.objects.filter(owner=request.user)

    if form2.is_valid() and form2.cleaned_data['gravy']:
        gravyy = form2.save(commit=False)
        gravyy.owner = request.user
        gravyy.save()
        
    
    context['form2']= form2
    context["dataset2"] = Gravy.objects.filter(owner=request.user)

    if form3.is_valid() and form3.cleaned_data['snacks']:
        snackss = form3.save(commit=False)
        snackss.owner = request.user
        snackss.save()
        
    
    context['form3']= form3
    context["dataset3"] = Snacks.objects.filter(owner=request.user)
    if form4.is_valid() and form4.cleaned_data['sweets']:
        sweetss = form4.save(commit=False)
        sweetss.owner = request.user
        sweetss.save()
        
    
    context['form4']= form4
    context["dataset4"] = Sweets.objects.filter(owner=request.user)


    # api = API('57fbffe56b594046b1a92aeaeabb3145')
    # query = request.GET.get('query')
    # results = api.search_recipes_complex(query=query)
    # context['parsed_results'] = json.loads(results)
    
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

def back_to_login(request):
    return HttpResponseRedirect(reverse_lazy('myapp:login'))



def menu(request):
    
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            all = form.save(commit=False)
            all.owner = request.user
            all.save()
            
            return redirect('myapp:menu')
    else:
        form = MenuItemForm()
    menu_item = MenuItem.objects.filter(owner=request.user)

    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    meals = ['Breakfast', 'Lunch', 'Dinner']
    menu_chart = {}

    for day in days:
            menu_chart[day] = {}
            for meal in meals:
                menu_avialable = MenuItem.objects.filter(day=day[:3].lower(), meal=meal.lower(), owner=request.user)
                if menu_avialable:
                    menu_chart[day][meal] = menu_avialable[0].item
                else:
                    menu_chart[day][meal] = '-'


    context = {}
    context["dataset1"] = Normal.objects.filter(owner=request.user)
    context["dataset2"] = Gravy.objects.filter(owner=request.user)
    context["dataset3"] = Snacks.objects.filter(owner=request.user)
    context["dataset4"] = Sweets.objects.filter(owner=request.user)

    return render(request, 'menu.html', {'form': form, 'menu_item': menu_item, 'menu_chart': menu_chart, 'context':context})

#def NewChart(request, id):
    ls = MenuName.objects.get(owner=request.user, id=id)

    if request.method == "POST":
        if request.POST.get("newitem"):
           d = request.POST.get("newd")
           m = request.POST.get("newm")
           i = request.POST.get("newi")

           ls.item_set.create(day=d, meal=m, item=i)

    return render(request, "newchart.html", {"ls":ls})

def deletemenu(request, id):
    menuone = MenuItem.objects.get(id=int(id))
    menuone.delete()
    return HttpResponseRedirect(reverse_lazy('myapp:menu'))

def post_it(request):
    
    charts = ['chart1', 'chart2', 'chart3', 'chart4']
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    meals = ['Breakfast', 'Lunch', 'Dinner']
    for day in days:
        #menu_chart[day] = {}
        for meal in meals:
            menu_avialable = MenuItem.objects.filter(day=day[:3].lower(), meal=meal.lower(), owner=request.user)
            if menu_avialable:
                 postdata = Post(day=day, meal=meal, item=menu_avialable[0].item, owner=request.user)
                 postdata.save()
            else:
                postdata = Post(day=day, meal=meal, item="-", owner=request.user)
                postdata.save()


    menu_chart = {}
    for day in days:
        menu_chart[day] = {}
        for meal in meals:
            menu_items = Post.objects.filter(day=day[:3].lower(), meal=meal.lower(), owner=request.user)
            if menu_items:
                menu_chart[day][meal] = menu_items[0].item
            else:
                menu_chart[day][meal] = '-'

    post_data_list = Post.objects.filter(owner=request.user)
    print(post_data_list)
    return render(request, 'profile.html', {'menu_chart':menu_chart})


def automatic(request):
    menu_item = MenuItem.objects.filter(owner=request.user)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    meals = ['Breakfast', 'Lunch', 'Dinner']
    menu_chart = {}
    for day in days:
        menu_chart[day] = {}
        for meal in meals:
            menu_avialable_snacks = Snacks.objects.filter(owner=request.user)
            menu_avialable_garvy = Gravy.objects.filter(owner=request.user)
            menu_avialable_normal = Normal.objects.filter(owner=request.user)
            menu_avialable_sweets = Sweets.objects.filter(owner=request.user)
            i = 0
            if menu_avialable_snacks and meal=='Breakfast':
                
                menu_chart[day][meal] = menu_avialable_snacks[i].snacks
                i = i + 1
                
            elif menu_avialable_normal and meal=='Lunch':
                menu_chart[day][meal] = menu_avialable_normal[0].fullname
            
            elif menu_avialable_garvy and meal=='Dinner' and (day=='Monday' or day=='Wednesday' or day=='Friday' or day=='Sunday'):
                menu_chart[day][meal] = menu_avialable_garvy[0].gravy
            
            elif menu_avialable_normal and meal=='Dinner' and (day=='Tuesday' or day=='Thursday' or day=='Saturday'):
                menu_chart[day][meal] = menu_avialable_normal[0].fullname
            else:
                menu_chart[day][meal] = '-'
    return render(request, 'menu.html', {'menu_item': menu_item ,'menu_chart': menu_chart})