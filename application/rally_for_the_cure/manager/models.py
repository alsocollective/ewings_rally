from django.db import models

class Slide(models.Model):
	title = models.CharField(max_length=50)
	quote_text = models.TextField(max_length=1000)
	background_image = ThumbnailerImageField(upload_to='uploaded/images')


class logos(models.Model):
	title = models.CharField(max_length=50)
	logo = ThumbnailerImageField(upload_to='uploaded/images')
	link =  models.CharField(max_length=300)

class location(models.Model):
	loc_type = (
			("guest","guest"),
			("pilot","pilot"),
			("driver","driver"),
		)
	index_version = models.CharField(max_length=55,choices=loc_type,default="guest")
	lat = models.CharField(max_length=30)
	log = models.CharField(max_length=30)


class Content(models.Model):
	inspiration_top = models.TextField(max_length=300)

	inspiration = models.TextField(max_length=3000)
	guests_text = models.TextField(max_length=2000)
	pilots_text = models.TextField(max_length=2000)
	drivers_text = models.TextField(max_length=2000)

	online_payment_link = models.CharField(max_length=300)
	online_payment_text = models.CharField(max_length=1000)

	cheque_payment_text= models.CharField(max_length=1000)
	waiver_form = forms.FileField(label="select form pdf")
	pledge_form = forms.FileField(label="select form pdf")
	registration_form = forms.FileField(upload_to='backgroundimage/%Y/%m/%d',label="select form pdf")
