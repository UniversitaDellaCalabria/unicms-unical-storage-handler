import json
import logging
import requests
import urllib

from datetime import datetime, timezone

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import (HttpResponse,
                         HttpResponseRedirect,
                         Http404)
from django.middleware.csrf import get_token
from django.shortcuts import get_object_or_404, redirect
from django.template import Template, Context
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import get_token

from cms.contexts.handlers import BaseContentHandler
from cms.contexts.models import WebPath
from cms.contexts.utils import contextualize_template, sanitize_path
from cms.pages.models import Page

from . forms import CdsWebsiteContactForm, DynCdsWebsiteContactForm
from . settings import *


logger = logging.getLogger(__name__)


# local or global settings
CMS_STORAGE_BASE_API = getattr(settings, 'CMS_STORAGE_BASE_API', CMS_STORAGE_BASE_API)

ALLOWED_ADDRESSBOOK_ROLES = getattr(settings, 'ALLOWED_ADDRESSBOOK_ROLES', ALLOWED_ADDRESSBOOK_ROLES)
ALLOWED_ADDRESSBOOK_STRUCTURE_ID = getattr(settings, 'ALLOWED_ADDRESSBOOK_STRUCTURE_ID', ALLOWED_ADDRESSBOOK_STRUCTURE_ID)
ALLOWED_STRUCTURE_TYPES = getattr(settings, 'ALLOWED_STRUCTURE_TYPES', ALLOWED_STRUCTURE_TYPES)
ALLOWED_CDS_COURSETYPES = getattr(settings, 'ALLOWED_CDS_COURSETYPES', ALLOWED_CDS_COURSETYPES)
ALLOWED_TEACHER_ROLES = getattr(settings, 'ALLOWED_TEACHER_ROLES', ALLOWED_TEACHER_ROLES)
CMS_STORAGE_ACTIVITY_API = getattr(settings, 'CMS_STORAGE_ACTIVITY_API', CMS_STORAGE_ACTIVITY_API)
CMS_STORAGE_ACTIVITIES_LABEL = getattr(settings, 'CMS_STORAGE_ACTIVITIES_LABEL', CMS_STORAGE_ACTIVITIES_LABEL)
CMS_STORAGE_ADDRESSBOOK_API = getattr(settings, 'CMS_STORAGE_ADDRESSBOOK_API', CMS_STORAGE_ADDRESSBOOK_API)
CMS_STORAGE_ADDRESSBOOK_LABEL = getattr(settings, 'CMS_STORAGE_ADDRESSBOOK_LABEL', CMS_STORAGE_ADDRESSBOOK_LABEL)
CMS_STORAGE_ADDRESSBOOK_VIEW_PREFIX_PATH = getattr(settings, 'CMS_STORAGE_ADDRESSBOOK_VIEW_PREFIX_PATH', CMS_STORAGE_ADDRESSBOOK_VIEW_PREFIX_PATH)
CMS_STORAGE_APPLIED_RESEARCH_LINE_API = getattr(settings, 'CMS_STORAGE_APPLIED_RESEARCH_LINE_API', CMS_STORAGE_APPLIED_RESEARCH_LINE_API)
CMS_STORAGE_APPLIED_RESEARCH_LINE_LABEL = getattr(settings, 'CMS_STORAGE_APPLIED_RESEARCH_LINE_LABEL', CMS_STORAGE_APPLIED_RESEARCH_LINE_LABEL)
CMS_STORAGE_BASE_PATH = getattr(settings, 'CMS_STORAGE_BASE_PATH', CMS_STORAGE_BASE_PATH)
CMS_STORAGE_BASE_RESEARCH_LINE_API = getattr(settings, 'CMS_STORAGE_BASE_RESEARCH_LINE_API', CMS_STORAGE_BASE_RESEARCH_LINE_API)
CMS_STORAGE_BASE_RESEARCH_LINE_LABEL = getattr(settings, 'CMS_STORAGE_BASE_RESEARCH_LINE_LABEL', CMS_STORAGE_BASE_RESEARCH_LINE_LABEL)
CMS_STORAGE_CDS_API = getattr(settings, 'CMS_STORAGE_CDS_API', CMS_STORAGE_CDS_API)
CMS_STORAGE_CDS_LIST_LABEL = getattr(settings, 'CMS_STORAGE_CDS_LIST_LABEL', CMS_STORAGE_CDS_LIST_LABEL)
CMS_STORAGE_CDS_VIEW_PREFIX_PATH = getattr(settings, 'CMS_STORAGE_CDS_VIEW_PREFIX_PATH', CMS_STORAGE_CDS_VIEW_PREFIX_PATH)
CMS_STORAGE_HIGH_FORMATION_MASTERS_API = getattr(settings, 'CMS_STORAGE_HIGH_FORMATION_MASTERS_API', CMS_STORAGE_HIGH_FORMATION_MASTERS_API)
CMS_STORAGE_HIGH_FORMATION_MASTERS_LABEL = getattr(settings, 'CMS_STORAGE_HIGH_FORMATION_MASTERS_LABEL', CMS_STORAGE_HIGH_FORMATION_MASTERS_LABEL)
CMS_STORAGE_HIGH_FORMATION_MASTERS_VIEW_PREFIX_PATH = getattr(settings, 'CMS_STORAGE_HIGH_FORMATION_MASTERS_VIEW_PREFIX_PATH', CMS_STORAGE_HIGH_FORMATION_MASTERS_VIEW_PREFIX_PATH)
CMS_STORAGE_LABORATORY_API = getattr(settings, 'CMS_STORAGE_LABORATORY_API', CMS_STORAGE_LABORATORY_API)
CMS_STORAGE_LABORATORY_LABEL = getattr(settings, 'CMS_STORAGE_LABORATORY_LABEL', CMS_STORAGE_LABORATORY_LABEL)
CMS_STORAGE_LABORATORY_VIEW_PREFIX_PATH = getattr(settings, 'CMS_STORAGE_LABORATORY_VIEW_PREFIX_PATH', CMS_STORAGE_LABORATORY_VIEW_PREFIX_PATH)
CMS_STORAGE_PATENTS_API = getattr(settings, 'CMS_STORAGE_PATENTS_API', CMS_STORAGE_PATENTS_API)
CMS_STORAGE_PATENTS_LABEL = getattr(settings, 'CMS_STORAGE_PATENTS_LABEL', CMS_STORAGE_PATENTS_LABEL)
CMS_STORAGE_PHD_ACTIVITIES_API = getattr(settings, 'CMS_STORAGE_PHD_ACTIVITIES_API', CMS_STORAGE_PHD_ACTIVITIES_API)
CMS_STORAGE_PHD_ACTIVITIES_LABEL = getattr(settings, 'CMS_STORAGE_PHD_ACTIVITIES_LABEL', CMS_STORAGE_PHD_ACTIVITIES_LABEL)
CMS_STORAGE_PROJECTS_API = getattr(settings, 'CMS_STORAGE_PROJECTS_API', CMS_STORAGE_PROJECTS_API)
CMS_STORAGE_PROJECTS_LABEL = getattr(settings, 'CMS_STORAGE_PROJECTS_LABEL', CMS_STORAGE_PROJECTS_LABEL)
CMS_STORAGE_PROJECTS_VIEW_PREFIX_PATH = getattr(settings, 'CMS_STORAGE_PROJECTS_VIEW_PREFIX_PATH', CMS_STORAGE_PROJECTS_VIEW_PREFIX_PATH)
CMS_STORAGE_PUBLICATIONS_API = getattr(settings, 'CMS_STORAGE_PUBLICATIONS_API', CMS_STORAGE_PUBLICATIONS_API)
CMS_STORAGE_PUBLICATIONS_LABEL = getattr(settings, 'CMS_STORAGE_PUBLICATIONS_LABEL', CMS_STORAGE_PUBLICATIONS_LABEL)
CMS_STORAGE_PUBLICATIONS_VIEW_PREFIX_PATH = getattr(settings, 'CMS_STORAGE_PUBLICATIONS_VIEW_PREFIX_PATH', CMS_STORAGE_PUBLICATIONS_VIEW_PREFIX_PATH)
CMS_STORAGE_RESEARCH_GROUP_API = getattr(settings, 'CMS_STORAGE_RESEARCH_GROUP_API', CMS_STORAGE_RESEARCH_GROUP_API)
CMS_STORAGE_RESEARCH_GROUP_LABEL = getattr(settings, 'CMS_STORAGE_RESEARCH_GROUP_LABEL', CMS_STORAGE_RESEARCH_GROUP_LABEL)
CMS_STORAGE_RESEARCH_LINE_API = getattr(settings, 'CMS_STORAGE_RESEARCH_LINE_API', CMS_STORAGE_RESEARCH_LINE_API)
CMS_STORAGE_RESEARCH_LINE_LABEL = getattr(settings, 'CMS_STORAGE_RESEARCH_LINE_LABEL', CMS_STORAGE_RESEARCH_LINE_LABEL)
CMS_STORAGE_ROOT_LABEL = getattr(settings, 'CMS_STORAGE_ROOT_LABEL', CMS_STORAGE_ROOT_LABEL)
CMS_STORAGE_SPINOFF_API = getattr(settings, 'CMS_STORAGE_SPINOFF_API', CMS_STORAGE_SPINOFF_API)
CMS_STORAGE_SPINOFF_LABEL = getattr(settings, 'CMS_STORAGE_SPINOFF_LABEL', CMS_STORAGE_SPINOFF_LABEL)
CMS_STORAGE_SPINOFF_VIEW_PREFIX_PATH = getattr(settings, 'CMS_STORAGE_SPINOFF_VIEW_PREFIX_PATH', CMS_STORAGE_SPINOFF_VIEW_PREFIX_PATH)
CMS_STORAGE_STRUCTURE_API = getattr(settings, 'CMS_STORAGE_STRUCTURE_API', CMS_STORAGE_STRUCTURE_API)
CMS_STORAGE_STRUCTURE_LABEL = getattr(settings, 'CMS_STORAGE_STRUCTURE_LABEL', CMS_STORAGE_STRUCTURE_LABEL)
CMS_STORAGE_STRUCTURE_VIEW_PREFIX_PATH = getattr(settings, 'CMS_STORAGE_STRUCTURE_VIEW_PREFIX_PATH', CMS_STORAGE_STRUCTURE_VIEW_PREFIX_PATH)
CMS_STORAGE_TEACHER_API = getattr(settings, 'CMS_STORAGE_TEACHER_API', CMS_STORAGE_TEACHER_API)
CMS_STORAGE_TEACHERS_LABEL = getattr(settings, 'CMS_STORAGE_TEACHERS_LABEL', CMS_STORAGE_TEACHERS_LABEL)
CMS_STORAGE_TEACHER_VIEW_PREFIX_PATH = getattr(settings, 'CMS_STORAGE_TEACHER_VIEW_PREFIX_PATH', CMS_STORAGE_TEACHER_VIEW_PREFIX_PATH)
INITIAL_STRUCTURE_FATHER = getattr(settings, 'INITIAL_STRUCTURE_FATHER', INITIAL_STRUCTURE_FATHER)

