from django.db import models

# Create your models here.
class HTData(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    temp = models.DecimalField(decimal_places=15, max_digits=20)
    humidity = models.DecimalField(decimal_places=15,max_digits=20)
    deviceid = models.IntegerField()
    def __unicode__(self):              # __unicode__ on Python 2
        return unicode(self.date)

