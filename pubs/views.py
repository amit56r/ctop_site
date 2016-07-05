from django.shortcuts import render

# Create your views here.

def pub_list(request):
	return render(request, 'pub/pub_list.html')
