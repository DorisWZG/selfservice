from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	#return HttpResponse("Hello, world!")
	#return render_to_string('default_web/index.html',{})
	return render(request, 'default_web/index.html', {})

def product_and_service(request):
	return render(request, 'default_web/pns.html',{})

def about(request):
	return render(request, 'about.html',{})

def member_service(request):
	return render(request, 'member_service.html',{})

def contact(request):
	return render(request, 'contact.html',{})

def education_case(request):
	return render(request, 'default_web/education_case.html',{})
def destination_mkt_case(request):
	return render(request, 'default_web/destination_mkt_case.html',{})
def real_estate_case(request):
	return render(request, 'default_web/real_estate_case.html',{})
def high_tech_case(request):
	return render(request, 'default_web/high_tech_case.html',{})


def market_test(request):
	return render(request, 'default_web/stage1_test.html', {})
def stage1_result(request):
	return render(request, 'default_web/stage1_result.html', {})

def budget_allocation_test(request):
	return render(request, 'default_web/stage2_test.html', {})
def stage2_result(request):
	return render(request, 'default_web/stage2_result.html', {})

def wave_test(request):
	return render(request, 'default_web/stage3_test.html', {})
def stage3_result(request):
	return render(request, 'default_web/stage3_result.html', {})






