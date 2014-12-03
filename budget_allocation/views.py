from django.shortcuts import render

# Create your views here.
def budget_allocation_test(request):
	return render(request, 'budget_allocation/stage2_test.html', {})
def stage2_result(request):
	return render(request, 'budget_allocation/stage2_result.html', {})
