from django.shortcuts import render
from django.db import models
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from members.models import Company
from members import forms


def joinus(request):	
	context_dict={}
	if request.method =='POST':
		name=request.POST.get('name')
		contact=request.POST.get('contact')
		ad1=request.POST.get('ad1')
		ad2=request.POST.get('ad2')
		city=request.POST.get('city')
		properties=request.POST.get('properties')


		try:
			x=Company(name=name, contact=contact, ad1=ad1, ad2=ad2, city=city , properties=properties)
			x.full_clean()
			x.save()
		except Exception,e:
			return HttpResponse(e)

		context_dict['name']=name
		context_dict['contact']=contact
		context_dict['ad1']=ad1
		context_dict['ad2']=ad2
		context_dict['city']=city
		context_dict['properties']=properties	
		return render(request, "response.html" , context_dict)
	else:
		return render(request, "form.html" , context_dict)


def home(request):
	return render(request, "home.html" , {})


def search(request):
	context_dict={}
	if request.method == 'GET':
		s = request.GET['search']
		try:
			x=Company.objects.filter(properties__icontains=s)
			
			context_dict['data']=x
			return render(request, "result.html",context_dict)
		except Exception,e:
			return HttpResponse(e)


#form_data = forms.AddCompany(request.POST or None)
	
	# if form_data.is_valid():
	# 	ko=Company.objects.create()
	# 	ko.name=form_data.cleaned_data['name']
	# 	ko.contact=form_data.cleaned_data['contact']
	# 	ko.ad1=form_data.cleaned_data['ad1']
	# 	ko.ad2=form_data.cleaned_data['ad2']
	# 	ko.city=form_data.cleaned_data['city']
	# 	ko.properties=form_data.cleaned_data['properties']
	# 	ko.save()	

	# context = {'addcompany':form_data}
	# return render(request, 'form.html', context)