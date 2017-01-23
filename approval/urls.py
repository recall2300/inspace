from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^approval/new/$', views.ApprovalCreateView.as_view(), name='approval_new'),
    # url(r'^approval/$', views.approval_list, name="approval_list"),
    # url(r'^approval/(?P<pk>[0-9]+)/$', views.approval_detail, name="approval_detail"),
    # url(r'^approval/(?P<pk>[0-9]+)/edit/$', views.approval_edit, name='approval_edit'),
]  #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
