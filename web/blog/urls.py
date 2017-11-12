from django.conf.urls import url

from . import views

# app_name='blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    # url(r'^login/$', 'django.contrib.auth.views.login', name='login', kwargs={'template_name':'/blog/login.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^doregister/$', views.reguser, name='reguser'),
    url(r'^write/$', views.write, name='write'),
    url(r'^regpost/$', views.regpost, name='regpost'),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.viewPost, name='viewPost'),
]