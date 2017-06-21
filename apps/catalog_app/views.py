# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import Course, Description

# Create your views here.
def index(request):
	courses = Course.objects.all()
	context = {
		'courses': courses
	}
	return render(request, 'catalog_app/index.html', context)

def add_course(request):
	course = Course.objects.create(name=request.POST['name'])
	Description.objects.create(description=request.POST['description'], course=course )
	return redirect('/')