CMS_WEBPATH_CDS = getattr(settings, 'CMS_WEBPATH_CDS', CMS_WEBPATH_CDS)
CMS_WEBPATH_CDS_OLD = getattr(settings, 'CMS_WEBPATH_CDS_OLD', CMS_WEBPATH_CDS_OLD)
CMS_WEBPATH_CDS_MORPH = getattr(settings, 'CMS_WEBPATH_CDS_MORPH', CMS_WEBPATH_CDS_MORPH)
CMS_WEBPATH_PROSPECT = getattr(settings, 'CMS_WEBPATH_PROSPECT', CMS_WEBPATH_PROSPECT)
CMS_WEBPATH_PROSPECT_DEFAULT = getattr(settings, 'CMS_WEBPATH_PROSPECT_DEFAULT', CMS_WEBPATH_PROSPECT_DEFAULT)
CMS_STORAGE_CDS_WEBSITES_CORSO_LABEL = getattr(settings, 'CMS_STORAGE_CDS_WEBSITES_CORSO_LABEL', CMS_STORAGE_CDS_WEBSITES_CORSO_LABEL)
CMS_STORAGE_CDS_WEBSITES_ISCRIVERSI_LABEL = getattr(settings, 'CMS_STORAGE_CDS_WEBSITES_ISCRIVERSI_LABEL', CMS_STORAGE_CDS_WEBSITES_ISCRIVERSI_LABEL)
CMS_STORAGE_CDS_WEBSITES_STUDIARE_LABEL = getattr(settings, 'CMS_STORAGE_CDS_WEBSITES_STUDIARE_LABEL', CMS_STORAGE_CDS_WEBSITES_STUDIARE_LABEL)
CMS_STORAGE_CDS_WEBSITES_OPPORTUNITA_LABEL = getattr(settings, 'CMS_STORAGE_CDS_WEBSITES_OPPORTUNITA_LABEL', CMS_STORAGE_CDS_WEBSITES_OPPORTUNITA_LABEL)
CMS_STORAGE_CDS_WEBSITES_ORGANIZZAZIONE_LABEL = getattr(settings, 'CMS_STORAGE_CDS_WEBSITES_ORGANIZZAZIONE_LABEL', CMS_STORAGE_CDS_WEBSITES_ORGANIZZAZIONE_LABEL)
CMS_STORAGE_CDS_WEBSITE_PROSPECT_EMAIL_RECIPIENTS = getattr(settings, 'CMS_STORAGE_CDS_WEBSITE_PROSPECT_EMAIL_RECIPIENTS', CMS_STORAGE_CDS_WEBSITE_PROSPECT_EMAIL_RECIPIENTS)

