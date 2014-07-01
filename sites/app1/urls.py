from django.conf.urls.defaults import *
from app1.views import archive

urlpatterns = patterns('',
    url(r'^$',archive),
    url(r'^404$',show_404),
)
