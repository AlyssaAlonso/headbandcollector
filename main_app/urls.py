from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('headbands/', views.headbands_index, name='index'),
  path('headbands/<int:headband_id>/', views.headbands_detail, name='detail'),
]