from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
# Create your views here.
from django.http import HttpResponse
from .models import *
from .forms import contactUsForm,AskQuaForm,CustomerForm,OrderForm
from django.forms import inlineformset_factory

def index(request):
    return render(request, 'index.html') 
    
@login_required
def constact(request):
    return render(request, 'conn.html')
@login_required
def constactPage(request):
	#customer = request.user.customer
	#customer = Customer.objects.get(id=pk)
	#form = contactUsForm(initial={'customer':customer})



	OrderFormSet = inlineformset_factory(Customer, contactUs, fields=('frist_name','Last_name','status', 'message'), extra=1,widgets = {
		'customer': forms.TextInput(attrs={'class':'form-control'}),
		'frist_name': forms.TextInput(attrs={'class':'form-control'}),
		'Last_name': forms.TextInput(attrs={'class':'form-control'}),
		'status': forms.Select(attrs={'class':'form-control'}),
		'message': forms.Textarea(attrs={'class':'form-control'}),
		} )
	customer = Customer.objects.get(id =request.user.customer.id)
	formset = OrderFormSet(queryset=contactUs.objects.none(),instance=customer)



	if request.method == 'POST':
		print('Printing POST:', request.POST)
		formset = OrderFormSet(request.POST,instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('index')






	# if request.method == 'POST':
	# 	form = contactUsForm(request.POST, request.FILES,instance=customer)
	# 	if form.is_valid():
	# 		form.save()

	context = {'form':formset}
	return render(request, 'constact.html', context)
@login_required
def OrderbookPage(request):
    return render(request, 'orderbook.html')
@login_required
def askquaPage(request):
	OrderFormSet = inlineformset_factory(Customer, AskQua, fields=('full_name','Question','status'), extra=1,widgets = {
		'full_name': forms.TextInput(attrs={'class':'form-control'}),
		'status': forms.Select(attrs={'class':'form-control'}),
		'Question': forms.Textarea(attrs={'class':'form-control'}),
		
		}  )
	customer = Customer.objects.get(id =request.user.customer.id)
	formset = OrderFormSet(queryset=AskQua.objects.none(),instance=customer)

	aksquadata = customer.askqua_set.all()
	if request.method == 'POST':
		print('Printing POST:', request.POST)
		formset = OrderFormSet(request.POST,instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('index')

	context = {'form':formset, 'aksquadata':aksquadata}
	return render(request, 'aksqua.html',context)




@login_required
def profilePage(request):

	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()
			return redirect('setting')

	context = {'form':form}
	return render(request, 'profileform.html',context)
@login_required
def settingsPage(request):

	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product',), extra=1 ,widgets = {
		
		'product': forms.Select(attrs={'class':'form-control'}),
		} )
	customer = Customer.objects.get(id =request.user.customer.id)
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	#form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('index')

	context = {'form':formset}
	return render(request,'setting.html',context)

@login_required
def profilesettingPage(request):

	customer = Customer.objects.get(id =request.user.customer.id)
	orderss = customer.order_set.all()










	context ={'orderss' : orderss}
	return render(request,'profile.html',context)

def logoutUser(request):
	

	return redirect('index')