CURRENT_YEAR = getattr(settings, 'CURRENT_YEAR', CURRENT_YEAR)
CDS_WEBSITE_CURRENT_YEAR = getattr(settings, 'CDS_WEBSITE_CURRENT_YEAR', CDS_WEBSITE_CURRENT_YEAR)
CDS_WEBSITE_PROSPECT_CURRENT_YEAR = getattr(settings, 'CDS_WEBSITE_PROSPECT_CURRENT_YEAR', CDS_WEBSITE_PROSPECT_CURRENT_YEAR)
HIGH_FORMATION_YEAR = getattr(settings, 'HIGH_FORMATION_YEAR', HIGH_FORMATION_YEAR)


class BaseStorageHandler(BaseContentHandler):
    template = "storage_base.html"

    def __init__(self, **kwargs):
        super(BaseStorageHandler, self).__init__(**kwargs)
        self.match_dict = self.match.groupdict()
        self.webpath = WebPath.objects.filter(site=self.website,
                                              parent=None,
                                              is_active=True)\
                                      .first()
        allowed_sites = settings.ALLOWED_UNICMS_SITES

        if '*' not in allowed_sites and self.webpath.site.pk not in allowed_sites:
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
        url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_BASE_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        leaf = ('#', CMS_STORAGE_ROOT_LABEL)
        return (leaf,)


class CdSListViewHandler(BaseStorageHandler):
    template = "storage_cdslist.html"

    def as_view(self):

        # url_data = {}

        # if ALLOWED_CDS_COURSETYPES:
            # url_data['coursetype'] = ",".join(ALLOWED_CDS_COURSETYPES)
        # if CURRENT_YEAR:
            # url_data['academicyear'] = CURRENT_YEAR

        # params = urllib.parse.urlencode(url_data)
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_CDS_API}'
        # if params: self.data['url'] = f"{self.data['url']}?{params}"
        return super().as_view()

    @property
    def breadcrumbs(self):
        # leaf = (self.pub_context.url, getattr(self.pub_context.publication, 'title'))
        leaf = ('#', CMS_STORAGE_CDS_LIST_LABEL)
        parent = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        return (parent, leaf)


