from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView
from filebrowser.sites import site


class MyRegistrationView(RegistrationView):
    def get_success_url(self, user=None):
        return '/moneykatz/'


urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'moneykatz_django.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/filebrowser/', include(site.urls)),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^moneykatz/', include('moneykatz.urls')),
                       url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
                       url(r'^accounts/', include('registration.backends.simple.urls')),
                       )
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
