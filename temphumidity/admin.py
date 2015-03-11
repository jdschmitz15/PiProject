from django.contrib import admin
from temphumidity.models import HTData



class htdataAdmin(admin.ModelAdmin):
    fields = ['date','deviceid','temp','humidity']

# Register your models here.
admin.site.register(HTData,htdataAdmin)

