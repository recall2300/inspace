from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import View
from rest_framework import viewsets

from approval.forms import ApprovalForm
from approval.serializers import *
from .models import Approval, Employee, Comment


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


#
# class MyView(View):
#     def get(self, request):
#         # 뷰 로직 작성
#         return HttpResponse('result')

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

        return render(request, self.template_name, {'form': form})


# class ApprovalCreateView(FormView):
#     success_url = '/'
#     template_name = 'approval_form.html'
#     form_class = ApprovalForm
#
#     def from_valid(self, form):
#         form_save = form.save()
#         print(form_save.__dict__)
#
#         messages.info(self.request, "successfully added")
#         return super(ApprovalCreateView, self).form_valid(form)


# class ApprovalCreateView(CreateView):
#     model = Approval
#
#     def form_valid(self, form):
#         self.object = form.save()
#         return render(self.request, 'approval/approval_create_success.html', {'approvals': self.object})


def approval_list(request):
    if request.user.is_authenticated:
        approvals = Approval.objects.all()
        return render(request, "approval/approval_list.html", {'approvals': approvals})
    else:
        return redirect('login')


def approval_detail(request):
    return


def approval_edit(request):
    return


@login_required(login_url='/login/')
def home(request):
    if request.user.is_authenticated:
        approvals = Approval.objects.all()
        return render(request, "approval/approval_list.html", {'approvals': approvals})
    '''
    print(request)
    userdata = {
        'username': request.user.username,
        'email': request.user.email,
        'department': request.user.department,
        'contact': request.user.contact,
        'position': request.user.position,
        'image' : request.user.image,
        'gender' : request.user.gender,
        'nickname' : request.user.nickname
    }
    return render(request, 'approval_list.html', userdata)
    '''
