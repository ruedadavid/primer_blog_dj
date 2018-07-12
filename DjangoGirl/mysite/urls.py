from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),    
    #url(r'', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]