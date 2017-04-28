from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='lrroot'),
    url(r'^register$', views.register, name='lrreg'),
    url(r'^login$', views.login, name='lrlog'),
    # url(r'^session-test/$', views.session_test_1),
    # url(r'^session-test/done/$', views.session_test_2),

]
