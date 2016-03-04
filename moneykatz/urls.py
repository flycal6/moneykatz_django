from django.conf.urls import patterns, url
from moneykatz import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^list/$', views.cat_list, name='cat_list'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_file/$', views.add_file, name='add_file'),
    url(r'^resume/$', views.resume, name='resume'),
    url(r'^jacqueline-thomas-resume/$', views.jresume, name='jackie-thomas'),
    url(r'^like_category/$', views.like_category, name='like_category'),
)
