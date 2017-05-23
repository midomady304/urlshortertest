from django.db import models
#it's for create fileds and so one in the page ! like name,age,etc
# the most important part in program here every thing for logic program
# Create your models here.
'''
python manage.py makemigrations here name of apps --empty
python manage.py makemigration
python manage.py migrate
python manage.py createsuperuser

'''

class KirrURL(models.Model):
	#here is the filed ! named url
	url       = models.CharField(max_length=220,)
	shortcode = models.CharField(max_length=15, unique=True)
	updated   = models.DateTimeField(auto_now = True) # everytime the model is saved
	#timestamp = models.DateTimeField(auto_now_add = True) #when model was created
	#shortcode = models.CharField(max_length=15, null=true) this mean is the empty in database is ok
	#shortcode = models.CharField(max_length=15, default='defaultshortcode') it mean every value will be by default

	def __str__(self):
		return str(self.url)


	def __unicode__(self):
		return str(self.url)