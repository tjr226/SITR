from django.db import models
from django.contrib.auth.models import User

# you need to do TWO command line commands to successfully migrate everything
# python manage.py makemigrations
# python manage.py migrate

class Contact(models.Model):
	contact_name = models.CharField(max_length=100, unique=False)
	contact_info = models.CharField(max_length=1000)
	last_contacted = models.DateField(auto_now_add=True)
	# recurrence schedule defaults to quarters/90 days
	recurrence_schedule_in_days = models.PositiveIntegerField(default=90)

	created_at = models.DateField(auto_now_add=True)
	created_by = models.ForeignKey(User, null=True, related_name='contacts', on_delete=models.CASCADE,)

	def __str__(self):
		return self.name