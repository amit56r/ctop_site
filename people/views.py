from django.shortcuts import render
from .models import People
# Create your views here.



def people_list(request):
	faculty = People.objects.filter(position = People.PROFESSOR)
	students = People.objects.filter(position = People.STUDENT)
	current_students = students.filter(has_graduated = False)
	alumni = students.filter(has_graduated = True)

	context = {'faculty': faculty, 'current_students' : current_students, 'alumni': alumni}
	return render(request, 'people/people_list.html', context)
