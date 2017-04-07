from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #admin/으로 시작하는 모든 url을 장고가 view와 대조해 찾아 낸다.
    url(r'', include('blog.urls')),   
]
