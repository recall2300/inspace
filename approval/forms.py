from django import forms
from django.forms import ModelForm, Textarea
from .models import Approval, Employee


# http://ngee.tistory.com/816
# Documents : https://docs.djangoproject.com/en/1.10/ref/forms/widgets/#django.forms.TextInput

class ApprovalForm(forms.ModelForm):
    class Meta:
        model = Approval
        fields = (
            'start_date', 'end_date', 'leave_day',
            'approval_line_id',

            'username', 'department', 'position',

            'leave_classification', 'emergency_contact', 'destination', 'reason',

            'write_date',
            'state_code',
            'employee'
        )

        widgets = {
            'start_date': forms.TextInput(
                attrs={'placeholder': "시작일을 선택해주세요", 'class': 'calendar-init-date', 'required': 'True'}),
            'end_date': forms.TextInput(
                attrs={'placeholder': "마감일을 선택해주세요", 'class': "calendar-init-date", 'required': 'True'}),
            'leave_day': forms.TextInput(attrs={'readonly': True}),
            'approval_line_id': forms.HiddenInput(),

            'username': forms.HiddenInput(),
            'department': forms.HiddenInput(),
            'position': forms.HiddenInput(),

            'leave_classification': forms.Select(attrs={'class': 'ui fluid dropdown', 'required': True}),
            'emergency_contact': forms.TextInput(
                attrs={'placeholder': "숫자만 입력해주세요", 'pattern': "(\d{3}).*(\d{3}).*(\d{4})"}),
            'destination': forms.TextInput(attrs={}),
            'reason': Textarea(attrs={}),

            'write_date': forms.HiddenInput(),
            'state_code': forms.HiddenInput(),

        }

        labels = {
            'start_date': '시작일',
            'end_date': '마감일',
            'leave_day': '사용일수',
            'approval_line_id': '결재라인 id',

            'username': '',
            'department': '',
            'position': '',

            'leave_classification': '휴가구분',
            'emergency_contact': '긴급연락처',
            'destination': '목적지',
            'reason': '사유',

            'write_date': '',
            'state_code': '',

        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            'email', 'image', 'nickname', 'gender', 'username', 'department', 'position',
            'available_leave_day', 'contact', 'signature_image')
        widgets = {
            'email': forms.TextInput(attrs={'readonly': True}),
            'image': forms.FileInput(),
            'gender': forms.Select(attrs={}),
            'available_leave_day': forms.TextInput(attrs={'readonly': True}),
        }
        labels = {
            'email': '이메일',
            'image': '이미지',
            'nickname': '별명',
            'gender': '성별',
            'username': '이름',
            'department': '부서',
            'position': '직위',
            'available_leave_day': '연가',
            'contact': '연락처',
            'signature_image': '서명이미지'
        }
