from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

# app_name='blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^doregister/$', views.reguser, name='reguser'),
    url(r'^write/$', views.write, name='write'),
    url(r'^regpost/$', views.regpost, name='regpost'),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.viewPost, name='viewPost'),
    url(r'^search/$', views.search, name='search'),
    url(r'^mypage/$', views.mypage, name='mypage'),


    # url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),  # 로그아웃 후 홈으로 이동
    # url(r'^login/$', auth_views.login, {'template_name':'blog/login.html'}, name='login'),
]