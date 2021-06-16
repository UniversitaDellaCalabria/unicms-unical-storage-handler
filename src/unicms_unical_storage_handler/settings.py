import logging

from django.utils.translation import gettext_lazy as _


logger = logging.getLogger(__name__)


# list of website pks allowed to display the pages
ALLOWED_UNICMS_SITES = [2]

# base path
CMS_STORAGE_BASE_PATH = 'storage'
CMS_STORAGE_CDS_VIEW_PREFIX_PATH = 'cds'
CMS_STORAGE_ACTIVITY_VIEW_PREFIX_PATH = 'activities'
CMS_STORAGE_THEACHER_VIEW_PREFIX_PATH = 'teachers'

# regexps
CMS_STORAGE_BASE_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})(/)?$' # noqa
CMS_STORAGE_CDS_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_CDS_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_CDS_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_CDS_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
CMS_STORAGE_ACTIVITY_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_CDS_VIEW_PREFIX_PATH})/(?P<cdsid>[a-z0-9\-]*)/activities/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
CMS_STORAGE_TEACHERLIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_THEACHER_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_TEACHERINFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_THEACHER_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]*)(/)?$' # noqa

CMS_STORAGE_HANDLERS_PATHS = [CMS_STORAGE_BASE_URL_VIEW_REGEXP,
                              CMS_STORAGE_CDS_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_CDS_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_ACTIVITY_URL_VIEW_REGEXP,
                              CMS_STORAGE_TEACHERLIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_TEACHERINFO_URL_VIEW_REGEXP,
                              ]

CMS_STORAGE_APP_REGEXP_URLPATHS = {
    'unicms_unical_storage_handler.handlers.BaseStorageHandler' : CMS_STORAGE_BASE_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.CdSListViewHandler' : CMS_STORAGE_CDS_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.CdSInfoViewHandler' : CMS_STORAGE_CDS_INFO_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.ActivityViewHandler' : CMS_STORAGE_ACTIVITY_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.TeacherListViewHandler' : CMS_STORAGE_TEACHERLIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.TeacherInfoViewHandler' : CMS_STORAGE_TEACHERINFO_URL_VIEW_REGEXP,
}

# cms_storage APIs (ref: https://storage.unical.it)
CMS_STORAGE_BASE_API = 'https://storage.portale.unical.it/api/ricerca/'
CMS_STORAGE_CDS_API = f'{CMS_STORAGE_BASE_API}cds/'
CMS_STORAGE_ACTIVITY_API = f'{CMS_STORAGE_BASE_API}activities/'
CMS_STORAGE_TEACHER_API = f'{CMS_STORAGE_BASE_API}teachers/'

# labels (for breadcrumbs and page title)
CMS_STORAGE_ROOT_LABEL = _("Data storage")
CMS_STORAGE_CDS_LIST_LABEL = _("Corsi di studio")
CMS_STORAGE_ACTIVITIES_LABEL = _("Insegnamenti")
CMS_STORAGE_TEACHERS_LABEL = _("Docenti")
