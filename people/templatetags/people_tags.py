from django import template
from people.models import People


register = template.Library()


@register.filter
def degreeStr(value):
	if value == People.PHD :
		return 'Phd'
	elif value  == People.MS :
		return 'MS'
	elif value  == People.BS :
		return 'BS'
	else:
		return ''


@register.filter
def postgradStr(value):
	if value:
		return ' ,now at {}'.format(value)
	else:
		return ''