from rest_framework import viewsets
from django.contrib.auth import logout
from approval.serializers import *
from .models import Approval, Employee, Comment
from django.shortcuts import render, redirect


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

# class ApprovalViewSet(GenericAPIView, mixins.ListModelMixin):
#     queryset = Approval.objects.all()
#     serializer_class = ApprovalSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

class ApprovalViewSet(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

def approval_list(request):
    if request.user.is_authenticated:
        approvals = Approval.objects.all()
        return render(request, "approval/approval_list.html", {'approvals': approvals})
    else:
        return redirect('login')

def approval_logout(request):
    logout(request)
    return redirect('login')

def approval_detail(request):
    return

def approval_new(request):
    if request.method == "POST":
        form = Post
    return

def approval_edit(request):
    return