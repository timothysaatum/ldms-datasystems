from django.contrib import admin
from .models import Lab, Test, TestResultsPdf, Department




class LabAdmin(admin.ModelAdmin):
    list_display = ('lab_name', 'digital_address', 'region_of_location', 'telephone', 'email_address')



class TestResultsPdfAdmin(admin.ModelAdmin):
	list_display = ('submitted_on', 'laboratory', 'send_by', 'test', 'upload_pdf')




class TestAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'test_name', 'price',
     'discount', 'percentage_discount')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'laboratory', 'department_head', 'contact', 'email_address')

admin.site.register(Lab, LabAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(TestResultsPdf, TestResultsPdfAdmin)
admin.site.register(Department, DepartmentAdmin)