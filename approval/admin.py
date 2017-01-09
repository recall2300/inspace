from django.contrib import admin
from .models import *

"""
어드민 페이지에서 데이터를 조작할 수 있게 모델을 추가합니다
"""
admin.site.register(Approval)
admin.site.register(Comment)
admin.site.register(Employee)