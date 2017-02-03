from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View, CreateView
from rest_framework import viewsets
from approval.forms import ApprovalForm, EmployeeForm
from approval.serializers import *
from .models import Approval, Employee, Comment, ApprovalLine
from social_django.models import UserSocialAuth
from django.db.models import Max


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
    template_name = 'approval_form.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        initial = {'username': user.username,
                   'department': user.department,
                   'position': user.position}
        form = self.form_class(initial=initial)
        return render(request, self.template_name, {'form': form, 'user': request.user})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form, })


def approval_detail(request):
    return


def approval_edit(request):
    return


@login_required(login_url='/login/')
def home(request):
    form_class = ApprovalForm
    user = request.user
    initial = {'username': user.username,
               'department': user.department,
               'position': user.position}
    form = form_class(initial=initial)
    if request.user.is_authenticated:
        approvals = Approval.objects.all().order_by('-write_date')
        approval_line = ApprovalLine.objects.all()
        # line_id_max = approval_line.aggregate(Max('line_id'))['line_id__max']
        approval_line_dict = {}
        # for line_id in range(line_id_max):
        #     approval_line_dict[line_id + 1] = {'description': None, 'approval_line': []}

        # for row in approval_line:
        #     select_line = approval_line_dict[row.line_id]
        #     select_line['description'] = row.description
        #     select_line['approval_line'].append(row.employee.username)

        # for line in approval_line:
        #     approval_line_list[line.line_id].append(line.employee)

        print(approval_line_dict)

        employee = Employee.objects.all()
        return render(request, "approval/main.html",
                      {'form': form, 'approvals': approvals, 'approval_line_dict': approval_line_dict,
                       'employee': employee})


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


def testpage(request):
    return render(request, 'testpage.html')


def new_approval_line(request):
    return
