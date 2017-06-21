# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
	courses = Course.objects.all()
	print courses
	return render(request, 'catalog_app/index.html')
