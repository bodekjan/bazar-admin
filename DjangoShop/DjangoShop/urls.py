"""
Definition of urls for DjangoShop.
"""

from datetime import datetime
from django.conf.urls import url, include
import django.contrib.auth.views
from django.conf import settings
from django.conf.urls.static import static
#from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns



import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

# rest fucker url
#router = routers.DefaultRouter()
#router.register(r'goods', app.views.GoodViewSet)
#router.register(r'^goods/$', app.views.goodList, base_name='rest')


urlpatterns = [
    # rest fucker
    url(r'^api/user', app.views.UserApi),
    url(r'^api/generate', app.views.GenerateApi),
    url(r'^api/type', app.views.TypeApi),
    url(r'^api/goods/$', app.views.GoodApi),
    url(r'^api/service/$', app.views.ServiceApi),
    url(r'^api/places/$', app.views.PlaceApi),
    url(r'^api/banner/$', app.views.BannerApi),
    url(r'^api/goods/(?P<id>[0-9]+)/$', app.views.GoodDetailApi),
    url(r'^api/banner/(?P<id>[0-9]+)/$', app.views.BannerDetailApi),
    # Examples:
    url(r'^$', app.views.main, name='main'),
    #url(r'^rest', include(router.urls)),
    url(r'^main', app.views.main, name='main'),
    url(r'^login', app.views.login, name='login'),
    url(r'^logout', app.views.logout, name='logout'),
    url(r'^setting', app.views.setting, name='setting'),
    url(r'^goodlist', app.views.goodList, name='goodlist'),
    url(r'^typelist', app.views.typeList, name='typelist'),
    url(r'^userlist', app.views.userList, name='userlist'),
    url(r'^placelist', app.views.placeList, name='placelist'),
    url(r'^bannerlist', app.views.bannerList, name='bannerlist'),
    url(r'^servicelist', app.views.serviceList, name='servicelist'),
    url(r'^employeelist', app.views.employeeList, name='employelist'),
    url(r'^billlist', app.views.billList, name='billlist'),
    url(r'^addgood', app.views.addGood, name='addgood'),
    url(r'^addtype', app.views.addType, name='addtype'),
    url(r'^addplace', app.views.addPlace, name='addplace'),
    url(r'^addservice', app.views.addService, name='addservice'),
    url(r'^addbanner', app.views.addBanner, name='addbanner'),
    url(r'^addemployee', app.views.addEmployee, name='addemployee'),
    url(r'^goodalert', app.views.goodAlert, name='goodalert'),
    url(r'^errorlist', app.views.errorList, name='errorlost'),
    url(r'^urgentbill', app.views.urgentBill, name='urgentbill'),
    url(r'^sys', app.views.sysCommand, name='syscommand'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)
