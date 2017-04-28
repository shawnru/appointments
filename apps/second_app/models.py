from __future__ import unicode_literals
from ..first_app.models import User
from django.db import models
import datetime

class Appointmentmanager(models.Manager):
    def addappt(self, postdata, userid):
        error = []
        response_to_views = {}
        user = User.objects.get(id=userid)
        date = Appointment.objects.filter(date=postdata['date'])
        time = Appointment.objects.filter(time=postdata['time'])
        answer = False
        if postdata:
            if len(postdata['time']) == 0:
                error.append('Please include a time.')
            if len(postdata['task']) == 0:
                error.append('Please include a task.')
            if len(postdata['date']) == 0:
                error.append('Please include a date for your appointment.')
            if postdata['date'] < unicode(datetime.date.today()):
                error.append('Please pick a current date or future date.')
            for x in date:
                for y in time:
                    if postdata['date'] == x.date and postdata['time'] == y.time:
                        answer = True
            if answer == True:
                error.append('You are busy then, try another date.')
            if error == []:
                self.create(time=postdata['time'],task=postdata['task'],date=postdata['date'],status='Pending',planned_by=user)
        response_to_views['errors'] = error
        return response_to_views

    def update(self, postdata):
        error = []
        response_to_views = {}
        appo = Appointment.objects.get(id=postdata['appoid'])
        answer = False
        date = Appointment.objects.filter(date=postdata['date'])
        time = Appointment.objects.filter(time=postdata['time'])
        if postdata:
            if len(postdata['time']) == 0:
                error.append('Please include a time.')
            if len(postdata['task']) == 0:
                error.append('Please include a task.')
            if len(postdata['date']) == 0:
                error.append('Please include a date for your appointment.')
            if postdata['date'] < unicode(datetime.date.today()):
                error.append('Please pick a current date or future date.')
            for x in date:
                for y in time:
                    if postdata['date'] == x.date and postdata['time'] == y.time:
                        answer = True
            if answer == True:
                error.append('You are busy then, try another date.')
            if error == []:
                appo.time=postdata['time']
                appo.task=postdata['task']
                appo.date=postdata['date']
                appo.status=postdata['status']
                appo.save()
        response_to_views['errors'] = error
        return response_to_views

class Appointment(models.Model):
    time = models.CharField(max_length=200)
    task = models.CharField(max_length=70)
    status = models.CharField(max_length=70)
    date = models.CharField(max_length=70, default=datetime.date.today())
    planned_by = models.ForeignKey(User, related_name='planned_by')
    appointments = models.ManyToManyField(User, related_name='appointments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = Appointmentmanager()
