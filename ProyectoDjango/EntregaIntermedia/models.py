from django.db import models

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
    
# Datos de ítems
class genItem(models.Model):
    itemname = models.CharField(max_length=20)
    itemquantity = models.IntegerField()
    # Position in world
    itemposX = models.IntegerField()
    itemposY = models.IntegerField()
    itemposZ = models.IntegerField()
    
# Datos de vehículos
class genVehicle(models.Model):
    vehiclemodel = models.CharField(max_length=30)
    # Position in world
    vehicleposX = models.IntegerField()
    vehicleposY = models.IntegerField()
    
# Extra: Datos de administradores
class genAdmin(models.Model):
    adminid = models.IntegerField()
    adminaccesslevel = models.CharField(max_length=20)