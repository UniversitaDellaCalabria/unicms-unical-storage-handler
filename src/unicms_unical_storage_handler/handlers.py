import urllib

from django.conf import settings
from django.http import (HttpResponse,
                         Http404)
from django.template import Template, Context
from django.utils.translation import gettext_lazy as _

from cms.contexts.handlers import BaseContentHandler
from cms.contexts.models import WebPath
from cms.contexts.utils import contextualize_template, sanitize_path
from cms.pages.models import Page

from . settings import *


# settings params
ALLOWED_ADDRESSBOOK_ROLES = getattr(settings, 'ALLOWED_ADDRESSBOOK_ROLES',
                                    ALLOWED_ADDRESSBOOK_ROLES)
ALLOWED_ADDRESSBOOK_STRUCTURE_ID = getattr(settings, 'ALLOWED_ADDRESSBOOK_STRUCTURE_ID',
                                           ALLOWED_ADDRESSBOOK_STRUCTURE_ID)
ALLOWED_ADDRESSBOOK_STRUCTURE_TYPES = getattr(settings, 'ALLOWED_ADDRESSBOOK_STRUCTURE_TYPES',
                                              ALLOWED_ADDRESSBOOK_STRUCTURE_TYPES)

ALLOWED_UNICMS_SITES = getattr(settings, 'ALLOWED_UNICMS_SITES',
                               ALLOWED_UNICMS_SITES)

ALLOWED_CDS_COURSETYPES = getattr(settings, 'ALLOWED_CDS_COURSETYPES',
                                  ALLOWED_CDS_COURSETYPES)

INITIAL_STRUCTURE_FATHER = getattr(settings, 'INITIAL_STRUCTURE_FATHER',
                                  INITIAL_STRUCTURE_FATHER)
# end settings params

class BaseStorageHandler(BaseContentHandler):
    template = "storage_base.html"

    def __init__(self, **kwargs):
        super(BaseStorageHandler, self).__init__(**kwargs)
        self.lang = self.request.LANGUAGE_CODE
        self.match_dict = self.match.groupdict()
        self.webpath = WebPath.objects.filter(site=self.website,
                                              parent=None,
                                              is_active=True)\
                                      .first()
        if self.webpath.site.pk not in settings.ALLOWED_UNICMS_SITES:
            raise Http404('Website not allowed to show this webpath')

        # only home page of allowed websites
        if not self.webpath or self.match_dict.get('webpath', '/') != self.webpath.fullpath: # pragma: no cover
            raise Http404('Unknown WebPath')

        self.page = Page.objects.filter(is_active=True,
                                        webpath=self.webpath).first()
        self.data = {'request': self.request,
                     'webpath': self.webpath,
                     'website': self.website,
                     'page': self.page,
                     'path': self.match_dict.get('webpath', '/'),
                     'handler': self
        }

    def as_view(self):
        ext_template_sources = contextualize_template(self.template,
                                                      self.page)
        template = Template(ext_template_sources)
        context = Context(self.data)
        return HttpResponse(template.render(context), status=200)

    @property
    def get_base_url(self):
        url = f'{self.webpath.get_full_path()}/{settings.CMS_STORAGE_BASE_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        leaf = ('#', settings.CMS_STORAGE_ROOT_LABEL)
        return (leaf,)


class CdSListViewHandler(BaseStorageHandler):
    template = "storage_cdslist.html"

    def as_view(self):

        data = {'lang': self.lang}

        if ALLOWED_CDS_COURSETYPES:
            data['coursetype'] = ",".join(ALLOWED_CDS_COURSETYPES)

        params = urllib.parse.urlencode(data)
        self.data['url'] = f'{settings.CMS_STORAGE_CDS_API}?{params}'

        return super().as_view()

    @property
    def breadcrumbs(self):
        # leaf = (self.pub_context.url, getattr(self.pub_context.publication, 'title'))
        leaf = ('#', settings.CMS_STORAGE_CDS_LIST_LABEL)
        parent = (self.get_base_url, settings.CMS_STORAGE_ROOT_LABEL)
        return (parent, leaf)


