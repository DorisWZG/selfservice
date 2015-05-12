from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


#def index(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
def index(request):
	return render(request, 'asia_media_guide/index.html', {})


