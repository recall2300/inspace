from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'', include('django.contrib.auth.urls')),
    url(r'^$', views.home),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    #url(r'^$', views.approval_list, name="approval_list"),
    #url(r'^approval/(?P<pk>[0-9]+)/$', views.approval_detail, name="approval_detail"),
    #url(r'^approval/new/$', views.approval_new, name='approval_new'),
    #url(r'^approval/(?P<pk>[0-9]+)/edit/$', views.approval_edit, name='approval_edit'),
]
