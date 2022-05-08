from django.views.generic import TemplateView
from django.urls import path
from EntregaIntermedia import views

urlpatterns = [
    path('', views.home, name='index'),
    path('searchuser/', views.SearchUser.as_view(), name = 'searchuser'),
    path('searchitem/', views.SearchItem.as_view(), name='searchitem'),
    path('searchvehicle/', views.SearchVehicle.as_view(), name='searchvehicle'),
    path('searchadmin', views.SearchAdmin.as_view(), name = 'searchadmin'),
    
    path('adduser/', views.AddUser.as_view(), name='adduser'),
    path('additem/', views.AddItem.as_view(), name='additem'),
    path('addvehicle/', views.AddVehicle.as_view(), name='addvehicle'),
    path('addadmin/', views.AddAdmin.as_view(), name = 'addadmin'),
    
    path('players/', views.Users, name = 'players'),
    path('items/', views.Items, name = 'items'),
    path('vehicles/', views.Vehicles, name = 'vehicles'),
    path('admins/', views.Administrators, name = 'admins')
]
