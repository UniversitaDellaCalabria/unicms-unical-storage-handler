from django.contrib import admin
from django.utils.html import format_html

from . models import *


@admin.register(WebPathCdsCod)
class WebPathCdsCodAdmin(admin.ModelAdmin):
    list_display = ('webpath', 'cds_cod', 'webpath_status')
    list_filter = ('webpath__is_active',)
    search_fields = ('webpath__name' ,'webpath__fullpath', 'cds_cod')
    raw_id_fields = ('webpath',)

    def webpath_status(self, obj):
        if obj.webpath.is_active:
            return format_html('<img src="/static/admin/img/icon-yes.svg" alt="True">')
        return format_html('<img src="/static/admin/img/icon-no.svg" alt="False">')
    webpath_status.admin_order_field  = 'webpath__is_active'


@admin.register(CdsWebsiteHomeBlocks)
class CdsWebsiteHomeBlocksAdmin(admin.ModelAdmin):
    list_display = ('block', 'section', 'order', 'is_active')
    list_filter = ('section', 'is_active')
    search_fields = ('block' ,'section')
    list_editable = ('order', 'is_active',)
    raw_id_fields = ('block',)
