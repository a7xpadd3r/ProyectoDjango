from pipes import Template
from re import template
from django.shortcuts import render
from django.views.generic import TemplateView
from EntregaIntermedia import forms, models
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

# Create your views here.
def home(request):
    context = { 'title' : 'Inicio' }
    return render(request, "home.html", context)

# Home page
class Index(TemplateView):
    template_name = 'home.html'
    
    def get(self, request):
        context = { 'title' : 'Inicio'}
        return render(request, self.template_name, context)

# User interaction stuff. Order: VIEW ALL, SEARCH, ADD
# Added: EDIT, REMOVE
# Users section
class Users(TemplateView):
    template_name = 'players.html'
    
    def get(self, request):
        players = models.genUser.objects.all()
        context = {
            'title' : 'Ver jugadores',
            'playersdata' : players,
            'amount' : players.count(),
            }
        return render(request, self.template_name, context)
    
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
    
class AddUser(LoginRequiredMixin, TemplateView):
    template_name = 'forms/addplayer.html'
    
    def get(self,request):
        context = {'title' : 'Agregar jugador','form' : forms.AddUserForm}
        return render(request, self.template_name, context)
    
    def post(self, request):
        context = {'form' : forms.AddUserForm}
        response = forms.AddUserForm(request.POST)
        img = request.FILES 
        checkid = request.POST['userid']        
        if request.method == 'POST' and models.genUser.objects.filter(userid = checkid).count() == 0 and response.is_valid:
            r_nick = request.POST['usernick']
            r_id = request.POST['userid']
            r_lastconnection = request.POST['userlastconnection']
            r_posX = request.POST['userposX']
            r_posY = request.POST['userposY']
            r_posZ = request.POST['userposZ']
            obj_userdata = models.genUser(usernick = r_nick, 
                                          userid = r_id, 
                                          userlastconnection = r_lastconnection, 
                                          userposX = r_posX, 
                                          userposY = r_posY, 
                                          userposZ = r_posZ,
                                          creationdate = datetime.datetime.now(),
                                          modificationdate = datetime.datetime.now(),
                                          createdby = request.user,
                                          lastmodifiedby = request.user,
                                          playericon = img.get('icon'))
            obj_userdata.save()
            context = {'form' : forms.AddUserForm, 'message' : 'Nuevo jugador agregado con éxito!', 'newentry' : obj_userdata}
            print(f'Guardado jugador nuevo: {r_nick}-{r_id}-{r_lastconnection}-{r_posX},{r_posY},{r_posZ} on {r_lastconnection}')
            
        else:   # Repost input
            context = {'form' : forms.AddUserForm(initial = {
                'usernick' : request.POST['usernick'],
                'userid' : request.POST['userid'],
                'userlastconnection' : request.POST['userlastconnection'],
                'userposX' : request.POST['userposX'],
                'userposY' : request.POST['userposY'],
                'userposZ' : request.POST['userposZ'],
                }
            ), 'errormessage' : f"El ID ingresado ya está en uso o ha ocurrido un error."}
            print(f"Ha ocurrido un error.")
        return render(request, self.template_name, context)
    
class EditUser(LoginRequiredMixin, TemplateView):
    template_name = 'forms/editplayer.html'
    
    def get(self, request, editthisid):
        print(f"Editando: {models.genUser.objects.filter(userid = editthisid)}")
        user = models.genUser.objects.get(userid = editthisid)
        context = {
            'form' : forms.EditUserForm(initial= {
                'usernick' : user.usernick,
                'userid' : user.userid,
                'userlastconnection' : user.userlastconnection,
                'userposX' : user.userposX,
                'userposY' : user.userposY,
                'userposZ' : user.userposZ,
                })
            }
        return render(request, self.template_name, context)
    
    def post(self, request, editthisid):
        changes = request.POST
        models.genUser.objects.update_or_create(userid = editthisid,
            defaults = {
            'usernick' : changes.get('usernick'),
            'userlastconnection' : changes.get('userlastconnection'),
            'userposX' : changes.get('userposX'),
            'userposY' : changes.get('userposY'),
            'userposZ' : changes.get('userposZ'),
            'modificationdate' : datetime.datetime.now(),
            'lastmodifiedby' : str(request.user),
            }
        )
        context = { 'message' : 'Entrada modificada con éxito!' }
        return render(request, self.template_name, context)
    
