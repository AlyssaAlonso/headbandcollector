from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Headband

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def headbands_index(request):
  headbands = Headband.objects.all()
  return render(request, 'headbands/index.html', {
    'headbands': headbands
  })

def headbands_detail(request, headband_id):
  headband = Headband.objects.get(id=headband_id)
  return render(request, 'headbands/detail.html', { 'headband': headband })

class HeadbandCreate(CreateView):
  model = Headband
  fields = '__all__'

class HeadbandUpdate(UpdateView):
  model = Headband
  fields = ['name', 'material', 'description', 'price']

class HeadbandDelete(DeleteView):
  model = Headband
  success_url = '/headbands'