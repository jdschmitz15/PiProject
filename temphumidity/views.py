
from temphumidity.models import HTData
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView )
from serializers import HTDataSerializer
from datetime import datetime, timedelta


class HTDataMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = HTData.objects.all()
    serializer_class = HTDataSerializer

class HTDataTodayList(ListCreateAPIView):
    """
    Return a list of all the tasks, or
    create new ones
    """
    today = datetime.today()
    queryset = HTData.objects.filter(date__year=today.year, date__month=today.month,date__day=today.day)
    serializer_class = HTDataSerializer

class HTDataWeekList(ListCreateAPIView):
    """
    Return a list of all the tasks, or
    create new ones
    """
    startdate = datetime.today()
    enddate = startdate - timedelta(days=6)
    queryset = HTData.objects.filter(date__range=[ enddate,startdate])
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

