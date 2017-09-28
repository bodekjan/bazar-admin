"""
Definition of views.
"""
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext
from datetime import datetime
from app.forms import *
from app.models import *
from app.serializer import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.db.models.aggregates import Count
import os

def main(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    # stastics
    userCount = User.objects.count()
    goodCount = Good.objects.count()
    return render(
        request,
        'app/mainpage.html',
        {
            'title':'Home Page',
            'usercount': userCount ,
            'goodcount': goodCount
        }
    )

def logout(request):
    del request.session['login']
    return redirect('login')


def login(request):
    if request.method == 'POST':
        username=request.POST['uname']
        password=request.POST['password']
        if username =='askar' and password == '123456':
            request.session['login'] =True
            return redirect('/main')
        else:
            return render(
                request,
                'app/pages-login.html',
                {
                    'title':'Home Page',
                    'year':datetime.now().year,
                }
            )
    else:
        return render(
            request,
            'app/pages-login.html',
            {
                'title':'Home Page',
                'year':datetime.now().year,
            }
        )


def errorList(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    return render(
        request,
        'app/errorlist.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


def billList(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    return render(
        request,
        'app/billlist.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


def urgentBill(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    return render(
        request,
        'app/urgentBill.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


def setting(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    return render(
        request,
        'app/settingpage.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


def goodList(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    defKey = ""
    defType = -1
    method = request.GET.get('method')
    typeId = request.GET.get('type')
    if(typeId!=None):
        typeId = int(typeId)
    keyVal = request.GET.get('key')
    types = Types.objects.all()
    if(method=='delete'):
        goodId = request.GET.get('id')
        Good.objects.filter(id=goodId).delete()
    if(typeId!=None or keyVal!=None):
        if(keyVal==None):
            keyVal = ""
        defKey = keyVal
        if(typeId==None):
            goods = Good.objects.select_related().filter(goodname__contains=keyVal).values_list('id','goodname','goodprice','goodcount','goodimg','gooddate','goodtype__typename','goodtype__typeimg','goodstatus','pricetype')
        else:
            defType = typeId
            if(typeId==-1):
                goods = Good.objects.select_related().filter(goodname__contains=keyVal).values_list('id','goodname','goodprice','goodcount','goodimg','gooddate','goodtype__typename','goodtype__typeimg','goodstatus','pricetype')
            else:
                goods = Good.objects.select_related().filter(goodname__contains=keyVal,goodtype__id=defType).values_list('id','goodname','goodprice','goodcount','goodimg','gooddate','goodtype__typename','goodtype__typeimg','goodstatus','pricetype')
            
    else:
        goods = Good.objects.select_related().all().values_list('id','goodname','goodprice','goodcount','goodimg','gooddate','goodtype__typename','goodtype__typeimg','goodstatus','pricetype')
    return render(
        request,
        'app/goodlist.html',
        {
            'status':'success',
            'message':'',
            'goods':goods,
            'types':types,
            'key':defKey,
            'typeid':int(defType),
        }
    )


def bannerList(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    method = request.GET.get('method')
    if(method=='delete'):
        bannerId = request.GET.get('id')
        Banner.objects.filter(id=bannerId).delete()
    banners = Banner.objects.select_related().all().values_list('id','bannername','bannerimg','bannerdate','bannerdesc')
    return render(
        request,
        'app/bannerlist.html',
        {
            'status':'success',
            'message':'',
            'banners':banners,
        }
    )

def serviceList(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    method = request.GET.get('method')
    if(method=='delete'):
        serviceId = request.GET.get('id')
        Service.objects.filter(id=serviceId).delete()
    servives = Service.objects.select_related().all().values_list('id','servicename','servicedate','serviceprice','servicecount','servicestatus')
    return render(
        request,
        'app/servicelist.html',
        {
            'status':'success',
            'message':'',
            'servives':servives,
        }
    )

def typeList(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    method = request.GET.get('method')
    if(method=='delete'):
        typeId = request.GET.get('id')
        Types.objects.filter(id=typeId).delete()
    types = Types.objects.all().annotate(
    num_goods=Count('good')).values_list()
    return render(
        request,
        'app/typelist.html',
        {
            'status':'success',
            'message':'',
            'types':types,
        }
    )

def employeeList(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    method = request.GET.get('method')
    if(method=='delete'):
        empId = request.GET.get('id')
        Employee.objects.filter(id=empId).delete()
    emp = Employee.objects.select_related().all().values_list('id','epic','ename','ephone','edate','estatus','ecount')
    return render(
        request,
        'app/employeelist.html',
        {
            'status':'success',
            'message':'',
            'emp':emp,
        }
    )

def userList(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    users = User.objects.all().values_list()
    users = User.objects.select_related().all().values_list('id','userphone','useraddress','createddate','userreguin__placename')
    return render(
        request,
        'app/userlist.html',
        {
            'status':'success',
            'message':'',
            'users':users,
        }
    )

def placeList(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    method = request.GET.get('method')
    if(method=='delete'):
        placeId = request.GET.get('id')
        Place.objects.filter(id=placeId).delete()
    places = Place.objects.all().annotate(
    num_users=Count('user')).values_list()
    return render(
        request,
        'app/placelist.html',
        {
            'status':'success',
            'message':'',
            'places':places,
        }
    )
def addEmployee(request):
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    if request.method == "POST":
        emp = EmployeeForm(request.POST,request.FILES)
        if emp.is_valid():
            #获取表单信息
            #写入数据库
            employee = Employee()
            employee.estatus = 0
            employee.ecount = 0
            employee.ename =  emp.cleaned_data['ename']
            employee.ephone =  emp.cleaned_data['ephone']
            if( emp.cleaned_data['epic']!=None):
                employee.epic =  emp.cleaned_data['epic']
            if( emp.cleaned_data['empid']!=None):
                if( emp.cleaned_data['epic']!=None):
                    t = Employee.objects.get(id=emp.cleaned_data['empid'])
                    t.ename = employee.ename
                    t.ephone = employee.ephone
                    t.epic = employee.epic
                    t.save()
                else:
                    Employee.objects.filter(id=emp.cleaned_data['empid']).update(ename = employee.ename,ephone = employee.ephone)
            else:
                employee.save()
            return render(
                request,
                'app/addemployee.html',
                {
                    'status':'success',
                    'message':'yessss',
                    'emp':emp,
                }
            )
        else:
            print(emp.errors)
            return render(
                request,
                'app/addemployee.html',
                {
                    'status':'error',
                    'message':'aaaaaaaaaaaaaaaaaaaaaaaaa',
                    'types':emp,
                }
            )
    else:
        method = request.GET.get('method')
        if(method=='edit'):
            empId = request.GET.get('id')
            empModel = Employee.objects.get(id=empId)
            emp = EmployeeForm()
            emp = EmployeeForm(instance=empModel)
            return render(
                request,
                'app/addemployee.html',
                {
                    'status':'edit',
                    'message':'',
                    'model':empModel,
                    'emp':emp,
                }
            )
        else:
            emp = EmployeeForm()
    return render(
        request,
        'app/addemployee.html',
        {
            'status':'default',
            'message':'',
            'emp':emp,
        }
    )

def addType(request):
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    if request.method == "POST":
        types = TypeForm(request.POST,request.FILES)
        if types.is_valid():
            #获取表单信息
            #写入数据库
            type = Types()
            type.childcount = 0
            type.typename = types.cleaned_data['typename']
            if(types.cleaned_data['typeimg']!=None):
                type.typeimg = types.cleaned_data['typeimg']
            if(types.cleaned_data['typeid']!=None):
                if(types.cleaned_data['typeimg']!=None):
                    t = Types.objects.get(id=types.cleaned_data['typeid'])
                    t.typename = type.typename
                    t.typeimg = type.typeimg
                    t.save()
                    #Types.objects.filter(id=types.cleaned_data['typeid']).update(typename = type.typename,typeimg = type.typeimg)
                else:
                    Types.objects.filter(id=types.cleaned_data['typeid']).update(typename = type.typename)
            else:
                type.save()
            return render(
                request,
                'app/addtype.html',
                {
                    'status':'success',
                    'message':'yessss',
                    'types':types,
                }
            )
        else:
            print(types.errors)
            return render(
                request,
                'app/addtype.html',
                {
                    'status':'error',
                    'message':'aaaaaaaaaaaaaaaaaaaaaaaaa',
                    'types':types,
                }
            )
    else:
        method = request.GET.get('method')
        if(method=='edit'):
            typeId = request.GET.get('id')
            typeModel = Types.objects.get(id=typeId)
            types = TypeForm()
            types = TypeForm(instance=typeModel)
            return render(
                request,
                'app/addtype.html',
                {
                    'status':'edit',
                    'message':'',
                    'model':typeModel,
                    'types':types,
                }
            )
        else:
            types = TypeForm()
    return render(
        request,
        'app/addtype.html',
        {
            'status':'default',
            'message':'',
            'types':types,
        }
    )

def addBanner(request):
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    if request.method == "POST":
        banners = BannerForm(request.POST,request.FILES)
        if banners.is_valid():
            #获取表单信息
            #写入数据库
            banner = Banner()
            banner.bannername = banners.cleaned_data['bannername']
            banner.bannerimg = banners.cleaned_data['bannerimg']
            banner.bannerdesc = banners.cleaned_data['bannerdesc']
            if(banners.cleaned_data['bannerimg']!=None):
                banner.bannerimg = banners.cleaned_data['bannerimg']
            if(banners.cleaned_data['bannerid']!=None):
                if(banners.cleaned_data['bannerimg']!=None):
                    t = Banner.objects.get(id=banners.cleaned_data['bannerid'])
                    t.bannername = banner.bannername
                    t.bannerimg = banner.bannerimg
                    t.bannerdesc = banner.bannerdesc
                    t.save()
                else:
                    Banner.objects.filter(id=banners.cleaned_data['bannerid']).update(bannername = banner.bannername,bannerdesc = banner.bannerdesc)
            else:
                banner.save()
            return render(
                request,
                'app/addbanner.html',
                {
                    'status':'success',
                    'message':'yessss',
                    'banners':banners,
                }
            )
        else:
            return render(
                request,
                'app/addbanner.html',
                {
                    'status':'error',
                    'message':'aaaaaaaaaaaaaaaaaaaaaaaaa',
                    'banners':banners,
                }
            )
    else:
        method = request.GET.get('method')
        if(method=='edit'):
            bannerId = request.GET.get('id')
            bannerModel = Banner.objects.get(id=bannerId)
            banners = BannerForm()
            banners = BannerForm(instance=bannerModel)
            return render(
                request,
                'app/addbanner.html',
                {
                    'status':'edit',
                    'message':'',
                    'model':bannerModel,
                    'banners':banners,
                }
            )
        else:
            banners = BannerForm()
    return render(
        request,
        'app/addbanner.html',
        {
            'status':'default',
            'message':'',
            'banners':banners,
        }
    )

def addPlace(request):
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    if request.method == "POST":
        places = PlaceForm(request.POST,request.FILES)
        if places.is_valid():
            #获取表单信息
            #写入数据库
            place = Place()
            place.childcount = 0
            place.placename = places.cleaned_data['placename']
            if(places.cleaned_data['placeid']!=None):
                Place.objects.filter(id=places.cleaned_data['placeid']).update(placename = place.placename)
            else:
                place.save()
            return render(
                request,
                'app/addplace.html',
                {
                    'status':'success',
                    'message':'yessss',
                    'places':places,
                }
            )
        else:
            print(types.errors)
            return render(
                request,
                'app/addtype.html',
                {
                    'status':'error',
                    'message':'aaaaaaaaaaaaaaaaaaaaaaaaa',
                    'places':places,
                }
            )
    else:
        method = request.GET.get('method')
        if(method=='edit'):
            placeId = request.GET.get('id')
            placeModel = Place.objects.get(id=placeId)
            places = PlaceForm()
            places = PlaceForm(instance=placeModel)
            return render(
                request,
                'app/addplace.html',
                {
                    'status':'edit',
                    'message':'',
                    'model':placeModel,
                    'places':places,
                }
            )
        else:
            places = PlaceForm()
    return render(
        request,
        'app/addplace.html',
        {
            'status':'default',
            'message':'',
            'places':places,
        }
    )

def addGood(request):
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    types = Types.objects.all().values_list()
    if request.method == "POST":
        goods = GoodsForm(request.POST,request.FILES)
        if goods.is_valid():
            #获取表单信息
            #写入数据库
            good = Good()
            good.goodname = goods.cleaned_data['goodname']
            good.goodtype = Types.objects.get(id=goods.cleaned_data['goodtype'])
            good.goodprice = goods.cleaned_data['goodprice']
            good.goodcount = goods.cleaned_data['goodcount']
            good.gooddesc = goods.cleaned_data['gooddesc']
            good.goodimg = goods.cleaned_data['goodimg']
            good.goodstatus = goods.cleaned_data['goodstatus']
            good.pricetype = goods.cleaned_data['pricetype']
            if(goods.cleaned_data['goodimg']!=None):
                good.goodimg = goods.cleaned_data['goodimg']
            if(goods.cleaned_data['goodid']!=None):
                if(goods.cleaned_data['goodimg']!=None):
                    g = Good.objects.get(id=goods.cleaned_data['goodid'])
                    g.goodname = good.goodname
                    g.goodtype = good.goodtype
                    g.goodprice = good.goodprice
                    g.goodcount = good.goodcount
                    g.gooddesc = good.gooddesc
                    g.goodimg = good.goodimg
                    g.goodstatus = good.goodstatus
                    g.pricetype = good.pricetype
                    g.save()
                else:
                    Good.objects.filter(id=goods.cleaned_data['goodid']).update(goodname = good.goodname,goodtype = good.goodtype,goodprice = good.goodprice,goodcount = good.goodcount,gooddesc = good.gooddesc,goodstatus = good.goodstatus, pricetype = good.pricetype)
            else:
                good.save()
            return render(
                request,
                'app/addgood.html',
                {
                    'status':'success',
                    'message':'yessss',
                    'goods':goods,
                    'types': types,
                }
            )
        else:
            return render(
                request,
                'app/addgood.html',
                {
                    'status':'error',
                    'message':'aaaaaaaaaaaaaaaaaaaaaaaaa',
                    'goods':goods,
                    'types': types,
                }
            )
    else:
        method = request.GET.get('method')
        if(method=='edit'):
            goodId = request.GET.get('id')
            goodModel = Good.objects.get(id=goodId)
            goods = GoodsForm()
            goods = GoodsForm(instance=goodModel)
            return render(
                request,
                'app/addgood.html',
                {
                    'status':'edit',
                    'message':'',
                    'model':goodModel,
                    'goods':goods,
                    'types': types,
                }
            )
        else:
            goods = GoodsForm()
    return render(
        request,
        'app/addgood.html',
        {
            'status':'default',
            'message':'',
            'goods':goods,
            'types': types,
        }
    )

def addService(request):
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    if request.method == "POST":
        services = ServiceForm(request.POST,request.FILES)
        if services.is_valid():
            #获取表单信息
            #写入数据库
            service = Service()
            service.servicename = services.cleaned_data['servicename']
            service.servicestatus = services.cleaned_data['servicestatus']
            service.serviceprice = services.cleaned_data['serviceprice']
            service.servicecount = 0
            if(services.cleaned_data['serviceid']!=None):
                Service.objects.filter(id=services.cleaned_data['serviceid']).update(servicename = service.servicename,servicestatus = service.servicestatus,serviceprice = service.serviceprice)
            else:
                service.save()
            return render(
                request,
                'app/addservice.html',
                {
                    'status':'success',
                    'message':'yessss',
                    'services':services,
                }
            )
        else:
            return render(
                request,
                'app/addservice.html',
                {
                    'status':'error',
                    'message':'aaaaaaaaaaaaaaaaaaaaaaaaa',
                    'services':services,
                }
            )
    else:
        method = request.GET.get('method')
        if(method=='edit'):
            serviceId = request.GET.get('id')
            serviceModel = Service.objects.get(id=serviceId)
            services = ServiceForm()
            services = ServiceForm(instance=serviceModel)
            return render(
                request,
                'app/addservice.html',
                {
                    'status':'edit',
                    'message':'',
                    'model':serviceModel,
                    'services':services,
                }
            )
        else:
            services = ServiceForm()
    return render(
        request,
        'app/addservice.html',
        {
            'status':'default',
            'message':'',
            'services':services,
        }
    )



def goodAlert(request):
    """Renders the about page."""
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    return render(
        request,
        'app/goodalert.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

# simple ajax ( system command )
def sysCommand(request):
    """Renders the about page."""
    #assert isinstance(request, HttpRequest)
    is_login = request.session.get('login',False)
    if is_login==False:
        return redirect('/login')
    name_dict = {'status': 'error', 'msg': 'قۇرۇق'}
    command = request.POST.get('command','null') 
    if(command == 'mysql'):
        os.system('net stop mysql')
        os.system('net start mysql')
        name_dict = {'status': 'success', 'msg': 'ساندان قايتا قوزغىلىۋاتىدۇ، ھىچنىمىگە چېقىلماي 5 مىنۇت ساقلاپ تۇرۇپ ئاندىن مەشخۇلات قىلىڭ'}
    if(command == 'apache'):
        os.system('net stop apache2.4')
        os.system('net start apache2.4')
        name_dict = {'status': 'success', 'msg': 'ئاپاچى قايتا قوزغىلىۋاتىدۇ، ھىچنىمىگە چېقىلماي بەش مىنۇت ساقلاپ ئاندىن مەشخۇلات قىلىڭ'}
    if(command == 'win'):
        os.system('shutdown.exe -r -t 10')
        name_dict = {'status': 'success', 'msg': 'مۇلازىمىر قايتا قوزغىلىشقا باشلىدى، ھىچنىمىگە چېقىلماي 5 مىنۇت ساقلاپ ئاندىن مەشفۇلات قىلىڭ'}
    return JsonResponse(name_dict)


# api work zone

@csrf_exempt
@api_view(['POST'])
def GenerateApi(request):
    """
    List all snippets, or create a new snippet.
    """
    xrequest = request.data
    if request.method == 'POST':
        serializer = UserSerializer(data=xrequest)
        serializer.is_valid()
        user = User()
        user.userphone = serializer.data.get('userphone')
        user.userpass = serializer.data.get('userpass')
        try:
            inUser = User.objects.get(userphone=user.userphone)
            # 成功并返回石头世纪token值
            if(inUser.userpass == user.userpass):
                echo = Echo()
                echo.status = 200
                echo.message = 'success'
                echo.token = '11111111111111111111111111111111111'
                echo.uaddress = inUser.useraddress
                echo.uplease = inUser.userreguin.id
                echolizer = EchoSerializer(echo, many=False)
                return Response(echolizer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist: 
            # 成功并返回石头世纪token值
            print("wrong number");
        echo = Echo()
        echo.status = 204
        echo.message = 'wrong'
        echo.token = ''
        echolizer = EchoSerializer(echo, many=False)
        return Response(echolizer.data, status=status.HTTP_200_OK)
# rest fucker
@csrf_exempt
@api_view(['POST'])
def UserApi(request):
    """
    List all snippets, or create a new snippet.
    """
    mrequest = request.data
    if request.method == 'POST':
        serializer = UserSerializer(data=mrequest)
        if (serializer.is_valid()):
            user = User()
            user.userphone = serializer.validated_data.get('userphone')
            user.useraddress = serializer.validated_data.get('useraddress')
            user.userpass = serializer.validated_data.get('userpass')
            user.userreguin = Place.objects.get(id=serializer.validated_data.get('userplace'))
            user.save()
            # 成功并返回石头世纪token值
            echo = Echo()
            echo.status = 200
            echo.message = 'success'
            echo.token = '11111111111111111111111111111111111'
            echolizer = EchoSerializer(echo, many=False)
            return Response(echolizer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_201_CREATED)


        
# rest fucker
@api_view(['GET'])
def PlaceApi(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Place.objects.all()
        serializer = PlaceSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['GET'])
def TypeApi(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Types.objects.all()
        serializer = TypesSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['GET'])
def BannerApi(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Banner.objects.all()
        serializer = BannerSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['GET'])
def GoodApi(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        good = Good.objects.all()
        serializer = GoodSerializer(good, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['GET'])
def ServiceApi(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        service = Service.objects.all()
        serializer = ServiceSerializer(service, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['GET'])
def GoodDetailApi(request,id):
    """
    List all snippets, or create a new snippet.
    """
    try:
        good = Good.objects.get(id=id)
    except Good.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GoodSerializer(good)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['GET'])
def BannerDetailApi(request,id):
    """
    List all snippets, or create a new snippet.
    """
    try:
        banner = Banner.objects.get(id=id)
    except Banner.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BannerSerializer(banner)
        return JsonResponse(serializer.data, safe=False)
'''
@csrf_exempt
def goodApiList(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        good = Good.objects.all()
        serializer = GoodSerializer(good, many=True)s
        return JsonResponse(serializer.data, safe=False)
@csrf_exempt
def goodApiDetail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        good = Good.objects.get(id=id)
    except Good.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GoodSerializer(good)
        return JsonResponse(serializer.data)

@csrf_exempt
def placeApiList(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        place = Place.objects.all()
        serializer = PlaceSerializer(place, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def userApi(request):
    if request.method == 'POST':
        print(request.data)
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        try:
            user = User.objects.get(userphone=serializer.userphone)
        except User.DoesNotExist:
            return Response(status=status.HTTP_200_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserApi(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        try:
            user = User.objects.get(userphone=serializer.userphone)
        except User.DoesNotExist:
            return Response(status=status.HTTP_200_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''