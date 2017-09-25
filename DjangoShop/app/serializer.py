from rest_framework import serializers
from app.models import *

class GoodSerializer(serializers.HyperlinkedModelSerializer):
    #typeid = serializers.RelatedField(source='goodtype', read_only=True)
    typeid = serializers.IntegerField(source='goodtype.id')
    class Meta:
        model = Good
        fields = ('id','goodname','goodprice','goodcount','goodimg','typeid','gooddesc','goodstatus','pricetype')

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('id','servicename','serviceprice','servicestatus')

class BannerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Banner
        fields = ('id','bannername','bannerimg','bannerdesc')


class TypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Types
        fields = ('id','typename','typeimg')

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('id','placename')

class EchoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Echo
        fields = ('status','message','token','uaddress','uplease')

class UserSerializer(serializers.Serializer):
    userphone = serializers.CharField(required=False, allow_blank=True)
    useraddress = serializers.CharField(required=False, allow_blank=True)
    userplace = serializers.IntegerField(required=False,)
    userpass = serializers.CharField(required=False, allow_blank=True)
    token = serializers.CharField(required=False, allow_blank=True)
    def validate_userphone(self, value):
        try:
            user = User.objects.get(userphone=value)
            raise serializers.ValidationError("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        except User.DoesNotExist: 
            return value