class CdSInfoViewHandler(BaseStorageHandler):
    template = "storage_cdsinfo.html"

    def __init__(self, **kwargs):
        super(CdSInfoViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_CDS_API}{self.code}/'
        return super().as_view()

    @property
    def parent_url(self):
        url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_BASE_PATH}/{CMS_STORAGE_CDS_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        # leaf = (self.pub_context.url, getattr(self.pub_context.publication, 'title'))
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        parent = (self.parent_url, CMS_STORAGE_CDS_LIST_LABEL)
        leaf = ('#', self.code)
        return (root, parent, leaf)


class ActivityViewHandler(BaseStorageHandler):
    template = "storage_activity.html"

    def __init__(self, **kwargs):
        super(ActivityViewHandler, self).__init__(**kwargs)
        self.cdsid = self.match_dict.get('cdsid', '')
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_ACTIVITY_API}{self.code}/'
        return super().as_view()

    @property
    def cdslist_url(self):
        url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_BASE_PATH}/{CMS_STORAGE_CDS_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def cdsid_url(self):
        url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_BASE_PATH}/{CMS_STORAGE_CDS_VIEW_PREFIX_PATH}/{self.cdsid}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        cdslist = (self.cdslist_url, CMS_STORAGE_CDS_LIST_LABEL)
        cdsid = (self.cdsid_url, self.cdsid)
        activities = (self.cdsid_url, CMS_STORAGE_ACTIVITIES_LABEL)
        leaf = ('#', self.code)
        return (root, cdslist, cdsid, activities, leaf)


class SingleActivityViewHandler(BaseStorageHandler):
    template = "storage_activity.html"

    def __init__(self, **kwargs):
        super(SingleActivityViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_ACTIVITY_API}{self.code}/'
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        activities = ('#', CMS_STORAGE_ACTIVITIES_LABEL)
        leaf = ('#', self.code)
        return (root, activities, leaf)


class TeacherListViewHandler(BaseStorageHandler):
    template = "storage_teachers_list.html"

    def __init__(self, **kwargs):
        super(TeacherListViewHandler, self).__init__(**kwargs)

    def as_view(self):

        # url_data = {}

        # if ALLOWED_TEACHER_ROLES:
            # url_data['role'] = ",".join(ALLOWED_TEACHER_ROLES)

        # params = urllib.parse.urlencode(url_data)
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_TEACHER_API}'
        # if params: self.data['url'] = f"{self.data['url']}?{params}"
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', CMS_STORAGE_TEACHERS_LABEL)
        return (root, leaf)


class TeacherInfoViewHandler(BaseStorageHandler):
    template = "storage_teachers_info.html"

    def __init__(self, **kwargs):
        super(TeacherInfoViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_TEACHER_API}{self.code}/'
        self.data['code'] = self.code
        return super().as_view()

    @property
    def parent_url(self):
        url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_BASE_PATH}/{CMS_STORAGE_TEACHER_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        parent = (self.parent_url, CMS_STORAGE_TEACHERS_LABEL)
        leaf = ('#', self.code)
        return (root, parent, leaf)


class AddressbookListViewHandler(BaseStorageHandler):
    template = "storage_addressbook_list.html"

    def __init__(self, **kwargs):
        super(AddressbookListViewHandler, self).__init__(**kwargs)

    def as_view(self):

        # url_data = {}

        # if ALLOWED_ADDRESSBOOK_ROLES:
            # url_data['role'] = ",".join(ALLOWED_ADDRESSBOOK_ROLES)
        # if ALLOWED_ADDRESSBOOK_STRUCTURE_ID:
            # url_data['structure'] = ",".join(ALLOWED_ADDRESSBOOK_STRUCTURE_ID)
        # if ALLOWED_STRUCTURE_TYPES:
            # url_data['structuretypes'] = ",".join(ALLOWED_STRUCTURE_TYPES)
            # #000 = Non assegnato
            # url_data['structuretypes'] += ",000"

        # params = urllib.parse.urlencode(url_data)
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_ADDRESSBOOK_API}'
        # if params: self.data['url'] = f"{self.data['url']}?{params}"
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', CMS_STORAGE_ADDRESSBOOK_LABEL)
        return (root, leaf)


class AddressbookInfoViewHandler(BaseStorageHandler):
    template = "storage_addressbook_info.html"

    def __init__(self, **kwargs):
        super(AddressbookInfoViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_ADDRESSBOOK_API}{self.code}/'
        return super().as_view()

    @property
    def parent_url(self):
        url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_BASE_PATH}/{CMS_STORAGE_ADDRESSBOOK_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        parent = (self.parent_url, CMS_STORAGE_ADDRESSBOOK_LABEL)
        leaf = ('#', self.code)
        return (root, parent, leaf)


class StructureListViewHandler(BaseStorageHandler):
    template = "storage_structure_list.html"

    def __init__(self, **kwargs):
        super(StructureListViewHandler, self).__init__(**kwargs)

    def as_view(self):
        url_data = {}

        if INITIAL_STRUCTURE_FATHER != '':
            url_data['father'] = INITIAL_STRUCTURE_FATHER
        if ALLOWED_STRUCTURE_TYPES:
            url_data['type'] = ",".join(ALLOWED_STRUCTURE_TYPES)

        params = urllib.parse.urlencode(url_data)
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_STRUCTURE_API}'
        if params: self.data['url'] = f"{self.data['url']}?{params}"
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', CMS_STORAGE_STRUCTURE_LABEL)
        return (root, leaf)


class StructureInfoViewHandler(BaseStorageHandler):
    template = "storage_structure_info.html"

    def __init__(self, **kwargs):
        super(StructureInfoViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['code'] = self.code
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_STRUCTURE_API}{self.code}/'
        return super().as_view()

    @property
    def parent_url(self):
        url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_BASE_PATH}/{CMS_STORAGE_STRUCTURE_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        parent = (self.parent_url, CMS_STORAGE_STRUCTURE_LABEL)
        leaf = ('#', self.code)
        return (root, parent, leaf)


class LaboratoryListViewHandler(BaseStorageHandler):
    template = "storage_laboratory_list.html"

    def __init__(self, **kwargs):
        super(LaboratoryListViewHandler, self).__init__(**kwargs)

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_LABORATORY_API}'
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', CMS_STORAGE_LABORATORY_LABEL)
        return (root, leaf)


