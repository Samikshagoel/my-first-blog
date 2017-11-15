from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

app_name = 'blogg'

urlpatterns = [
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^$', views.post_list, name = 'post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name = 'post_detail'),
	url(r'^post/new/$', views.post_new, name = 'post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
]