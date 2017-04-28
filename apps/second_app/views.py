from django.shortcuts import render, redirect
from ..first_app.models import User
from .models import Appointment
from django.contrib import messages
import datetime

def appointments(request):
    if 'id' in request.session:
        user = User.objects.get(id=request.session['id'])
        appt = Appointment.objects.filter(date=datetime.date.today())
        apt = Appointment.objects.exclude(date=datetime.date.today())
        for x in appt:
            appo = Appointment.objects.get(id=x.id)
            appo.appointments.add(user)
        for x in apt:
            appo = Appointment.objects.get(id=x.id)
            appo.appointments.remove(user)

        context = {
            'current_user': User.objects.filter(id=request.session['id']),
            'curr_date_appo_log': Appointment.objects.filter(appointments__id=request.session['id']).order_by('date', 'time'),
            'other_dates_appo_log': Appointment.objects.exclude(appointments__id=request.session['id']).order_by('date', 'time'),
        }
        return render(request, 'second_app/appointments.html', context)

    else:
        return redirect('logreg:lrroot')

def logout(request):
    request.session.clear()
    return redirect('logreg:lrroot')

def appointment(request, appoid, userid):
    if 'id' in request.session:
        context = {
            'appo_deets': Appointment.objects.filter(id=appoid),
        }
        return render(request, 'second_app/appointment.html', context)

    else:
        return redirect('logreg:lrroot')

def add(request, userid):
    if 'id' in request.session:
        if request.method == 'POST':
            response_from_models = Appointment.objects.addappt(request.POST, userid)
            if response_from_models['errors']:
                for error in response_from_models['errors']:
                    messages.error(request, error)
                return redirect('appos:aproot')
            else:
                return redirect('appos:aproot')
    else:
        return redirect('logreg:lrroot')

def update(request):
    if 'id' in request.session:
        if request.method == 'POST':
            response_from_models = Appointment.objects.update(request.POST)
            if response_from_models['errors']:
                for error in response_from_models['errors']:
                    messages.error(request, error)
                return redirect('appos:aproot')
            else:
                return redirect('appos:aproot')
    else:
        return redirect('logreg:lrroot')

def delete(request, appoid):
    if 'id' in request.session:
        if request.method == 'POST':
            Appointment.objects.filter(id=appoid).delete()
            return redirect('appos:aproot')
    else:
        return redirect('logreg:lrroot')
