from django.contrib import admin
from .models import Hospital, Sample, Ward


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('hospital_name', 'digital_address', 'region_of_location', 'telephone',
     'email_address', 'created_by', 'created_on', 'website')


class WardAdmin(admin.ModelAdmin):
    list_display = ('ward_name', 'hospital', 'head_of_ward', 'contact', 'email_address')


class SampleAdmin(admin.ModelAdmin):
    list_display = ('ward', 'send_to', 'send_by', 'phone', 'sample_type', 'sample_tube', 
        'sample_id', 'sample_origin', 'sex_of_client', 'name_of_client', 'age_of_client', 
        'department', 'received_by', 'is_delivered')


admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Ward, WardAdmin)
admin.site.register(Sample, SampleAdmin)
