
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages


def index(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, 'first_app/index.html', context)

def register(request):
    if request.method == 'POST':
        error = []
        if request.POST['register']:
            response_from_models = User.objects.register(request.POST)
            if response_from_models['errors']:
                print response_from_models['errors']
                for error in response_from_models['errors']:
                    messages.error(request, error)
            return redirect('logreg:lrroot')
    else:
        return redirect('logreg:lrroot')

def login(request):
    if request.method == 'POST':
        try:
            response_from_signin = User.objects.signin(request.POST)
            if response_from_signin['id']:
                for a in response_from_signin['id']:
                    request.session['id'] = a.id
                    print request.session['id']
                return redirect('appos:aproot')
            else:
                messages.error(request, 'No user in database')
                return redirect ('logreg:lrroot')
        except KeyError:
            messages.error(request, 'No user in database')
            return redirect ('logreg:lrroot')

    else:
        return redirect ('logreg:lrroot')


# def session_test_1(request):
#     request.session['test'] = 'Session Vars Worked!'
#     return http.HttpResponseRedirect('done/?session=%s' % request.session.session_key)
#
# def session_test_2(request):
#     return http.HttpResponse('<br>'.join([
#         request.session.session_key,
#         request.GET.get('session'),
#         request.session.get('test', 'Session is Borked :(')
#          ]))
