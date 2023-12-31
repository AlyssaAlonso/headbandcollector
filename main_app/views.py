from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Headband, Accessory
from .forms import StatusForm

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
  id_list = headband.accessories.all().values_list('id')
  accessories_headband_doesnt_have = Accessory.objects.exclude(id__in=id_list)
  status_form = StatusForm()
  return render(request, 'headbands/detail.html', {
    'headband': headband, 'status_form': status_form,
    'accessories': accessories_headband_doesnt_have
  })

def add_status(request, headband_id):
  # create a ModelForm instance using the data in request.POST
  form = StatusForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the headband_id assigned
    new_status = form.save(commit=False)
    new_status.headband_id = headband_id
    new_status.save()
  return redirect('detail', headband_id=headband_id)

class HeadbandCreate(CreateView):
  model = Headband
  fields = '__all__'

class HeadbandUpdate(UpdateView):
  model = Headband
  fields = ['name', 'material', 'description', 'price']

class HeadbandDelete(DeleteView):
  model = Headband
  success_url = '/headbands'

class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'color']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories'

def assoc_accessory(request, headband_id, accessory_id):
  Headband.objects.get(id=headband_id).accessories.add(accessory_id)
  return redirect('detail', headband_id=headband_id)

def unassoc_accessory(request, headband_id, accessory_id):
  Headband.objects.get(id=headband_id).accessories.remove(accessory_id)
  return redirect('detail', headband_id=headband_id)