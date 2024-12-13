from django.contrib import admin
from django.urls import path
from django.utils.html import format_html

from . admin_views import create_course_websites
from . models import *


@admin.register(WebPathCdsCod)
class WebPathCdsCodAdmin(admin.ModelAdmin):
    list_display = ('webpath', 'cds_cod', 'webpath_status')
    list_filter = ('webpath__is_active',)
    search_fields = ('webpath__name' ,'webpath__fullpath', 'cds_cod')
    raw_id_fields = ('webpath',)

    change_list_template = "admin/admin_changelist_custom.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("create-course-websites/",
                 self.admin_site.admin_view(create_course_websites),
                 name="unicms_unical_storage_handler_create_course_websites"),
        ]
        return custom_urls + urls

    def webpath_status(self, obj):
        if obj.webpath.is_active:
            return format_html('<img src="/static/admin/img/icon-yes.svg" alt="True">')
        return format_html('<img src="/static/admin/img/icon-no.svg" alt="False">')
    webpath_status.admin_order_field  = 'webpath__is_active'


@admin.register(CdsWebsiteHomeBlocks)
class CdsWebsiteHomeBlocksAdmin(admin.ModelAdmin):
    list_display = ('block', 'section', 'order', 'is_active')
    list_filter = ('is_active', 'section')
    search_fields = ('block__name' ,'section')
    list_editable = ('order', 'is_active',)
    raw_id_fields = ('block',)
