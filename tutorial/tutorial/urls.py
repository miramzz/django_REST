from django.conf.urls import patterns, url
from snippets import views
from django.conf.urls import include

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
