from django.shortcuts import render
from django.views.generic import (View,TemplateView,
	                              ListView,DetailView,
	                              CreateView,UpdateView,DeleteView)
from django.http import HttpResponse
from django.urls import reverse_lazy		
from .import models

class indexView(TemplateView):
	template_name='templates/index.html'

class SchoolListView(ListView):
	context_object_name='schools'
	model=models.School
	template_name='basic_app/school_list.html'

class SchoolDetailView(DetailView):
	context_object_name='school_detail'
	model=models.School
	template_name='basic_app/school_detail.html'

class SchoolCreateView(CreateView):
	fields=('name','principal','location')
	model=models.School
	template_name='basic_app/school_form.html'

class SchoolUpdateView(UpdateView):
	fields=('name','principal')
	model=models.School
	template_name='basic_app/school_form.html'

class SchoolDeleteView(DeleteView):
	model=models.School
	success_url=reverse_lazy("basic_app:list")
	template_name='basic_app/school_confirm_delete.html'