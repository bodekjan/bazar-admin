"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Banner(models.Model):
    bannername = models.CharField(max_length = 50)
    bannerimg = models.FileField(upload_to = 'banner/')
    bannerdate = models.DateTimeField(auto_now_add=True)
    bannerdesc = models.TextField()
    def __unicode__(self):
        return self.bannername

class Types(models.Model):
    typename = models.CharField(max_length = 50)
    typeimg = models.FileField(upload_to = 'types/')
    typedate = models.DateTimeField(auto_now_add=True)
    childcount = models.IntegerField()
    def __unicode__(self):
        return self.typename

class Good(models.Model):
    goodname = models.CharField(max_length = 50)
    #goodtype = models.IntegerField()
    goodtype = models.ForeignKey(Types)
    goodprice = models.FloatField()
    goodcount = models.IntegerField()
    goodimg = models.FileField(upload_to = 'goods/')
    gooddesc = models.TextField()
    gooddate = models.DateTimeField(auto_now_add=True)
    goodstatus = models.IntegerField()
    pricetype = models.IntegerField()
    def __unicode__(self):
        return self.goodname


class Service(models.Model):
    servicename = models.CharField(max_length = 50)
    serviceprice = models.FloatField()
    servicecount = models.IntegerField()
    servicedate = models.DateTimeField(auto_now_add=True)
    servicestatus = models.IntegerField()
    def __unicode__(self):
        return self.servicename

class Place(models.Model):
    placename = models.CharField(max_length = 50)
    childcount = models.IntegerField()
    def __unicode__(self):
        return self.placename
class User(models.Model):
    userphone = models.CharField(max_length = 50)
    userpass = models.CharField(max_length = 50)
    userreguin = models.ForeignKey(Place)
    useraddress = models.CharField(max_length = 250)
    createddate = models.DateTimeField(auto_now_add=True)
    #userorder = models.ForeignKey(Order) 
    def __unicode__(self):
        return self.userphone

class Employee(models.Model):
    ename = models.CharField(max_length = 50)
    epic = models.FileField(upload_to = 'emp/')
    ephone = models.CharField(max_length = 50)
    edate = models.DateTimeField(auto_now_add=True)
    estatus = models.IntegerField()
    ecount = models.IntegerField()
    #userorder = models.ForeignKey(Order) 
    def __unicode__(self):
        return self.userphone

class Echo(models.Model):
    status = models.IntegerField()
    message = models.CharField(max_length = 250)
    token = models.CharField(max_length = 250)
    uaddress = models.CharField(max_length = 250)
    uplease = models.IntegerField()
    def __unicode__(self):
        return self.status
