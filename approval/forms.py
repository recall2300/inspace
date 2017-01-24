from django import forms
from django.forms import ModelForm, Textarea
from .models import Approval, Employee


# http://ngee.tistory.com/816
# Documents : https://docs.djangoproject.com/en/1.10/ref/forms/widgets/#django.forms.TextInput
class ApprovalForm(forms.ModelForm):
    class Meta:
        model = Approval
        fields = (
            'username', 'department', 'position', 'reason', 'start_date', 'end_date', 'leave_classification',
            'emergency_contact', 'destination')

        widgets = {
            'username': forms.HiddenInput(),
            'department': forms.HiddenInput(),
            'position': forms.HiddenInput(),
            'reason': Textarea(attrs={}),
            'start_date': forms.SelectDateWidget(),
            'end_date': forms.SelectDateWidget(attrs={}),
            'leave_classification': forms.Select(attrs={}),
            'emergency_contact': forms.TextInput(attrs={}),
            'destination': forms.TextInput(attrs={})

        }

    labels = {
        'username': '이름',
        'department': '부서',
        'position': '직위',
        'reason': '사유',
        'start_date': '시작일',
        'end_date': '마감일',
        'leave_classification': '휴가구분',
        'emergency_contact': '긴급연락처',
        'destination': '목적지'

    }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            'email', 'image', 'nickname', 'gender', 'username', 'department', 'position',
            'available_leave_day', 'contact', 'signature_image')
        widgets = {
            'email': forms.TextInput(attrs={'readonly': True}),
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
