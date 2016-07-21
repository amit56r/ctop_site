from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from post.models import Post

# Create your views here.


def frontpage(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'post/frontpage.html',{'posts': posts})