from cgi import test
from django.urls import path
from django.contrib.auth.views import LogoutView
from EntregaFinal import views

urlpatterns = [
    # cbv needs more work...
    path('players-cbv/', views.UsersWithList.as_view(), name='players-cbv'),
    
    path('accounts/login/', views.UserLogin.as_view(), name='login'),
    path('accounts/signup/', views.UserRegister.as_view(), name='register'),
    path('accounts/profile/', views.ViewProfile.as_view(), name = 'profile'),
    path('accounts/editprofile/', views.update_profile, name = 'editprofile'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    
    path('error/', views.GenericError, name = 'error'),
    path('test1/', views.TestProfileView.as_view(), name = 'test1'),
    path('test2/', views.TestRequest, name = 'test2'),
]