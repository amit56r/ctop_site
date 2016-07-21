from django.shortcuts import render,get_object_or_404
from django.utils import timezone


from django.contrib.auth.decorators import login_required



def index(reques):
	return render(reques,'base.html',{})


	