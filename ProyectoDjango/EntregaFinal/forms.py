from django import forms
from django.contrib.auth.models import User
from EntregaFinal.models import Profile        
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('info', 'avatar')