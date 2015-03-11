# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HTData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('temp', models.DecimalField(max_digits=10, decimal_places=5)),
                ('humidity', models.DecimalField(max_digits=10, decimal_places=5)),
                ('deviceid', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
