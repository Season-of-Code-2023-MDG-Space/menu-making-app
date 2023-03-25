
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = "myapp"

urlpatterns = [
    path('signup/', csrf_exempt(views.signupview),name='signup'),
    path('', csrf_exempt(views.Login),name='login'),
    path('signup/login',views.back_to_login ,name='back_to_login' ),
    path('next/next',views.Next,name='next'),
    path('next/profile',views.Profile,name='profile'),
    path('next/profile/',views.Profile,name='profile'),
    path('next/createchart',views.menu,name='menu'),
    path('next/menu',views.menu,name='menu'),
    #path('next/menu_list',views.menu_chart,name='menu_chart'),
   # path('next/uploadmenu',views.Uploadmenu,name='uploadmenu'),
    path('next/uploadmenu/', views.my_form, name='my_form'),
    path('next/logout', views.back_to_login, name='back_to_login'),
    path('next/uploadmenu/delete/<int:id>', views.delete, name='delete'),
    path('next/uploadmenu/delete2/<int:id>', views.delete2, name='delete2'),
    path('next/uploadmenu/delete3/<int:id>', views.delete3, name='delete3'),
    path('next/uploadmenu/delete4/<int:id>', views.delete4, name='delete4'),
    path('next/deletemenu/<int:id>', views.deletemenu, name='deletemenu'),
    path('next/post_it', views.post_it, name='post_it'),
    path('next/automatic', views.automatic, name='automatic'),
    
]