from django.conf.urls import patterns, url
from unity import views

urlpatterns = patterns(
    '',
    # url(r'^$', views.index, name='index'),
    url(r'^text101/$', views.text101, name='text101'),
)
