from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.approval_list, name="approval_list"),
    url(r'^login$', views.approval_login, name="approval_login"),
    url(r'^login_do$', views.approval_login_do, name="approval_login_do"),
    url(r'^logout$', views.approval_logout, name="approval_logout"),
    url(r'^approval/(?P<pk>[0-9]+)/$', views.approval_detail, name="approval_detail"),
    url(r'^approval/new/$', views.approval_new, name='approval_new'),
    url(r'^approval/(?P<pk>[0-9]+)/edit/$', views.approval_edit, name='approval_edit'),
]