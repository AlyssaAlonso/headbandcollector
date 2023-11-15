from django.shortcuts import render
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