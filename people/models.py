from __future__ import unicode_literals

from django.db import models

# Create your models here.



class People(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	PROFESSOR = 'PROF'
	STUDENT = 'STUDENT'
	STAFF = 'STAFF'
	POSITION_LIST = [(PROFESSOR, 'Professor'), (STUDENT, 'Student'), (STAFF,'Staff')]


	PHD = 'PHD'
	MS = 'MS'
	BS = 'BS'
	DEGREE_LIST = [(PHD, 'PhD'), (MS, 'MS'), (BS, 'BS')]

	position = models.CharField(max_length = 10,
								choices = POSITION_LIST,
								default = STUDENT,
								)

	degree = models.CharField(max_length = 10,
								choices = DEGREE_LIST,
								default = BS,
								)


	website =  models.URLField(blank=True)
	has_graduated = models.BooleanField(default = False)
	postgrad_job = models.CharField(max_length=50,blank=True)


	def __str__(self):
		return '{} {}'.format(self.first_name, self.last_name)

