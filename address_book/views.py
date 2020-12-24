from django.shortcuts import render, redirect
from .models import Address
from .forms import AddressForm
from django.contrib import messages


def home(request):
	all_addresses = Address.objects.all()
	return render(request, 'home.html', {"all_addresses":all_addresses})


def add_address(request):
	if request.method == "POST":
		form = AddressForm(request.POST or none)
		if form.is_valid():
			form.save()
			messages.success(request,("address has been added "))
			return redirect('home')
		else:
			messages.success(request,("there has been an error "))
			return render (request, 'add_address.html', {})
	else:
		return render (request, 'add_address.html', {})



def edit_address(request, list_id):
	

	if request.method == "POST":
		current_address = Address.objects.get(pk= list_id)
		form = AddressForm(request.POST or none, instance = current_address)
		if form.is_valid():
			form.save()
			messages.success(request,("address has been edited "))
			return redirect('home')
		else:
			messages.success(request,("there has been an error "))
			return render (request, 'edit_address.html', {})
	else:
		get_address = Address.objects.get(pk= list_id)
		return render (request, 'edit_address.html', {'get_address':get_address})



def delete_address(request, list_id):
	if request.method == "POST":
		current_address = Address.objects.get(pk= list_id)
		current_address.delete()
		messages.success(request,("item has been deleteed"))
		return redirect("home")
	else:
		return redirect ("home")
