from xmlrpc.client import DateTime
from django import forms
import datetime

# Players #######################################
class AddUserForm(forms.Form):
    usernick = forms.CharField(max_length=15)
    userid = forms.IntegerField()
    userlastconnection = forms.DateField()
    # Position in world
    userposX = forms.IntegerField()
    userposY = forms.IntegerField()
    userposZ = forms.IntegerField()
    icon = forms.ImageField()
    
class EditUserForm(forms.Form):
    usernick = forms.CharField(max_length=15)
    userlastconnection = forms.DateField()
    # Position in world
    userposX = forms.IntegerField()
    userposY = forms.IntegerField()
    userposZ = forms.IntegerField()
    
class DeleteUserForm(forms.Form):
    deleteid = ''

class SearchUserForm(forms.Form):
    usernick = forms.CharField(max_length=15)
    
# Items #######################################
class AddItemForm(forms.Form):
    itemname = forms.CharField(max_length=20)
    itemquantity = forms.IntegerField()
    # Position in world
    itemposX = forms.IntegerField()
    itemposY = forms.IntegerField()
    itemposZ = forms.IntegerField()
    icon = forms.ImageField()

class EditItemForm(forms.Form):
    itemquantity = forms.IntegerField()
    # Position in world
    itemposX = forms.IntegerField()
    itemposY = forms.IntegerField()
    itemposZ = forms.IntegerField()
    modificationdate = datetime.datetime.now()

class SearchItemForm(forms.Form):
    item = forms.CharField()
    
class DeleteItemForm(forms.Form):
    deletename = ''

# Vehicles #######################################
class AddVehicleForm(forms.Form):
    vehiclemodel = forms.CharField(max_length=30)
    # Position in world
    vehicleposX = forms.IntegerField()
    vehicleposY = forms.IntegerField()
    icon = forms.ImageField()

class SearchVehicleForm(forms.Form):
    vehicle = forms.CharField(max_length=30)
    
class EditVehicleForm(forms.Form):
    # Position in world
    vehicleposX = forms.IntegerField()
    vehicleposY = forms.IntegerField()
    
class DeleteVehicleForm(forms.Form):
    deletename = ''
    
# Admins #######################################
class AddAdminForm(forms.Form):
    adminid = forms.IntegerField()
    accesslevel = forms.CharField(max_length=20)
    icon = forms.ImageField()
    
class SearchAdminForm(forms.Form):
    accesslevel = forms.CharField(max_length=20)
    
class EditAdminForm(forms.Form):
    accesslevel = forms.CharField(max_length=20)
    
class DeleteAdminForm(forms.Form):
    accesslevel = ''
