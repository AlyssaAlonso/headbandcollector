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
  path('headbands/<int:headband_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
  path('headbands/<int:headband_id>/unassoc_accessory/<int:accessory_id>/', views.unassoc_accessory, name='unassoc_accessory'),
  path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
  path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
  path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
  path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
  path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessories_delete'),
]