from django.contrib import admin

# Register your models here.
from scriptofstd.models import Scriptofstd

class ScriptAdmin(admin.ModelAdmin):
    list_display=('script_usn','script_id','script_subject_code','script_progress','script_upload_datetime')

admin.site.register(Scriptofstd,ScriptAdmin)