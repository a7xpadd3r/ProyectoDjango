from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your models here.
# Primer entrega del proyecto final (12/04/22)

# Datos de jugador
class genUser(models.Model):
    usernick = models.CharField(max_length=15)
    userid = models.IntegerField()
    userlastconnection = models.DateField()
    # Position in world
    userposX = models.IntegerField()
    userposY = models.IntegerField()
    userposZ = models.IntegerField()
    creationdate = models.DateField(blank = True, null = True)
    modificationdate = models.DateField(blank = True, null = True)
    createdby = models.CharField(max_length=30, blank = True, null = True)
    lastmodifiedby = models.CharField(max_length=30, blank = True, null = True)
    playericon = models.ImageField(upload_to = 'players', blank = True, null = True)
    def __str__(self) -> str:
        return f'({self.userid}) {self.usernick} - {self.userlastconnection}'
    
# Datos de ítems

class genItem(models.Model):
    itemname = models.CharField(max_length=20)
    itemquantity = models.IntegerField()
    # Position in world
    itemposX = models.IntegerField()
    itemposY = models.IntegerField()
    itemposZ = models.IntegerField()
    creationdate = models.DateField(blank = True, null = True)
    modificationdate = models.DateField(blank = True, null = True)
    createdby = models.CharField(max_length=30, blank = True, null = True)
    lastmodifiedby = models.CharField(max_length=30, blank = True, null = True)
    itemicon = models.ImageField(upload_to = 'items', blank = True, null = True)
    def __str__(self) -> str:
        return f'{self.itemname} - {self.itemquantity}'
    
# Datos de vehículos
class genVehicle(models.Model):
    vehiclemodel = models.CharField(max_length=30)
    # Position in world
    vehicleposX = models.IntegerField()
    vehicleposY = models.IntegerField()
    creationdate = models.DateField(blank = True, null = True)
    modificationdate = models.DateField(blank = True, null = True)
    createdby = models.CharField(max_length=30, blank = True, null = True)
    lastmodifiedby = models.CharField(max_length=30, blank = True, null = True)
    vehicleicon = models.ImageField(upload_to = 'vehicles', blank = True, null = True)
    def __str__(self) -> str:
        return f'{self.vehiclemodel}'
    
# Extra: Datos de administradores
class genAdmin(models.Model):
    adminid = models.IntegerField()
    adminaccesslevel = models.CharField(max_length=20)
    creationdate = models.DateField(blank = True, null = True)
    modificationdate = models.DateField(blank = True, null = True)
    createdby = models.CharField(max_length=30, blank = True, null = True)
    lastmodifiedby = models.CharField(max_length=30, blank = True, null = True)
    adminavatar = models.ImageField(upload_to = 'admins', blank = True, null = True)
    def __str__(self) -> str:
        return f'{self.adminid} ({self.adminaccesslevel})'