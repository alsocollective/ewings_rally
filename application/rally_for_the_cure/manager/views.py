from django.shortcuts import render, render_to_response, get_object_or_404
from easy_thumbnails.files import get_thumbnailer
from django.http import HttpResponse


def home(request):
	return render_to_response('index.html',{"something":"nothing"})

