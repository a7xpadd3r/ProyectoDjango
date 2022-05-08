from django import forms


# Players
class AddUserForm(forms.Form):
    usernick = forms.CharField(max_length=15)
    userid = forms.IntegerField()
    userlastconnection = forms.DateField()
    # Position in world
    userposX = forms.IntegerField()
    userposY = forms.IntegerField()
    userposZ = forms.IntegerField()

class SearchUserForm(forms.Form):
    usernick = forms.CharField(max_length=15)

# Items
class AddItemForm(forms.Form):
    itemname = forms.CharField(max_length=20)
    itemquantity = forms.IntegerField()
    # Position in world
    itemposX = forms.IntegerField()
    itemposY = forms.IntegerField()
    itemposZ = forms.IntegerField() 

class SearchItemForm(forms.Form):
    item = forms.CharField()

# Vehicles
class AddVehicleForm(forms.Form):
    vehiclemodel = forms.CharField(max_length=20)
    # Position in world
    vehicleposX = forms.IntegerField()
    vehicleposY = forms.IntegerField()

class SearchVehicleForm(forms.Form):
    vehicle = forms.CharField(max_length=30)
    
# Admins
class AddAdminForm(forms.Form):
    adminid = forms.IntegerField()
    accesslevel = forms.CharField(max_length=20)
    
class SearchAdminForm(forms.Form):
    accesslevel = forms.CharField(max_length=20)