class CdSInfoViewHandler(BaseStorageHandler):
    template = "storage_cdsinfo.html"

    def __init__(self, **kwargs):
        super(CdSInfoViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{settings.CMS_STORAGE_CDS_API}{self.code}/?lang={self.lang}'
        return super().as_view()

    @property
    def parent_url(self):
        url = f'{self.webpath.get_full_path()}/{settings.CMS_STORAGE_BASE_PATH}/{settings.CMS_STORAGE_CDS_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        # leaf = (self.pub_context.url, getattr(self.pub_context.publication, 'title'))
        root = (self.get_base_url, settings.CMS_STORAGE_ROOT_LABEL)
        parent = (self.parent_url, settings.CMS_STORAGE_CDS_LIST_LABEL)
        leaf = ('#', self.code)
        return (root, parent, leaf)


class ActivityViewHandler(BaseStorageHandler):
    template = "storage_activity.html"

    def __init__(self, **kwargs):
        super(ActivityViewHandler, self).__init__(**kwargs)
        self.cdsid = self.match_dict.get('cdsid', '')
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{settings.CMS_STORAGE_ACTIVITY_API}{self.code}/?lang={self.lang}'
        return super().as_view()

    @property
    def cdslist_url(self):
        url = f'{self.webpath.get_full_path()}/{settings.CMS_STORAGE_BASE_PATH}/{settings.CMS_STORAGE_CDS_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def cdsid_url(self):
        url = f'{self.webpath.get_full_path()}/{settings.CMS_STORAGE_BASE_PATH}/{settings.CMS_STORAGE_CDS_VIEW_PREFIX_PATH}/{self.cdsid}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, settings.CMS_STORAGE_ROOT_LABEL)
        cdslist = (self.cdslist_url, settings.CMS_STORAGE_CDS_LIST_LABEL)
        cdsid = (self.cdsid_url, self.cdsid)
        activities = (self.cdsid_url, settings.CMS_STORAGE_ACTIVITIES_LABEL)
        leaf = ('#', self.code)
        return (root, cdslist, cdsid, activities, leaf)


class TeacherListViewHandler(BaseStorageHandler):
    template = "storage_teachers_list.html"

    def __init__(self, **kwargs):
        super(TeacherListViewHandler, self).__init__(**kwargs)

    def as_view(self):
        self.data['url'] = f'{settings.CMS_STORAGE_TEACHER_API}?lang={self.lang}'
        return super().as_view()

    # @property
    # def parent_url(self):
        # url = f'{self.webpath.get_full_path()}/{settings.CMS_STORAGE_BASE_PATH}/{settings.CMS_STORAGE_CDS_VIEW_PREFIX_PATH}/'
        # return sanitize_path(url)

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, settings.CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', settings.CMS_STORAGE_TEACHERS_LABEL)
        return (root, leaf)


class TeacherInfoViewHandler(BaseStorageHandler):
    template = "storage_teachers_info.html"

    def __init__(self, **kwargs):
        super(TeacherInfoViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{settings.CMS_STORAGE_TEACHER_API}{self.code}/?lang={self.lang}'
        return super().as_view()

    @property
    def parent_url(self):
        url = f'{self.webpath.get_full_path()}/{settings.CMS_STORAGE_BASE_PATH}/{settings.CMS_STORAGE_THEACHER_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, settings.CMS_STORAGE_ROOT_LABEL)
        parent = (self.parent_url, settings.CMS_STORAGE_TEACHERS_LABEL)
        leaf = ('#', self.code)
        return (root, parent, leaf)


class AddressbookListViewHandler(BaseStorageHandler):
    template = "storage_addressbook_list.html"

    def __init__(self, **kwargs):
        super(AddressbookListViewHandler, self).__init__(**kwargs)

    def as_view(self):

        data = {'lang': self.lang}

        if ALLOWED_ADDRESSBOOK_ROLES:
            data['roles'] = ",".join(ALLOWED_ADDRESSBOOK_ROLES)
        if ALLOWED_ADDRESSBOOK_STRUCTURE_ID:
            data['structureid'] = ",".join(ALLOWED_ADDRESSBOOK_STRUCTURE_ID)
        if ALLOWED_ADDRESSBOOK_STRUCTURE_TYPES:
            data['structuretypes'] = ",".join(ALLOWED_ADDRESSBOOK_STRUCTURE_TYPES)

        params = urllib.parse.urlencode(data)

        self.data['url'] = f'{settings.CMS_STORAGE_ADDRESSBOOK_API}?{params}'
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, settings.CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', settings.CMS_STORAGE_ADDRESSBOOK_LABEL)
        return (root, leaf)


class AddressbookInfoViewHandler(BaseStorageHandler):
    template = "storage_addressbook_info.html"

    def __init__(self, **kwargs):
        super(AddressbookInfoViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{settings.CMS_STORAGE_ADDRESSBOOK_API}{self.code}/?lang={self.lang}'
        print(self.data['url'])
        return super().as_view()

    @property
    def parent_url(self):
        url = f'{self.webpath.get_full_path()}/{settings.CMS_STORAGE_BASE_PATH}/{settings.CMS_STORAGE_ADDRESSBOOK_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, settings.CMS_STORAGE_ROOT_LABEL)
        parent = (self.parent_url, settings.CMS_STORAGE_ADDRESSBOOK_LABEL)
        leaf = ('#', self.code)
        return (root, parent, leaf)


class StructureListViewHandler(BaseStorageHandler):
    template = "storage_structure_list.html"

    def __init__(self, **kwargs):
        super(StructureListViewHandler, self).__init__(**kwargs)

    def as_view(self):
        data = {'lang': self.lang}

        if INITIAL_STRUCTURE_FATHER != '':
            data['father'] = INITIAL_STRUCTURE_FATHER

        params = urllib.parse.urlencode(data)
        self.data['url'] = f'{settings.CMS_STORAGE_STRUCTURE_API}?{params}'
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, settings.CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', settings.CMS_STORAGE_STRUCTURE_LABEL)
        return (root, leaf)


class StructureInfoViewHandler(BaseStorageHandler):
    template = "storage_structure_info.html"

    def __init__(self, **kwargs):
        super(StructureInfoViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{settings.CMS_STORAGE_STRUCTURE_API}{self.code}/?lang={self.lang}'
        self.data['url_child_structures'] = f'{settings.CMS_STORAGE_STRUCTURE_API}/?lang={self.lang}&father={self.code}'
        self.data['url_personnel'] = f'{settings.CMS_STORAGE_ADDRESSBOOK_API}/?lang={self.lang}&structuretree={self.code}'
        return super().as_view()

    @property
    def parent_url(self):
        url = f'{self.webpath.get_full_path()}/{settings.CMS_STORAGE_BASE_PATH}/{settings.CMS_STORAGE_STRUCTURE_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, settings.CMS_STORAGE_ROOT_LABEL)
        parent = (self.parent_url, settings.CMS_STORAGE_STRUCTURE_LABEL)
        leaf = ('#', self.code)
        return (root, parent, leaf)


class LaboratoryListViewHandler(BaseStorageHandler):
    template = "storage_laboratory_list.html"

    def __init__(self, **kwargs):
        super(LaboratoryListViewHandler, self).__init__(**kwargs)

    def as_view(self):
        self.data['url'] = f'{settings.CMS_STORAGE_LABORATORY_API}?lang={self.lang}'
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, settings.CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', settings.CMS_STORAGE_STRUCTURE_LABEL)
        return (root, leaf)


class LaboratoryInfoViewHandler(BaseStorageHandler):
    template = "storage_laboratory_info.html"

    def __init__(self, **kwargs):
        super(LaboratoryInfoViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{settings.CMS_STORAGE_LABORATORY_API}{self.code}/?lang={self.lang}'
        print(self.data['url'])
        return super().as_view()

    @property
    def parent_url(self):
        url = f'{self.webpath.get_full_path()}/{settings.CMS_STORAGE_BASE_PATH}/{settings.CMS_STORAGE_LABORATORY_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, settings.CMS_STORAGE_ROOT_LABEL)
        parent = (self.parent_url, settings.CMS_STORAGE_LABORATORY_LABEL)
        leaf = ('#', self.code)
        return (root, parent, leaf)