class DeleteUser(LoginRequiredMixin, TemplateView):
    template_name = 'forms/deleteplayer.html'
    
    def get(self, request, deletethisid):
        print(f"Se quiere eliminar: '{deletethisid}'.")
        objetive = models.genUser.objects.get(userid = deletethisid)
        context = { 'results' : objetive, 'form' : forms.DeleteUserForm }
        return render(request, self.template_name, context)
    
    def post(self, request, deletethisid):
        print(f"Eliminando '{deletethisid}'...")
        objetive = models.genUser.objects.get(userid = deletethisid)
        context = { 'message' : 'La entrada ha sido eliminada.' }
        objetive.delete()
        return render(request, self.template_name, context) 

# Items section

class Items(TemplateView):
    template_name = 'items.html'
    
    def get(self, request):
        items = models.genItem.objects.all()
        context = {
            'title' : 'Ver ítems',
            'itemsdata' : items,
            'amount' : items.count(),
        }
        return render(request, self.template_name, context)

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

class AddItem(LoginRequiredMixin, TemplateView):
    template_name = 'forms/additem.html'
    
    def get(self,request):
        context = { 'title' : 'Agregar ítem', 'form' : forms.AddItemForm}
        return render(request, self.template_name, context)
    
    def post(self, request):
        context = {'form' : forms.AddItemForm}
        response = forms.AddItemForm(request.POST)
        img = request.FILES
        checkname = request.POST['itemname']
        if request.method == 'POST' and response.is_valid and models.genItem.objects.filter(itemname = checkname).count() == 0:
            r_name = request.POST['itemname']
            r_quantity = request.POST['itemquantity']
            r_posX = request.POST['itemposX']
            r_posY = request.POST['itemposY']
            r_posZ = request.POST['itemposZ']
            r_icon = img.get('icon')
            obj_itemdata = models.genItem(itemname = r_name, 
                                          itemquantity = r_quantity, 
                                          itemposX = r_posX, 
                                          itemposY = r_posY, 
                                          itemposZ = r_posZ, 
                                          creationdate = datetime.datetime.now(), 
                                          modificationdate = datetime.datetime.now(),
                                          createdby = request.user,
                                          lastmodifiedby = request.user,
                                          itemicon = r_icon)
            obj_itemdata.save()
            context = {'form' : forms.AddItemForm, 'message' : 'Nuevo ítem agregado con éxito!', 'newentry' : obj_itemdata}
            print(f'Guardando item: {r_name}-{r_quantity}-{r_posX},{r_posY},{r_posZ}')
        
        else:   # Repost input
            context = { 'form' : forms.AddItemForm(initial = {
                'itemname' : request.POST['itemname'],
                'itemquantity' : request.POST['itemquantity'],
                'itemposX' : request.POST['itemposX'],
                'itemposY' : request.POST['itemposY'],
                'itemposZ' : request.POST['itemposZ'],
                'icon' : request.POST['icon'],
                }), 
                'errormessage' : 'Ya existe un ítem con el nombre ingresado.'
            }
            print(f"Error: el item '{request.POST['itemname']}' ya existe.")
        return render(request, self.template_name, context)

class EditItem(LoginRequiredMixin, TemplateView):
    template_name = 'forms/edititem.html'
    
    def get(self, request, editthisitem):
        print(f"Editando: {models.genItem.objects.filter(itemname = editthisitem)}")
        item = models.genItem.objects.get(itemname = editthisitem)
        context = {
            'form' : forms.EditItemForm(initial = {
                'itemname' : item.itemname,
                'itemquantity' : item.itemquantity,
                'itemposX' : item.itemposX,
                'itemposY' : item.itemposY,
                'itemposZ' : item.itemposZ,
            })
        }
        return render(request, self.template_name, context)
    
    def post(self, request, editthisitem):
        changes = request.POST
        models.genItem.objects.update_or_create(itemname = editthisitem,
        defaults = {
            'itemquantity' : changes.get('itemquantity'),
            'itemposX' : changes.get('itemposX'),
            'itemposY' : changes.get('itemposY'),
            'itemposZ' : changes.get('itemposZ'),
            'modificationdate' : datetime.datetime.now(),
            'lastmodifiedby' : str(request.user),
        })
        context = { 'message' : 'Entrada modificada con éxito!' }
        return render(request, self.template_name, context)
    
