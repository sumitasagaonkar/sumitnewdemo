from django.forms import ModelForm
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *



class contactUsForm(ModelForm):
	class Meta:
		model = contactUs
		fields = ('customer','status','message')

		widgets = {
		'customer': forms.TextInput(attrs={'class':'form-control'}),
		'status': forms.Select(attrs={'class':'form-control'}),
		'message': forms.Textarea(attrs={'class':'form-control'}),
		}


		
class AskQuaForm(ModelForm):
	class Meta:
		model = AskQua
		fields = '__all__'

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ('name','Last_name','phone','email','adress')
		exclude = ['user']

		widgets = {
		'name': forms.TextInput(attrs={'class':'form-control'}),
		'Last_name': forms.TextInput(attrs={'class':'form-control'}),
		'phone': forms.TextInput(attrs={'class':'form-control'}),
		'email': forms.TextInput(attrs={'class':'form-control'}),
		'adress': forms.Textarea(attrs={'class':'form-control'}),
		}

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'











