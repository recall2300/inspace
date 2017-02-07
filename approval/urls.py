from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^approval/new/$', views.ApprovalCreateView.as_view(), name='approval_new'),
    url(r'^approval/my/$', views.MyApprovalList.as_view(), name='approval_my'),
    url(r'^approval-line/new/$', views.new_approval_line, name='approval_line_new'),
    url(r'^settings/$', views.Settings.as_view(), name='settings'),
]
