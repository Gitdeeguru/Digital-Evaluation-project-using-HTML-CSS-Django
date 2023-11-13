from django.contrib import admin

from staff.models import Staff

class StaffAdmin(admin.ModelAdmin):
    list_display=('staff_name','staff_id','staff_branch','staff_gender','staff_password')

admin.site.register(Staff,StaffAdmin)
# Register your models here.
