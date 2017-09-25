"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm
from app.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
class GoodsForm(ModelForm):
    good_type = (
    (0, u'普通用户'),
        (1, u'高级用户'),)
    goodid = forms.IntegerField(required=False)
    goodname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    goodtype = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    goodstatus = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pricetype = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    goodprice = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    goodcount = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    gooddesc = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    goodimg = forms.FileField(required=False,widget=forms.FileInput(attrs={'class': 'form-control','id':'goodimg'}))
    class Meta:
        model = Good
        #fields = '__all__'
        fields = ['goodname', 'goodprice', 'goodcount', 'goodimg', 'pricetype', 'gooddesc']

class ServiceForm(ModelForm):
    serviceid = forms.IntegerField(required=False)
    servicename = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    servicestatus = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    serviceprice = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Service
        fields = ['servicename', 'servicestatus', 'serviceprice']

class TypeForm(ModelForm):
    typeid = forms.IntegerField(required=False)
    typename = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    typeimg = forms.FileField(required=False,widget=forms.FileInput(attrs={'class': 'form-control','id':'typeimg'}))
    class Meta:
        model = Types
        #fields = '__all__'
        fields = ['typename', 'typeimg']

class PlaceForm(ModelForm):
    placeid = forms.IntegerField(required=False)
    placename = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Place
        #fields = '__all__'
        fields = ['placename']

class UserForm(ModelForm):
    userphone = forms.CharField(required=False)
    userpass = forms.CharField(required=False)
    useraddress = forms.CharField(required=False)
    userplace = forms.IntegerField(required=False)
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['userphone']



class BannerForm(ModelForm):
    bannerid = forms.IntegerField(required=False)
    bannername = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    bannerimg = forms.FileField(required=False,widget=forms.FileInput(attrs={'class': 'form-control','id':'bannerimg'}))
    bannerdesc = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Banner
        fields = ['bannername','bannerimg','bannerdesc']

class EmployeeForm(ModelForm):
    empid = forms.IntegerField(required=False)
    ename = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    epic = forms.FileField(required=False,widget=forms.FileInput(attrs={'class': 'form-control','id':'goodimg'}))
    ephone = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Employee
        #fields = '__all__'
        fields = ['ename']
        fields = ['ename', 'ephone']
