from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from EntregaIntermedia import forms, models # Importing models itself instead of every model

# Create your views here.
def home(request):
    context = { 'title' : 'Inicio' }
    return render(request, "home.html", context)

# User interaction stuff. Order: VIEW ALL, SEARCH, ADD
# Users section

def Users(request):
    template_name = 'players.html'
    players = models.genUser.objects.all()
    context = {
        'title' : 'Ver jugadores',
        'playersdata' : players,
        'amount' : players.count(),
    }
        #return render(request, self.template_name, context)
    return render(request, template_name, context)

class SearchUser(TemplateView):
    template_name = 'forms/searchuser.html'
  
    def get(self,request):
        context = {'title' : 'Buscar jugador', 'message' : 'Aquí aparecerán los resultados de su búsqueda.'}
        return render(request, self.template_name, context)
  
    def post(self, request):
        print(f"Buscando: {request.POST.get('playernick')}")
        data = models.genUser.objects.filter(usernick = request.POST.get('playernick'))
        context = { 'elements' : data }
        if data.count() == 0:
            context = { 'message' : 'No se han encontrado coincidencias.' }
            
        return render(request, self.template_name, context)
    
class AddUser(TemplateView):
    template_name = 'forms/addplayer.html'
    
    def get(self,request):
        context = {'title' : 'Agregar jugador','form' : forms.AddUserForm}
        return render(request, self.template_name, context)
    
    def post(self, request):
        context = {'form' : forms.AddUserForm}
        response = forms.AddUserForm(request.POST)
        
        if response.is_valid:
            r_nick = request.POST['usernick']
            r_id = request.POST['userid']
            r_lastconnection = request.POST['userlastconnection']
            r_posX = request.POST['userposX']
            r_posY = request.POST['userposY']
            r_posZ = request.POST['userposZ']
            obj_userdata = models.genUser(usernick = r_nick, userid = r_id, userlastconnection = r_lastconnection, userposX = r_posX, userposY = r_posY, userposZ = r_posZ)
            obj_userdata.save()
            context = {'form' : forms.AddUserForm, 'message' : 'Nuevo jugador agregado con éxito!'}
            print(f'Saving user: {r_nick}-{r_id}-{r_lastconnection}-{r_posX},{r_posY},{r_posZ} on {r_lastconnection}')
        return render(request, self.template_name, context)

# Items section

def Items(request):
    template_name = 'items.html'
    items = models.genItem.objects.all()
    context = {
        'title' : 'Ver ítems',
        'itemsdata' : items,
        'amount' : items.count(),
    }
        #return render(request, self.template_name, context)
    return render(request, template_name, context)

class SearchItem(TemplateView):
    template_name = 'forms/searchitem.html'
  
    def get(self,request):
        context = {'title' : 'Buscar ítem', 'message' : 'Aquí aparecerán los resultados de su búsqueda.'}
        return render(request, self.template_name, context)
  
    def post(self, request):
        print(f"Buscando: {request.POST.get('itemname')}")
        data = models.genItem.objects.filter(itemname = request.POST.get('itemname'))
        context = { 'elements' : data }
        if data.count() == 0:
            context = { 'message' : 'No se han encontrado coincidencias.' }
        return render(request, self.template_name, context)

class AddItem(TemplateView):
    template_name = 'forms/additem.html'
    
    def get(self,request):
        context = { 'title' : 'Agregar ítem', 'form' : forms.AddItemForm}
        return render(request, self.template_name, context)
    
    def post(self, request):
        context = {'form' : forms.AddItemForm}
        response = forms.AddItemForm(request.POST)
        
        if response.is_valid:
            r_name = request.POST['itemname']
            r_quantity = request.POST['itemquantity']
            r_posX = request.POST['itemposX']
            r_posY = request.POST['itemposY']
            r_posZ = request.POST['itemposZ']
            obj_itemdata = models.genItem(itemname = r_name, itemquantity = r_quantity, itemposX = r_posX, itemposY = r_posY, itemposZ = r_posZ)
            obj_itemdata.save()
            context = {'form' : forms.AddItemForm, 'message' : 'Nuevo ítem agregado con éxito!'}
            print(f'Saving item: {r_name}-{r_quantity}-{r_posX},{r_posY},{r_posZ}')
        return render(request, self.template_name, context)
    
