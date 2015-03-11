from django.forms import widgets
from rest_framework import serializers
from temphumidity.models import HTData

class HTDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HTData
        fields = ('id','date','deviceid','temp','humidity')