from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.appointments, name='aproot'),
    url(r'^logout$', views.logout, name='apout'),
    url(r'^appo/(?P<appoid>\d+)/(?P<userid>\d+)$', views.appointment, name='apappo'),
    url(r'^add/(?P<userid>\d+)$', views.add, name='apadd'),
    url(r'^delete/(?P<appoid>\d+)$', views.delete, name='apdel'),
    url(r'^update$', views.update, name='apedit'),
]
