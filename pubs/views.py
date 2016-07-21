from django.shortcuts import render
from .models import Publication, Venue
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.





def resolve_queries(qDict):
	return Publication.objects.all()



def pub_main(request,pg_id = 1):
	if request.GET:
		pubs  = resolve_queries(request.GET)
	else:
		pubs = Publication.objects.all()

	page_collection = Paginator(pubs, 2)

	try:
		page = page_collection.page(pg_id)
	except PageNotAnInteger:
		page = page_collection.page(1)
	except EmptyPage:
		page = page_collection.page(page_collection.num_pages) 



	return pub_list(request, page, page_collection.page_range)




def pub_list(request,page,page_range):



	context = {
				'page': page,
				'qDict': request.GET,
				'page_range': page_range,
				'type_list': Venue.TYPE_LIST

	}
	return render(request, 'pub/pub_list.html', context)
