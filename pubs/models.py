from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Venue(models.Model):
	name = models.CharField(max_length = 10)
	full_name = models.CharField(max_length = 150)

	JOURNAL = 'Journal'
	CONFERENCE = 'Conference'
	BOOK = 'Book Chapter'
	WORKSHOP = 'Workshop'
	POSTER = 'Poster'
	THESIS = 'Thesis'
	MISC = 'Misc.'


	TYPE_LIST = [(JOURNAL,JOURNAL),
				(CONFERENCE,CONFERENCE),
				(BOOK,BOOK),
				(WORKSHOP, WORKSHOP),
				(POSTER, POSTER),
				(THESIS, THESIS),
				(MISC,MISC),
				]

	venue_type = models.CharField(max_length = 15,
								choices = TYPE_LIST,
								default = MISC)


	def __str__(self):
		return self.name





class Publication(models.Model):
	title = models.CharField(max_length = 100)
	authors = models.CharField(max_length=100)
	venue = models.ForeignKey(Venue, on_delete=models.CASCADE, default = '')
	

	
	pub_date = models.DateField(blank=True)
	

	pdf_file = models.FileField(upload_to ='papers/', blank=True)


	def __str__(self):
		return '{}...'.format(self.title[0:20])