class LaboratoryInfoViewHandler(BaseStorageHandler):
    template = "storage_laboratory_info.html"

    def __init__(self, **kwargs):
        super(LaboratoryInfoViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_LABORATORY_API}{self.code}/'
        return super().as_view()

    @property
    def parent_url(self):
        url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_BASE_PATH}/{CMS_STORAGE_LABORATORY_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        parent = (self.parent_url, CMS_STORAGE_LABORATORY_LABEL)
        leaf = ('#', self.code)
        return (root, parent, leaf)


class ResearchGroupListViewHandler(BaseStorageHandler):
    template = "storage_research_group_list.html"

    def __init__(self, **kwargs):
        super(ResearchGroupListViewHandler, self).__init__(**kwargs)

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_RESEARCH_GROUP_API}'
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', CMS_STORAGE_RESEARCH_GROUP_LABEL)
        return (root, leaf)


class BaseResearchLineListViewHandler(BaseStorageHandler):
    template = "storage_base_research_line_list.html"

    def __init__(self, **kwargs):
        super(BaseResearchLineListViewHandler, self).__init__(**kwargs)

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_BASE_RESEARCH_LINE_API}'
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', CMS_STORAGE_BASE_RESEARCH_LINE_LABEL)
        return (root, leaf)


class ResearchLineListViewHandler(BaseStorageHandler):
    template = "storage_research_line_list.html"

    def __init__(self, **kwargs):
        super(ResearchLineListViewHandler, self).__init__(**kwargs)

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_RESEARCH_LINE_API}'
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', CMS_STORAGE_RESEARCH_LINE_LABEL)
        return (root, leaf)


class AppliedResearchLineListViewHandler(BaseStorageHandler):
    template = "storage_applied_research_line_list.html"

    def __init__(self, **kwargs):
        super(AppliedResearchLineListViewHandler, self).__init__(**kwargs)

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_APPLIED_RESEARCH_LINE_API}'
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', CMS_STORAGE_APPLIED_RESEARCH_LINE_LABEL)
        return (root, leaf)


class PublicationsListViewHandler(BaseStorageHandler):
    template = "storage_publications_list.html"

    def __init__(self, **kwargs):
        super(PublicationsListViewHandler, self).__init__(**kwargs)

    def as_view(self):
        # url_data = {}
        # params = urllib.parse.urlencode(url_data)
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_PUBLICATIONS_API}'
        # if params: self.data['url'] = f"{self.data['url']}?{params}"
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', f'{CMS_STORAGE_PUBLICATIONS_LABEL}')
        return (root, leaf)


class PublicationsInfoViewHandler(BaseStorageHandler):
    template = "storage_publications_info.html"

    def __init__(self, **kwargs):
        super(PublicationsInfoViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_PUBLICATIONS_API}{self.code}/'
        return super().as_view()

    @property
    def parent_url(self):
        url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_BASE_PATH}/{CMS_STORAGE_PUBLICATIONS_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        parent = (self.parent_url, CMS_STORAGE_PUBLICATIONS_LABEL)
        leaf = ('#', self.code)
        return (root, parent, leaf)


class PatentsListViewHandler(BaseStorageHandler):
    template = "storage_patents_list.html"

    def __init__(self, **kwargs):
        super(PatentsListViewHandler, self).__init__(**kwargs)

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_PATENTS_API}'
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', CMS_STORAGE_PATENTS_LABEL)
        return (root, leaf)


class SpinoffListViewHandler(BaseStorageHandler):
    template = "storage_spinoff_list.html"

    def __init__(self, **kwargs):
        super(SpinoffListViewHandler, self).__init__(**kwargs)

    def as_view(self):
        # url_data = {}
        # params = urllib.parse.urlencode(url_data)
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_SPINOFF_API}'
        # if params: self.data['url'] = f"{self.data['url']}?{params}"
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', CMS_STORAGE_SPINOFF_LABEL)
        return (root, leaf)


class SpinoffInfoViewHandler(BaseStorageHandler):
    template = "storage_spinoff_info.html"

    def __init__(self, **kwargs):
        super(SpinoffInfoViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['code'] = self.code
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_SPINOFF_API}{self.code}/'
        return super().as_view()

    @property
    def parent_url(self):
        url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_BASE_PATH}/{CMS_STORAGE_SPINOFF_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        parent = (self.parent_url, CMS_STORAGE_SPINOFF_LABEL)
        leaf = ('#', self.code)
        return (root, parent, leaf)


class ProjectsListViewHandler(BaseStorageHandler):
    template = "storage_projects_list.html"

    def __init__(self, **kwargs):
        super(ProjectsListViewHandler, self).__init__(**kwargs)

    def as_view(self):
        # url_data = {}
        # params = urllib.parse.urlencode(url_data)
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_PROJECTS_API}'
        # if params: self.data['url'] = f"{self.data['url']}?{params}"
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', CMS_STORAGE_PROJECTS_LABEL)
        return (root, leaf)


