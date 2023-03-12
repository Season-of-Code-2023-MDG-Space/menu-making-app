
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = "myapp"

urlpatterns = [
    path('', csrf_exempt(views.signupview),name='signup'),
    path('login/', csrf_exempt(views.Login),name='login'),
    path('next/next',views.Next,name='next'),
    path('next/profile',views.Profile,name='profile'),
    path('next/profile',views.Profile,name='profile'),
    path('next/createchart',views.Createchart,name='createchart'),
   # path('next/uploadmenu',views.Uploadmenu,name='uploadmenu'),
    path('next/uploadmenu', views.my_form, name='my_form'),
    path('next/delete/<int:id>', views.delete, name='delete'),
    path('next/delete2/<int:id>', views.delete2, name='delete2'),
    path('next/delete3/<int:id>', views.delete3, name='delete3'),
    path('next/delete4/<int:id>', views.delete4, name='delete4'),
    
]