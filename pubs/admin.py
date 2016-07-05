from django.contrib import admin

# Register your models here.

from .models import Publication, Venue



class PubInline(admin.TabularInline):
	model = Publication
	extra  = 1

class VenueAdmin(admin.ModelAdmin):
	inlines = [PubInline]
	search_fields = ['name']

class PubAdmin(admin.ModelAdmin):
	search_fields = ['title', 'authors']

admin.site.register(Publication,PubAdmin)
admin.site.register(Venue,VenueAdmin)