class ProjectsInfoViewHandler(BaseStorageHandler):
    template = "storage_projects_info.html"

    def __init__(self, **kwargs):
        super(ProjectsInfoViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_PROJECTS_API}{self.code}/'
        return super().as_view()

    @property
    def parent_url(self):
        url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_BASE_PATH}/{CMS_STORAGE_PROJECTS_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        parent = (self.parent_url, CMS_STORAGE_PROJECTS_LABEL)
        leaf = ('#', self.code)
        return (root, parent, leaf)


class HighFormationMastersListViewHandler(BaseStorageHandler):
    template = "storage_high_formation_masters_list.html"

    def __init__(self, **kwargs):
        super(HighFormationMastersListViewHandler, self).__init__(**kwargs)

    def as_view(self):
        url_data = {}
        # if HIGH_FORMATION_YEAR:
            # url_data['year'] = HIGH_FORMATION_YEAR
        # params = urllib.parse.urlencode(url_data)
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_HIGH_FORMATION_MASTERS_API}'
        # if params: self.data['url'] = f"{self.data['url']}?{params}"
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', CMS_STORAGE_HIGH_FORMATION_MASTERS_LABEL)
        return (root, leaf)


class HighFormationMastersInfoViewHandler(BaseStorageHandler):
    template = "storage_high_formation_master_info.html"

    def __init__(self, **kwargs):
        super(HighFormationMastersInfoViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_HIGH_FORMATION_MASTERS_API}{self.code}/'
        return super().as_view()

    @property
    def parent_url(self):
        url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_BASE_PATH}/{CMS_STORAGE_HIGH_FORMATION_MASTERS_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        parent = (self.parent_url, CMS_STORAGE_HIGH_FORMATION_MASTERS_LABEL)
        leaf = ('#', self.code)
        return (root, parent, leaf)


class PhdActivitiesListViewHandler(BaseStorageHandler):
    template = "storage_phd_activities_list.html"

    def __init__(self, **kwargs):
        super(PhdActivitiesListViewHandler, self).__init__(**kwargs)

    def as_view(self):
        # url_data = {}

        # if CURRENT_YEAR:
            # url_data['year'] = CURRENT_YEAR

        # params = urllib.parse.urlencode(url_data)
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_PHD_ACTIVITIES_API}'
        # if params: self.data['url'] = f"{self.data['url']}?{params}"
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', CMS_STORAGE_PHD_ACTIVITIES_LABEL)
        return (root, leaf)


class PhdActivitiesInfoViewHandler(BaseStorageHandler):
    template = "storage_phd_activities_info.html"

    def __init__(self, **kwargs):
        super(PhdActivitiesInfoViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_PHD_ACTIVITIES_API}{self.code}/'
        return super().as_view()

    @property
    def parent_url(self):
        url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_BASE_PATH}/{CMS_STORAGE_PHD_ACTIVITIES_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        parent = (self.parent_url, CMS_STORAGE_PHD_ACTIVITIES_LABEL)
        leaf = ('#', self.code)
        return (root, parent, leaf)



class TeacherNewsListViewHandler(BaseStorageHandler):
    template = "storage_news_list.html"

    def __init__(self, **kwargs):
        super(TeacherNewsListViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        # url_data = {}

        # if CURRENT_YEAR:
            # url_data['year'] = CURRENT_YEAR

        # params = urllib.parse.urlencode(url_data)
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_TEACHER_API}{self.code}/{CMS_STORAGE_TEACHER_NEWS_API}'
        # if params: self.data['url'] = f"{self.data['url']}?{params}"
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', CMS_STORAGE_TEACHER_NEWS_LABEL)
        return (root, leaf)


class ActivitiesListViewHandler(BaseStorageHandler):
    template = "storage_activities_list.html"

    def __init__(self, **kwargs):
        super(ActivitiesListViewHandler, self).__init__(**kwargs)

    def as_view(self):
        url_data = {}
        # if HIGH_FORMATION_YEAR:
            # url_data['year'] = HIGH_FORMATION_YEAR
        # params = urllib.parse.urlencode(url_data)
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_ACTIVITY_API}'
        # if params: self.data['url'] = f"{self.data['url']}?{params}"
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        leaf = ('#', CMS_STORAGE_ACTIVITIES_LABEL)
        return (root, leaf)


class SingleActivityViewHandler(BaseStorageHandler):
    template = "storage_activity.html"

    def __init__(self, **kwargs):
        super(SingleActivityViewHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_ACTIVITY_API}{self.code}/'
        return super().as_view()

    @property
    def breadcrumbs(self):
        root = (self.get_base_url, CMS_STORAGE_ROOT_LABEL)
        activities = ('#', CMS_STORAGE_ACTIVITIES_LABEL)
        leaf = ('#', self.code)
        return (root, activities, leaf)


####### CDS WEBSITES #######

class CdsWebsiteBaseHandler(BaseContentHandler):
    def check_webpath(self):
        if not self.webpath.pk in CMS_WEBPATH_CDS:
            raise Http404('No degree course linked to this webpath')

        self.page = Page.objects.filter(is_active=True,
                                        webpath=self.webpath).first()
        self.cds_cod = CMS_WEBPATH_CDS[self.webpath.pk]

    def __init__(self, **kwargs):
        super(CdsWebsiteBaseHandler, self).__init__(**kwargs)
        self.match_dict = self.match.groupdict()
        self.webpath = WebPath.objects.filter(site=self.website,
                                              fullpath=self.match_dict.get('webpath', ''),
                                              is_active=True)\
                                      .first()
        if not self.webpath:
            raise Http404('Unknown WebPath')

        self.check_webpath()

        self.data = {'request': self.request,
                     'webpath': self.webpath,
                     'website': self.website,
                     'page': self.page,
                     'path': self.match_dict.get('webpath', '/'),
                     'handler': self,
                     'cds_cod': self.cds_cod,
                     'csrf': get_token(self.request)
        }

    def as_view(self):
        if not self.template: return
        ext_template_sources = contextualize_template(self.template,
                                                      self.page)
        template = Template(ext_template_sources)
        context = Context(self.data)

        return HttpResponse(template.render(context), status=200)

    @property
    def get_base_url(self):
        return self.webpath.get_full_path()


