from django.db import models
#it's for create fileds and so one in the page ! like name,age,etc
# the most important part in program here every thing for logic program
# Create your models here.
'''
python manage.py makemigration
python manage.py migrate

'''

class KirrURL(models.Model):
	#here is the filed ! named url
	url = models.CharField(max_length=220,)

	def __str__(self):
		return str(self.url)


	def __unicode__(self):
		return str(self.url)