# Vehicle section

def Vehicles(request):
    template_name = 'vehicles.html'
    vehicles = models.genVehicle.objects.all()
    context = {
        'title' : 'Ver vehículos',
        'vehiclesdata' : vehicles,
        'amount' : vehicles.count(),
    }
        #return render(request, self.template_name, context)
    return render(request, template_name, context)

class AddVehicle(TemplateView):
    template_name = 'forms/addvehicle.html'
    
    def get(self,request):
        context = { 'title' : 'Agregar vehículo', 'form' : forms.AddVehicleForm}
        return render(request, self.template_name, context)
    
    def post(self, request):
        context = {'form' : forms.AddVehicleForm}
        response = forms.AddVehicleForm(request.POST)
        
        if response.is_valid:
            r_name = request.POST['vehiclename']
            r_posX = request.POST['vehicleposX']
            r_posY = request.POST['vehicleposY']
            obj_vehicledata = models.genVehicle(vehiclemodel = r_name, vehicleposX = r_posX, vehicleposY = r_posY)
            obj_vehicledata.save()
        
        print(f'Saving vehicle: {r_name}-{r_posX},{r_posY}')
        return render(request, self.template_name, context)
    
class SearchVehicle(TemplateView):
    template_name = 'forms/searchvehicle.html'
  
    def get(self,request):
        context = {'title' : 'Buscar vehículo', 'message' : 'Aquí aparecerán los resultados de su búsqueda.'}
        return render(request, self.template_name, context)
  
    def post(self, request):
        print(f"Buscando: {request.POST.get('vehiclemodel')}")
        data = models.genVehicle.objects.filter(vehiclemodel = request.POST.get('vehiclemodel'))
        context = { 'elements' : data}
        if data.count() == 0:
            context = { 'message' : 'No se han encontrado coincidencias.' }
        
        return render(request, self.template_name, context)
    
# Admins section

def Administrators(request):
    template_name = 'admins.html'
    admins = models.genAdmin.objects.all()
    context = {
        'title' : 'Ver administradores',
        'adminsdata' : admins,
        'amount' : admins.count(),
    }
        #return render(request, self.template_name, context)
    return render(request, template_name, context)

class AddAdmin(TemplateView):
    template_name = 'forms/addadmin.html'
    
    def get(self,request):
        context = { 'title' : 'Agregar administrador', 'form' : forms.AddAdminForm}
        return render(request, self.template_name, context)
    
    def post(self, request):
        context = {'form' : forms.AddAdminForm}
        response = forms.AddAdminForm(request.POST)
        
        if response.is_valid:
            r_id = request.POST['adminid']
            r_accesslevel = request.POST['accesslevel']
            obj_admindata = models.genAdmin(adminid = r_id, adminaccesslevel = r_accesslevel)
            obj_admindata.save()
            print(f'Saving administrator: {r_id}-{r_accesslevel}')
            context = {'form' : forms.AddAdminForm, 'message' : 'Nuevo administrador agregado con éxito!'}
            
        return render(request, self.template_name, context)
    
class SearchAdmin(TemplateView):
    template_name = 'forms/searchadmin.html'
  
    def get(self,request):
        context = {'title' : 'Buscar administrador', 'message' : 'Aquí aparecerán los resultados de su búsqueda.'}
        return render(request, self.template_name, context)
  
    def post(self, request):
        print(f"Buscando: {request.POST.get('accesslevel')}")
        data = models.genAdmin.objects.filter(adminaccesslevel = request.POST.get('accesslevel'))
        context = { 'elements' : data}
        if data.count() == 0:
            context = { 'message' : 'No se han encontrado coincidencias.' }
        return render(request, self.template_name, context)