class DeleteItem(LoginRequiredMixin, TemplateView):
    template_name = 'forms/deleteitem.html'
    
    def get(self, request, deletethisitem):
        print(f"Se quiere elimiar: '{deletethisitem}'.")
        objetive = models.genItem.objects.get(itemname = deletethisitem)
        print(objetive)
        context = { 'results' : objetive, 'form' : forms.DeleteItemForm }
        print(objetive)
        return render(request, self.template_name, context)
    
    def post(self, request, deletethisitem):
        print(f"Eliminando '{deletethisitem}'...")
        objetive = models.genItem.objects.get(itemname = deletethisitem)
        context = { 'message' : 'La entrada ha sido eliminada.' }
        objetive.delete()
        return render(request, self.template_name, context)  
    
# Vehicle section

class Vehicles(TemplateView):
    template_name = 'vehicles.html'
    
    def get(self, request):
        vehicles = models.genVehicle.objects.all()
        context = {
            'title' : 'Ver vehículos',
            'vehiclesdata' : vehicles,
            'amount' : vehicles.count(),
        }
        return render(request, self.template_name, context)

class AddVehicle(LoginRequiredMixin, TemplateView):
    template_name = 'forms/addvehicle.html'
    
    def get(self,request):
        context = { 'title' : 'Agregar vehículo', 'form' : forms.AddVehicleForm}
        return render(request, self.template_name, context)
    
    def post(self, request):
        context = {'form' : forms.AddVehicleForm}
        response = forms.AddVehicleForm(request.POST)
        img = request.FILES
        checkmodel = request.POST['vehiclemodel']
        print()
        
        if response.is_valid and models.genVehicle.objects.filter(vehiclemodel = checkmodel).count() == 0:
            r_name = request.POST['vehiclemodel']
            r_posX = request.POST['vehicleposX']
            r_posY = request.POST['vehicleposY']
            obj_vehicledata = models.genVehicle(vehiclemodel = r_name, 
                                                vehicleposX = r_posX, 
                                                vehicleposY = r_posY, 
                                                creationdate = datetime.datetime.now(), 
                                                createdby = request.user,
                                                lastmodifiedby = request.user,
                                                modificationdate = datetime.datetime.now(), 
                                                vehicleicon = img.get('icon'))
            obj_vehicledata.save()
            context = { 'form' : forms.AddVehicleForm, 'message' : 'Nuevo vehículo agregado con éxito!', 'newentry' : obj_vehicledata}
            print(f'Saving vehicle: {r_name}-{r_posX},{r_posY}')
            return render(request, self.template_name, context)
        
        elif response.is_valid and models.genVehicle.objects.filter(vehiclemodel = checkmodel).count() != 0:
            context = {'form' : forms.AddVehicleForm, 'errormessage' : 'Ya existe un vehículo con el nombre ingresado.', }
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
    
class EditVehicle(LoginRequiredMixin, TemplateView):
    template_name = 'forms/editvehicle.html'
    
    def get(self, request, editthisvehicle):
        print(f"Editando: '{models.genVehicle.objects.get(vehiclemodel = editthisvehicle)}'.")
        vehicle = models.genVehicle.objects.get(vehiclemodel = editthisvehicle)
        context = {
            'form' : forms.EditVehicleForm(initial = {
                'vehiclemodel' : vehicle.vehiclemodel,
                'vehicleposX' : vehicle.vehicleposX,
                'vehicleposY' : vehicle.vehicleposY,
            })
        }
        return render(request, self.template_name, context)
    
    def post(self, request, editthisvehicle):
        changes = request.POST
        models.genVehicle.objects.update_or_create(vehiclemodel = editthisvehicle,
        defaults = {
            'vehicleposX' : changes.get('vehicleposX'),
            'vehicleposY' : changes.get('vehicleposY'),
            'modificationdate' : datetime.datetime.now(),
            'lastmodifiedby' : str(request.user),
        })
        context = { 'message' : 'Entrada modificada con éxito!' }
        return render(request, self.template_name, context)
    
