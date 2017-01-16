from django import forms

from .models import Approval


class ApprovalForm(forms.ModelForm):
    class Meta:
        model = Approval
        fields = (
            'department', 'position', "username", 'reason', 'start_date', 'end_date', 'write_date',
            'leave_classification',
            'emergency_contact', 'destination', 'comments')
