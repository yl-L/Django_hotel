from django.conf.urls import include, url

from django.contrib import admin

from hotel.views import index,hotel_id
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'kcsj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



    url(r'^admin/', include(admin.site.urls)),
    url(r'^hotel/(\d+)', hotel_id),
    url(r'^$', index),
]