class DeleteVehicle(LoginRequiredMixin, TemplateView):
    template_name = 'forms/deletevehicle.html'
    
    def get(self, request, deletethisvehicle):
        print(f"Se quiere eliminar: '{deletethisvehicle}'.")
        objetive = models.genVehicle.objects.get(vehiclemodel = deletethisvehicle)
        context = { 'results' : objetive, 'form' : forms.DeleteVehicleForm }
        return render(request, self.template_name, context)
    
    def post(self, request, deletethisvehicle):
        print(f"Eliminando '{deletethisvehicle}'...")
        objetive = models.genVehicle.objects.get(vehiclemodel = deletethisvehicle)
        objetive.delete()
        context = { 'message' : 'La entrada ha sido eliminada.'}
        return render(request, self.template_name, context)
    
# Admins section

class Administrators(TemplateView):
    template_name = 'admins.html'
    
    def get(self, request):
        admins = models.genAdmin.objects.all()
        context = {
            'title' : 'Ver administradores',
            'adminsdata' : admins,
            'amount' : admins.count(),
        }
        return render(request, self.template_name, context)

class AddAdmin(LoginRequiredMixin, TemplateView):
    template_name = 'forms/addadmin.html'
    
    def get(self,request):
        context = { 'title' : 'Agregar administrador', 'form' : forms.AddAdminForm}
        return render(request, self.template_name, context)
    
    def post(self, request):
        context = {'form' : forms.AddAdminForm}
        response = forms.AddAdminForm(request.POST)
        img = request.FILES
        
        if response.is_valid:
            r_id = request.POST['adminid']
            r_accesslevel = request.POST['accesslevel']
            obj_admindata = models.genAdmin(adminid = r_id, 
                                            adminaccesslevel = r_accesslevel,
                                            creationdate = datetime.datetime.now(),
                                            createdby = request.user,
                                            modificationdate = datetime.datetime.now(),
                                            lastmodifiedby = request.user,
                                            adminavatar = img.get('icon'))
            obj_admindata.save()
            print(f'Saving administrator: {r_id}-{r_accesslevel}')
            context = {'form' : forms.AddAdminForm, 'message' : 'Nuevo administrador agregado con éxito!', 'newentry' : obj_admindata}
            
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
    
class EditAdmin(LoginRequiredMixin, TemplateView):
    template_name = 'forms/editadmin.html'
    
    def get(self, request, editthisid):
        print(f"Editando: '{models.genAdmin.objects.get(adminid = editthisid)}'.")
        admin = models.genAdmin.objects.get(adminid = editthisid)
        context = {
            'form' : forms.EditAdminForm(initial = {
                'accesslevel' : admin.adminaccesslevel,
            })
        }
        return render(request, self.template_name, context)
    
    def post(self, request, editthisid):
        changes = request.POST
        models.genAdmin.objects.update_or_create(adminid = editthisid,
            defaults = {
                'adminaccesslevel' : changes.get('accesslevel'),
                'modificationdate' : datetime.datetime.now(),
                'lastmodifiedby' : str(request.user),
            })
        context = { 'message' : 'Entrada modificada con éxito!' }
        return render(request, self.template_name, context)

class DeleteAdmin(LoginRequiredMixin, TemplateView):
    template_name = 'forms/deleteadmin.html'
    
    def get(self, request, deletethisid):
        print(f"Se quiere eliminar: '{deletethisid}'.")
        objetive = models.genAdmin.objects.get(adminid = deletethisid)
        context = { 'results' : objetive, 'form' : forms.DeleteAdminForm }
        return render(request, self.template_name, context)
    
    def post(self, request, deletethisid):
        print(f"Eliminando '{deletethisid}'...")
        objetive = models.genAdmin.objects.get(adminid = deletethisid)
        objetive.delete()
        context = { 'message' : 'La entrada ha sido eliminada.'}
        return render(request, self.template_name, context)