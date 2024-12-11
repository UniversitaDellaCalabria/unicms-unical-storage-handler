from django.contrib import admin
from django.utils.html import format_html

from . models import *


@admin.register(WebPathCdsCod)
class WebPathCdsCodAdmin(admin.ModelAdmin):
    list_display = ('webpath', 'cds_cod', 'webpath_status')
    list_filter = ('webpath__is_active',)
    search_fields = ('webpath', 'cds_cod')
    raw_id_fields = ('webpath',)

    def webpath_status(self, obj):
        if obj.webpath.is_active:
            return format_html('<img src="/static/admin/img/icon-yes.svg" alt="True">')
        return format_html('<img src="/static/admin/img/icon-no.svg" alt="False">')
    webpath_status.admin_order_field  = 'webpath__is_active'