class CdsWebsitesProspectHandler(CdsWebsiteBaseHandler):

    template = "storage_cds_websites_prospect.html"

    def check_webpath(self):
        course_type = self.cds_json['CourseType']
        if self.webpath.pk != CMS_WEBPATH_PROSPECT.get(course_type, CMS_WEBPATH_PROSPECT_DEFAULT):
            raise Http404('No study course linked to this webpath')

        self.page = Page.objects.filter(is_active=True,
                                        webpath=self.webpath).first()

    def __init__(self, **kwargs):
        self.redirect = False
        self.cds_cod = kwargs['cds_cod']

        # old study course!
        if CMS_WEBPATH_CDS_OLD.get(self.cds_cod):
            raise Http404

        cds_data = requests.get(f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_CDS_VIEW_PREFIX_PATH}/?cdscod={self.cds_cod}&academicyear={CDS_WEBSITE_PROSPECT_CURRENT_YEAR}&format=json', timeout=5)

        if not cds_data or cds_data.status_code != 200:
            raise Http404

        self.cds_json = cds_data.json()['results'][0]

        super(CdsWebsitesProspectHandler, self).__init__(**kwargs)

        if self.request.POST:
            form = DynCdsWebsiteContactForm(data=self.request.POST)
            if form.is_valid():
                name = f"{form.cleaned_data['first_name']} {form.cleaned_data['last_name']}"
                course = f"{self.cds_json['CdSCod']} - {self.cds_json['CdSName']}"
                try:
                    send_mail(
                        subject=f"Richiesta informazioni: {course} - {name}",
                        message=f"{form.cleaned_data['message']} Email: {form.cleaned_data['email']}",
                        html_message=f"<b>Utente:</b> {name}<br><b>Email:</b> {form.cleaned_data['email']}<br><b>Telefono:</b> {form.cleaned_data['phone']}<br><br><b>Messaggio:</b><p>{form.cleaned_data['message']}</p><br>",
                        from_email=settings.EMAIL_SENDER,
                        recipient_list=CMS_STORAGE_CDS_WEBSITE_PROSPECT_EMAIL_RECIPIENTS,
                        fail_silently=False,
                    )
                    messages.add_message(
                        self.request,
                        messages.SUCCESS,
                        _("Your message has been successfully sent"),
                    )
                    self.redirect = True
                except:
                    messages.add_message(
                        self.request,
                        messages.ERROR,
                        _("Your message was not sent due to a technical problem. Try later"),
                    )
            else:
                for k, v in form.errors.items():
                    messages.add_message(
                        self.request,
                        messages.ERROR,
                        f"{k}: {v}"
                    )
        else:
            form = DynCdsWebsiteContactForm()

        self.data['messages'] = messages.get_messages(self.request)
        self.data['form'] = form
        self.data['hide_cds_auto_menu'] = 1

    def as_view(self):
        if self.redirect: return HttpResponseRedirect(self.request.path_info)
        return super(CdsWebsitesProspectHandler, self).as_view()

    @property
    def breadcrumbs(self):
        return [('#', self.cds_json['CdSName'])]


class CdsWebsitesCorsoHandler(CdsWebsiteBaseHandler):
    template = "storage_cds_websites_corso.html"

    @property
    def breadcrumbs(self):
        return [('#', CMS_STORAGE_CDS_WEBSITES_CORSO_LABEL)]


class CdsWebsitesCorsoActivityHandler(CdsWebsiteBaseHandler):
    template = "storage_cds_website_activity.html"

    def __init__(self, **kwargs):
        super(CdsWebsitesCorsoActivityHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_ACTIVITY_API}{self.code}/'
        return super().as_view()

    @property
    def corso_url(self):
        url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_CDS_WEBSITES_BASE_PATH}/{CMS_STORAGE_CDS_WEBSITES_CORSO_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        corso = (self.corso_url, CMS_STORAGE_CDS_WEBSITES_CORSO_LABEL)
        leaf = ('#', self.code)
        return (corso, leaf)


class CdsWebsitesIscriversiHandler(CdsWebsiteBaseHandler):
    template = "storage_cds_websites_iscriversi.html"

    @property
    def breadcrumbs(self):
        return [('#', CMS_STORAGE_CDS_WEBSITES_ISCRIVERSI_LABEL)]


class CdsWebsitesStudiareHandler(CdsWebsiteBaseHandler):
    template = "storage_cds_websites_studiare.html"

    @property
    def breadcrumbs(self):
        return [('#', CMS_STORAGE_CDS_WEBSITES_STUDIARE_LABEL)]


class CdsWebsitesStudiareActivityHandler(CdsWebsiteBaseHandler):
    template = "storage_cds_website_activity.html"

    def __init__(self, **kwargs):
        super(CdsWebsitesStudiareActivityHandler, self).__init__(**kwargs)
        self.code = self.match_dict.get('code', '')

    def as_view(self):
        self.data['url'] = f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_ACTIVITY_API}{self.code}/'
        return super().as_view()

    @property
    def studiare_url(self):
        url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_CDS_WEBSITES_BASE_PATH}/{CMS_STORAGE_CDS_WEBSITES_STUDIARE_VIEW_PREFIX_PATH}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        studiare = (self.studiare_url, CMS_STORAGE_CDS_WEBSITES_STUDIARE_LABEL)
        leaf = ('#', self.code)
        return (studiare, leaf)


