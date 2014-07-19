from django.conf.urls import patterns, url
from django.conf.urls import include

urlpatterns = patterns('',
    url(r'^', include('snippets.urls')),
    url(r'^$', 'api_root'),
)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)