from easy_thumbnails.fields import ThumbnailerImageField
from django.db import models

class Slide(models.Model):
	title = models.CharField(max_length=50)
	quote_text = models.TextField(max_length=1000)
	background_image = ThumbnailerImageField(upload_to='uploaded/images')
	#order of the slides

class Logos(models.Model):
	loc_type = (
			("Platinum","Platinum"),
			("Gold","Gold"),
			("Silver","Silver"),
			("Bronze","Bronze"),
		)
	status = models.CharField(max_length=55,choices=loc_type,default="guest")
	title = models.CharField(max_length=50)
	logo = ThumbnailerImageField(upload_to='uploaded/images')
	link =  models.CharField(max_length=300)

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
	# link url
	# order of location


class Content(models.Model):
	slides = models.ManyToManyField(Slide)

	inspiration_top = models.TextField(max_length=300)
	inspiration = models.TextField(max_length=3000)
	#background image 1 for insperation
	#background image 2 for insperation
	guests_text = models.TextField(max_length=2000)
	pilots_text = models.TextField(max_length=2000)
	drivers_text = models.TextField(max_length=2000)

	online_payment_link = models.CharField(max_length=300)
	online_payment_text = models.CharField(max_length=1000) #to text field
	#background image for registration

	cheque_payment_text= models.CharField(max_length=1000) #to text field
	waiver_form = models.FileField(upload_to='backgroundimage/%Y/%m/%d')
	pledge_form = models.FileField(upload_to='backgroundimage/%Y/%m/%d')
	registration_form = models.FileField(upload_to='backgroundimage/%Y/%m/%d')

	map_locations =  models.ManyToManyField(location)
	sponsors =  models.ManyToManyField(Logos)

	conact_phone = models.CharField(max_length=300)
	conact_email = models.CharField(max_length=300)


