from django.contrib import admin
from .models import *
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

"""
커스텀 유저모델을 사용하려면 다음의 정의를 내려줘야 합니다.
"""


class UserCreationForm(forms.ModelForm):
    """ 필수필드로 정의한 필드와 패스워드 필드를 적어줘야합니다."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Mata:
        model = Employee
        fields = ('email', 'username', 'department', 'position', 'contact')

    def clean_password2(self):
        """ 두 패스워드를 비교하는 함수"""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Employee
        fields = ('email', 'password', 'username', 'gender', 'nickname', 'image', 'department', 'position', 'contact',
                  'is_active', 'is_admin')

    def clean_password(self):
        """사용자가 제공한것과 관계없이 초기값을 반환합니다"""
        return self.initial['password']


class UserAdmin(BaseUserAdmin):
    """이 폼은 유저를 새로 추가하거나 변경할때 쓰입니다."""
    form = UserChangeForm
    add_form = UserCreationForm
    # User모델을 표시할 때 사용하는 필드
    # 기본 UserAdmin의 정의를 덮어쓰며, auth.User의 특정 필드를 참조합니다.
    list_display = ('email', 'username', 'gender', 'nickname', 'image', 'department', 'position', 'contact', 'is_admin')
    list_filter = ('department', 'position', 'is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'department', 'position', 'contact')}),
        ('Permissions', {'fields': ('is_admin', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1',
                       'password2', 'department', 'position', 'contact', 'is_active', 'is_admin',)}
         ),
    )
    search_fields = ('email', 'username', 'department', 'position', 'contact',)
    ordering = ('email', 'username', 'department', 'position', 'contact',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(Employee, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)

"""
어드민 페이지에서 데이터를 조작할 수 있게 모델을 추가합니다.
"""

admin.site.register(EmployeeDepartment)
admin.site.register(Approval)
admin.site.register(Comment)
admin.site.register(ApprovalLine)
admin.site.register(ApprovalState)