class CdsWebsitesStudiareCalendarHandler(CdsWebsiteBaseHandler):
    template = "storage_cds_websites_studiare_calendari.html"

    @property
    def breadcrumbs(self):
        studiare_url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_CDS_WEBSITES_BASE_PATH}/{CMS_STORAGE_CDS_WEBSITES_STUDIARE_VIEW_PREFIX_PATH}/'
        return [(sanitize_path(studiare_url), CMS_STORAGE_CDS_WEBSITES_STUDIARE_LABEL),
                ('#', CMS_STORAGE_CDS_WEBSITES_STUDIARE_CALENDAR_LABEL)]


class CdsWebsitesStudiareScheduleHandler(CdsWebsiteBaseHandler):
    template = "storage_cds_websites_studiare_orari.html"

    @property
    def breadcrumbs(self):
        studiare_url = f'{self.webpath.get_full_path()}/{CMS_STORAGE_CDS_WEBSITES_BASE_PATH}/{CMS_STORAGE_CDS_WEBSITES_STUDIARE_VIEW_PREFIX_PATH}/'
        return [(sanitize_path(studiare_url), CMS_STORAGE_CDS_WEBSITES_STUDIARE_LABEL),
                ('#', CMS_STORAGE_CDS_WEBSITES_STUDIARE_SCHEDULE_LABEL)]


class CdsWebsitesOpportunitaHandler(CdsWebsiteBaseHandler):
    template = "storage_cds_websites_opportunita.html"

    @property
    def breadcrumbs(self):
        return [('#', CMS_STORAGE_CDS_WEBSITES_OPPORTUNITA_LABEL)]


class CdsWebsitesOrganizzazioneHandler(CdsWebsiteBaseHandler):
    template = "storage_cds_websites_organizzazione.html"

    @property
    def breadcrumbs(self):
        return [('#', CMS_STORAGE_CDS_WEBSITES_ORGANIZZAZIONE_LABEL)]


class CdsWebsitesRedirectHandler(BaseContentHandler):
    def __init__(self, **kwargs):
        super(CdsWebsitesRedirectHandler, self).__init__(**kwargs)
        path_dict = getattr(settings, 'CMS_WEBPATH_CDS', {})
        self.webpath = None
        for path in path_dict:
            if path_dict[path] == kwargs['cds_cod']:
                self.webpath = get_object_or_404(WebPath,
                                                 pk=path,
                                                 is_active=True)
                break

    def as_view(self):
        if not self.webpath: raise Http404()
        return redirect(self.webpath.get_site_path())


class CdsWebsitesRedirectProspectHandler(CdsWebsitesRedirectHandler):
    def __init__(self, **kwargs):
        self.cds_cod = kwargs['cds_cod']

        # old study course!
        if CMS_WEBPATH_CDS_OLD.get(self.cds_cod):
            raise Http404

        cds_data = requests.get(f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_CDS_VIEW_PREFIX_PATH}/?cdscod={self.cds_cod}&academicyear={CDS_WEBSITE_PROSPECT_CURRENT_YEAR}&format=json', timeout=5)

        if not cds_data or cds_data.status_code != 200 or not cds_data.json()['results']:
            for new_cds in CMS_WEBPATH_CDS_MORPH:
                if self.cds_cod in CMS_WEBPATH_CDS_MORPH[new_cds]:
                    cds_data = requests.get(f'{CMS_STORAGE_BASE_API}{CMS_STORAGE_CDS_VIEW_PREFIX_PATH}/?cdscod={new_cds}&academicyear={CDS_WEBSITE_PROSPECT_CURRENT_YEAR}&format=json', timeout=5)
                    break
            if not cds_data or cds_data.status_code != 200 or not cds_data.json()['results']:
                raise Http404

        self.cds_json = cds_data.json()['results'][0]

        super(CdsWebsitesRedirectHandler, self).__init__(**kwargs)

        cds_type = self.cds_json['CourseType']
        self.webpath = get_object_or_404(WebPath,
                                         pk=CMS_WEBPATH_PROSPECT.get(cds_type, CMS_WEBPATH_PROSPECT_DEFAULT),
                                         is_active=True)

    def as_view(self):
        if not self.webpath: raise Http404()
        root = WebPath.objects.filter(pk=settings.CMS_WEBPATH_PROSPECT_DEFAULT).first()
        if not root: raise Http404()

        cds_name =  self.cds_json['CdSName']
        cds_cod =  self.cds_json['CdSCod']
        return redirect('//' + sanitize_path(f'{root.site.domain}/{root.fullpath}/{settings.CMS_PATH_PREFIX}{self.webpath.fullpath}/{CMS_STORAGE_CDS_WEBSITES_BASE_PATH}/{cds_cod}-{slugify(cds_name)}/{CMS_STORAGE_CDS_WEBSITES_PROSPECT_VIEW_PREFIX_PATH}/'))


class CdsWebsitesStudyActivityRedirectHandler(CdsWebsitesRedirectHandler):
    def __init__(self, **kwargs):
        super(CdsWebsitesStudyActivityRedirectHandler, self).__init__(**kwargs)
        self.sub_path = kwargs['sub_path']
        self.activity_id = kwargs['code']

    def as_view(self):
        if self.webpath:
            return redirect(sanitize_path(f'/{settings.CMS_PATH_PREFIX}{self.webpath.fullpath}/{CMS_STORAGE_CDS_VIEW_PREFIX_PATH}/{self.sub_path}/{CMS_STORAGE_ACTIVITY_VIEW_PREFIX_PATH}/{self.activity_id}/'))
        raise Http404()
