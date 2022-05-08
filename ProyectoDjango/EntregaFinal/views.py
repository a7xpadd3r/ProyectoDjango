from pipes import Template
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import AbstractUser, User
import EntregaFinal

from EntregaIntermedia import models
from EntregaFinal import forms
from ProyectoDjango.settings import MEDIA_URL

class UsersWithList(LoginRequiredMixin, ListView): # Needs more work..
    genUsers = models.genUser.objects.all()
    fields = ['usernick', 'userid', 'userlastconnection', 'userposX', 'userposY', 'userposZ'] #as 
    success_url = reverse_lazy('players-cbv')
    template_name = 'players-cbv.html'
    
    def get_queryset(self):
        return  models.genUser.objects.all()

class UserLogin(TemplateView):  
    template_name = 'login.html'
    
    def get(self, request):
        form = AuthenticationForm
        context = { 'title' : 'Iniciar sesión', 'form' : form, 'logform' : 'logform' }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = AuthenticationForm(request, data = request.POST)
        if form:
            user = request.POST.get('username')
            pw = request.POST.get('password')
            user_auth = authenticate(username = user, password = pw)
            
            if user_auth:
                login(request, user_auth)
                #return redirect('/')
                context = { 'OK' : f'Bienvenido de vuelta, {user}!', 'title' : 'Sesión iniciada'}
                return render(request, self.template_name, context)
            else:
                context = { 'error' : 'Usuario/contraseña inválidos.', 'title' : 'Error al iniciar sesión', 'form' : form}
                return render(request, self.template_name, context)

class UserRegister(TemplateView):
    template_name = 'forms/register.html'
    context = { 'title' : 'Registrarse' }
    
    def get (self, request):
        form = UserCreationForm()
        context = { 'form' : form, 'title' : 'Registrarse', 'regform' : 'regform'}
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            context = { 'ok' : "Usuario creado con éxito!", 'title' : 'Usuario creado!'}
            print('Usuario creado.')
            return render(request, self.template_name,context)
        
        else:
            context = { 'error' : 'Ha ingresado datos incorrectos, intente nuevamente.', 'form' : form, }
            return render(request, self.template_name, context, )

@login_required
def TestRequest(request):
    return render(request, 'test.html')
    
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = forms.UserForm(request.POST, instance = request.user)
        profile_form = forms.ProfileForm(request.POST, instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            print('Guardado')
            return redirect('profile')
        else:
            print('Error')
            return redirect('error')
            
    else:
        user_form = forms.UserForm(instance = request.user)
        profile_form = forms.ProfileForm(instance = request.user.profile)
    return render(request, 'forms/editprofile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

class TestProfileView(TemplateView):
    template_name = 'test2.html'
    
    def get(self, request):
        user = User.objects.get(username = request.user)
        profile = request.user.profile.avatar
        context = { 'user' : user, 'profile' : profile, 'url' : MEDIA_URL }
        return render(request, self.template_name, context)
    
class ViewProfile(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    
    def get(self, request):
        context = { 'title' : 'Tu perfil', 'profile' : 'Estás viendo tu perfil.'}
        return render(request, self.template_name, context)
    
@login_required
def GenericError(request):
    template_name = 'error.html'
    context = { 'title' : 'Error' }
    return render(request, template_name, context)