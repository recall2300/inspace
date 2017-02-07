from approval.models import EmployeePosition, EmployeeDepartment

EmployeePosition.objects.create(position="이사")
EmployeePosition.objects.create(position="부장")
EmployeePosition.objects.create(position="차장")
EmployeePosition.objects.create(position="과장")
EmployeePosition.objects.create(position="대리")
EmployeePosition.objects.create(position="사원")
EmployeePosition.objects.create(position="기타")
EmployeeDepartment.objects.create(id=1, parent_id=0, department_name="InSpace")
EmployeeDepartment.objects.create(id=2, parent_id=1, department_name="경지부")
EmployeeDepartment.objects.create(id=3, parent_id=1, department_name="개발부")