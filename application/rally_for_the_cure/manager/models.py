from easy_thumbnails.fields import ThumbnailerImageField
from django.db import models

class Slide(models.Model):
	title = models.CharField(max_length=50)
	quote_text = models.TextField(max_length=1000,blank=True)
	background_image = ThumbnailerImageField(upload_to='uploaded/img')
	order = models.IntegerField(default=99)		#
	def __unicode__(self):
		return self.title

class Logos(models.Model):
	loc_type = (
			("Platinum","Platinum"),
			("Gold","Gold"),
			("Silver","Silver"),
			("Bronze","Bronze"),
		)
	status = models.CharField(max_length=55,choices=loc_type,default="guest")
	title = models.CharField(max_length=50)
	logo = ThumbnailerImageField(upload_to='uploaded/img')
	link =  models.CharField(max_length=300)
	def __unicode__(self):
		return self.title

class location(models.Model):
	title = models.CharField(max_length=200)
	loc_type = (
			("guests","guests"),
			("pilots","pilots"),
			("drivers","drivers"),
		)
	location_type = models.CharField(max_length=55,choices=loc_type,default="guest")
	lat = models.CharField(max_length=30)
	log = models.CharField(max_length=30)
	description = models.TextField(max_length=500)
	order = models.IntegerField(default=99)			#
	link_url = models.CharField(max_length=300)		#
	def __unicode__(self):
		return self.title


class Content(models.Model):
	slides = models.ManyToManyField(Slide)

	inspiration_top = models.TextField(max_length=300)
	inspiration = models.TextField(max_length=3000)
	background_image_1 = ThumbnailerImageField(upload_to='uploaded/img')	#
	background_image_2 = ThumbnailerImageField(upload_to='uploaded/img')	#
	background_image_portrait = ThumbnailerImageField(upload_to='uploaded/img')	#


	guests_text = models.TextField(max_length=2000)
	pilots_text = models.TextField(max_length=2000)
	drivers_text = models.TextField(max_length=2000)

	online_payment_link = models.CharField(max_length=300)
	online_payment_text = models.TextField(max_length=1000)
	background_image_registration = ThumbnailerImageField(upload_to='uploaded/img')

	cheque_payment_text= models.TextField(max_length=1000)
	waiver_form = models.FileField(upload_to='files')
	pledge_form = models.FileField(upload_to='files')
	registration_form = models.FileField(upload_to='files')

	map_locations =  models.ManyToManyField(location)
	sponsors =  models.ManyToManyField(Logos)

	conact_phone = models.CharField(max_length=300)
	conact_email = models.CharField(max_length=300)


