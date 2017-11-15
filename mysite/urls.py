from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^login/$', auth_views.login, name='login'),
    #url(r'^login/$', auth_views.login, {'next_page': '/profile'}, name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'blogg:profile'}, name='logout'),
]
