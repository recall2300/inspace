from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from approval.serializers import UserSerializer, GroupSerializer
from .models import Approval
from django.shortcuts import render


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def approval_list(request):
    approvals = Approval.objects.all()
    return render(request, "approval/approval_list.html", {'approvals':approvals})

def approval_detail(request):
    return

def approval_new(request):
    return

def approval_edit(request):
    return