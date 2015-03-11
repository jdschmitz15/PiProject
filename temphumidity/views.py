
from temphumidity.models import HTData
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import (
ListCreateAPIView, RetrieveUpdateDestroyAPIView )
from serializers import HTDataSerializer



class HTDataMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = HTData.objects.all()
    serializer_class = HTDataSerializer

class HTDataList(HTDataMixin, ListCreateAPIView):
    """
    Return a list of all the tasks, or
    create new ones
    """
    pass

class HTDataDetail(HTDataMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific task, update it, or delete it.
    """
    pass