from django.db import models

# Create your models here.
class HTData(models.Model):
    date = models.DateTimeField()
    temp = models.DecimalField(decimal_places=5, max_digits=10)
    humidity = models.DecimalField(decimal_places=5,max_digits=10)
    deviceid = models.IntegerField()
    def __unicode__(self):              # __unicode__ on Python 2
        return unicode(self.date)

