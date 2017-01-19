from django import forms
from django.forms import ModelForm, Textarea
from .models import Approval


# class ApprovalForm(forms.Form):
#     username = forms.CharField()
# username = forms.CharField()
# username = forms.CharField()
# username = forms.CharField()
#
# department = models.CharField(max_length=10)
# position = models.CharField(max_length=10)
# # username = models.ForeignKey(settings.AUTH_USER_MODEL)
# username = models.CharField(max_length=10)
# reason = models.TextField()
# start_date = models.DateTimeField(default=timezone.now)
# end_date = models.DateTimeField(default=timezone.now)
# write_date = models.DateTimeField(default=timezone.now)
# LEAVE_CLASSIFICATION_CHOICES = (
#     ('연차', '연차'),
#     ('오전반차', '오전반차'),
#     ('오후반차', '오후반차'),
#     ('병가', '병가'),
#     ('경조사휴가', '경조사휴가'),
#     ('산전후휴가', '산전후휴가'),
#     ('기타', '기타')
# )
# leave_classification = models.CharField(max_length=5, choices=LEAVE_CLASSIFICATION_CHOICES, default='연차')
# emergency_contact = models.CharField(max_length=11)
# destination = models.CharField(max_length=30)
# comments = models.PositiveSmallIntegerField(default=0, null=True)

# http://ngee.tistory.com/816
class ApprovalForm(forms.ModelForm):
    class Meta:
        model = Approval
        fields = (
            'username', 'department', 'position', 'reason', 'start_date', 'end_date', 'leave_classification',
            'emergency_contact', 'destination')
        # Documents : https://docs.djangoproject.com/en/1.10/ref/forms/widgets/#django.forms.TextInput
        widgets = {
            'username': forms.HiddenInput(),
            'department': forms.HiddenInput(),
            'position': forms.HiddenInput(),
            'reason': Textarea(attrs={}),
            'start_date': forms.SelectDateWidget(attrs={}),
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
        # department = models.CharField(max_length=10)
        # position = models.CharField(max_length=10)
        # # username = models.ForeignKey(settings.AUTH_USER_MODEL)
        # username = models.CharField(max_length=10)
        # reason = models.TextField()
        # start_date = models.DateTimeField(default=timezone.now)
        # end_date = models.DateTimeField(default=timezone.now)
        # write_date = models.DateTimeField(default=timezone.now)
        # LEAVE_CLASSIFICATION_CHOICES = (
        #     ('연차', '연차'),
        #     ('오전반차', '오전반차'),
        #     ('오후반차', '오후반차'),
        #     ('병가', '병가'),
        #     ('경조사휴가', '경조사휴가'),
        #     ('산전후휴가', '산전후휴가'),
        #     ('기타', '기타')
        # )
        # leave_classification = models.CharField(max_length=5, choices=LEAVE_CLASSIFICATION_CHOICES, default='연차')
        # emergency_contact = models.CharField(max_length=11)
        # destination = models.CharField(max_length=30)
        # comments = models.PositiveSmallIntegerField(default=0, null=True)
