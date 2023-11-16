from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('headbands/', views.headbands_index, name='index'),
  path('headbands/<int:headband_id>/', views.headbands_detail, name='detail'),
  path('headbands/create/', views.HeadbandCreate.as_view(), name='headbands_create'),
  path('headbands/<int:pk>/update/', views.HeadbandUpdate.as_view(), name='headbands_update'),
  path('headbands/<int:pk>/delete/', views.HeadbandDelete.as_view(), name='headbands_delete'),
  path('headbands/<int:headband_id>/add_status/', views.add_status, name='add_status'),
]