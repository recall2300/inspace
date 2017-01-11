from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
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
    if request.user.is_authenticated:
        approvals = Approval.objects.all()
        return render(request, "approval/approval_list.html", {'approvals': approvals})
    else:
        return redirect('approval_login')


def approval_login(request):
    if request.user.is_authenticated:
        return redirect('approval_list')
    else:
        return render(request, "approval/approval_login.html")

def approval_login_do(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('approval_list')
    else:
        # Return an 'invalid login' error message.
        return redirect('approval_login')

def approval_logout(request):
    logout(request)
    return redirect('approval_login')

def approval_detail(request):
    return


def approval_new(request):
    return


def approval_edit(request):
    return
