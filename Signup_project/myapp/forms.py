from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Normal, Gravy, Sweets, Snacks, Breakfast, MenuItem, Post, MenuName, Charts

class signupform(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)

    class meta:
        model = User
        fields=('username','password1','password2','email','first_name','last_name')

    def save(self,commit=True):
        user = super(signupform,self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class GravyVeggie(forms.ModelForm):
  class Meta:
       model = Gravy
       fields = ["gravy",]
       labels = {'gravy': "ADD NEW DISH",}
       widgets = {'owner': forms.HiddenInput()}
       required = {
           "gravy":False,
       }

class SnacksMany(forms.ModelForm):
  class Meta:
       model = Snacks
       fields = ["snacks",]
       labels = {'snacks': "ADD NEW DISH",}
       widgets = {'owner': forms.HiddenInput()}
       required = {
           "snacks":False,
       }

class SweetsMany(forms.ModelForm):
  class Meta:
       model = Sweets
       fields = ["sweets",]
       labels = {'sweets': "ADD NEW DISH",}
       widgets = {'owner': forms.HiddenInput()}
       required = {
           "sweets":False,
       }

class NormalVeggie(forms.ModelForm):
  class Meta:
       model = Normal
       fields = ["fullname",]
       labels = {'fullname': "ADD NEW DISH",}
       widgets = {'owner': forms.HiddenInput()}
       required = {
           "fullname":False,
       }

class Morning(forms.ModelForm):
    class Meta:
      model = Breakfast
      fields = ["breakfast"]
      widgets = {'owner': forms.HiddenInput()}
      
class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = [ 'day', 'meal', 'item']
        widgets = {'owner': forms.HiddenInput()}


class CreateNewChart(forms.ModelForm):
    class Meta:
        model = MenuName
        fields = ['name_of_chart']
        widgets = {'owner': forms.HiddenInput()}