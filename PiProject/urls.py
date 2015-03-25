from django.conf.urls import patterns, include, url
from django.contrib import admin
from temphumidity.views import HTDataList, HTDataDetail, HTDataTodayList,HTDataWeekList

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myPiStuff.views.home', name='home'),


    url( r'^admin/', include(admin.site.urls)),
 #   url(r'^temphumidity/$', 'temphumidity.views.index'),
 #   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url( r'^htdata/$', HTDataList.as_view(), name = 'data_list' ),
    url( r'^htdata/today/$', HTDataTodayList.as_view(), name = 'data_today_list' ),
    url( r'^htdata/week/$', HTDataWeekList.as_view(), name = 'data_week_list' ),
    url( r'^htdata/(?P<pk>[0-9]+)$', HTDataDetail.as_view(), name = 'data_detail' ),

)
