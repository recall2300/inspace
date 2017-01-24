from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^approval/new/$', views.ApprovalCreateView.as_view(), name='approval_new'),
]
