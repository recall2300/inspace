from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View, CreateView, UpdateView
from rest_framework import viewsets
from approval.forms import ApprovalForm, EmployeeForm
from approval.serializers import *
from .models import Approval, Employee, Comment, ApprovalLine
from social_django.models import UserSocialAuth
from django.db.models import Max
import os

USER_FIELDS = ['username', 'email']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_DIR = os.path.join(BASE_DIR, 'static', 'images', 'profiles')


class ApprovalViewSet(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ApprovalCreateView(View):
    form_class = ApprovalForm
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        initial = {'username': user.username,
                   'department': user.department,
                   'position': user.position,
                   'employee': user}
        form = self.form_class(initial=initial)
        return render(request, self.template_name, {'form': form, 'user': request.user})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form, })


@login_required(login_url='/login/')
def home(request):
    profile_image_name = request.user.email.split('@')[0] + ".jpg"
    profile_image_dir = IMAGE_DIR + "/" + profile_image_name
    form_class = ApprovalForm
    user = request.user
    initial = {'username': user.username,
               'department': user.department,
               'position': user.position,
               'employee': user}
    form = form_class(initial=initial)
    if request.user.is_authenticated:
        approvals = Approval.objects.all().order_by('-write_date')
        approval_lines = ApprovalLine.objects.all()
        total_approval_line = approval_lines.aggregate(Max('line_id'))['line_id__max']
        approval_lines_dict = {}

        if total_approval_line is not None:
            for i in range(1, total_approval_line + 1):
                approval_lines_dict[i] = {'description': None, 'approval_line': []}

            for line in approval_lines:
                select_line = approval_lines_dict[line.line_id]
                select_line['description'] = line.description
                select_line['approval_line'].append(line.employee.username)

        return render(request, "approval/main.html",
                      {'form': form, 'approvals': approvals, 'approval_lines_dict': approval_lines_dict})


class AccountView(View):
    template_name = 'registration/account.html'
    form_class = EmployeeForm

    def get(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(instance=user)
        try:
            google_login = user.social_auth.get(provider='google-oauth2')
        except UserSocialAuth.DoesNotExist:
            google_login = None
        can_disconnect = True  # (user.social_auth.count() > 1 or user.has_usable_password())
        return render(request, self.template_name,
                      {'form': form, 'user': user, 'google_login': google_login, 'can_disconnect': can_disconnect,
                       'google_uid': google_login.id})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})


class MyApprovalList(View):
    template_name = 'approval/mylist.html'
    form_class = ApprovalForm

    def get(self, request, *args, **kwargs):
        user = request.user
        initial = {'username': user.username,
                   'department': user.department,
                   'position': user.position}
        form = self.form_class(initial=initial)
        if request.user.is_authenticated:
            approvals = Approval.objects.all().order_by('-write_date')
            return render(request, self.template_name, {'form': form, 'approvals': approvals})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})


class Settings(View):
    template_name = 'approval/settings.html'
    form_class = ApprovalForm

    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        if request.user.is_authenticated:
            return render(request, self.template_name, {'employees': employees})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})


def new_approval_line(request):
    print("hi")
    request_line = dict(request.POST)
    description = request_line.get('description')[0]
    line_id = request_line.get('line_id')[0]
    employee_list = request_line.get('new-approval-line')
    depth = 1
    for employee in employee_list:
        ApprovalLine.objects.create(
            line_id=line_id,
            employee=Employee.objects.get(email=employee),
            depth=depth,
            description=description
        )
        depth += 1

    print('hi!')
    return render(request, "main.html")
