from django.views.generic import TemplateView
from django.urls import path
from EntregaIntermedia import views

from django.conf import settings
from django.conf.urls.static import static
from ProyectoDjango.settings import STATIC_URL, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('searchuser/', views.SearchUser.as_view(), name = 'searchuser'),
    path('searchitem/', views.SearchItem.as_view(), name='searchitem'),
    path('searchvehicle/', views.SearchVehicle.as_view(), name='searchvehicle'),
    path('searchadmin', views.SearchAdmin.as_view(), name = 'searchadmin'),
    
    path('adduser/', views.AddUser.as_view(), name='adduser'),
    path('additem/', views.AddItem.as_view(), name='additem'),
    path('addvehicle/', views.AddVehicle.as_view(), name='addvehicle'),
    path('addadmin/', views.AddAdmin.as_view(), name = 'addadmin'),
    
    path('players/', views.Users.as_view(), name = 'players'),
    path('items/', views.Items.as_view(), name = 'items'),
    path('vehicles/', views.Vehicles.as_view(), name = 'vehicles'),
    path('admins/', views.Administrators.as_view(), name = 'admins'),
    
    # Agregados
    path('edituser/<int:editthisid>/', views.EditUser.as_view(), name = 'edituser'),
    path('deleteuser/<int:deletethisid>/', views.DeleteUser.as_view(), name = 'deleteuser'),
    
    path('edititem/<str:editthisitem>/', views.EditItem.as_view(), name = 'edititem'),
    path('deleteitem/<str:deletethisitem>', views.DeleteItem.as_view(), name = 'deleteitem'),
    
    path('editvehicle/<str:editthisvehicle>/', views.EditVehicle.as_view(), name = 'editvehicle'),
    path('deletevehicle/<str:deletethisvehicle>/', views.DeleteVehicle.as_view(), name = 'deletevehicle'),
    
    path('editadmin/<int:editthisid>/', views.EditAdmin.as_view(), name = 'editadmin'),
    path('deleteadmin/<int:deletethisid>/', views.DeleteAdmin.as_view(), name = 'deleteadmin'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
