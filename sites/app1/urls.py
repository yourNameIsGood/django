from django.conf.urls.defaults import *
from app1.views import archive

urlpatterns = patterns('',
    url(r'^$',archive),
)
