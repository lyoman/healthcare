from django.contrib import admin
from . models import Approval

# Register your models here.
class ApprovalModelAdmin(admin.ModelAdmin):
    list_display 		= ["user","approvedby", "status", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user"]
    list_editable		= ["status"]
    list_filter			= ["updated", "timestamp", "approvedby"]
    search_fields		= ["status"]
    class Meta:
        model = Approval
        
admin.site.register(Approval, ApprovalModelAdmin)