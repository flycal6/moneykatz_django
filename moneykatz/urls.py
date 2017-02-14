from django.conf.urls import patterns, url
from moneykatz import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^index-old/$', views.index_old, name='index_old'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^file-server/$', views.cat_list, name='cat_list'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_file/$', views.add_file, name='add_file'),
    url(r'^brian-thomas-resume/$', views.resume, name='resume'),
    url(r'^jacqueline-thomas-resume/$', views.jresume, name='jackie-thomas'),
    url(r'^like_category/$', views.like_category, name='like_category'),
    url(r'^django-secret-key/$', views.blog, name='blog'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^fixit/$', views.fixit, name='fixit'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^for-sale/$', views.for_sale, name='for-sale'),
    url(r'^definitely-not-junk/$', views.sale, name='sale'),
    # url(r'^payments/$', views.payments, name='payments'),
    url(r'^privacy/$', views.privacy, name='privacy'),
    url(r'^cancelled/$', views.cancelled, name='cancelled'),
    url(r'^success/$', views.success, name='success'),
    url(r'^valentines/$', views.valentines, name='valentines'),
)
