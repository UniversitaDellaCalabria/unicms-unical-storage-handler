import logging

from django.utils.translation import gettext_lazy as _


logger = logging.getLogger(__name__)


# list of website pks allowed to display the pages
ALLOWED_UNICMS_SITES = [1]

# base path
CMS_STORAGE_BASE_PATH = 'storage'
CMS_STORAGE_CDS_VIEW_PREFIX_PATH = 'cds'
CMS_STORAGE_ACTIVITY_VIEW_PREFIX_PATH = 'activities'
CMS_STORAGE_THEACHER_VIEW_PREFIX_PATH = 'teachers'
CMS_STORAGE_ADDRESSBOOK_VIEW_PREFIX_PATH = 'addressbook'
CMS_STORAGE_STRUCTURE_VIEW_PREFIX_PATH = 'structures'
CMS_STORAGE_STRUCTURETYPES_VIEW_PREFIX_PATH = 'structuretypes'
CMS_STORAGE_LABORATORY_VIEW_PREFIX_PATH = 'laboratories'

# regexps
CMS_STORAGE_BASE_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})(/)?$' # noqa
CMS_STORAGE_CDS_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_CDS_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_CDS_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_CDS_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
CMS_STORAGE_ACTIVITY_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_CDS_VIEW_PREFIX_PATH})/(?P<cdsid>[a-z0-9\-]*)/activities/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
CMS_STORAGE_TEACHER_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_THEACHER_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_TEACHER_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_THEACHER_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
CMS_STORAGE_ADDRESSBOOK_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_ADDRESSBOOK_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_ADDRESSBOOK_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_ADDRESSBOOK_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
CMS_STORAGE_STRUCTURE_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_STRUCTURE_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_STRUCTURE_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_STRUCTURE_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
CMS_STORAGE_LABORATORY_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_LABORATORY_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_LABORATORY_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_LABORATORY_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]*)(/)?$' # noqa

CMS_STORAGE_HANDLERS_PATHS = [CMS_STORAGE_BASE_URL_VIEW_REGEXP,
                              CMS_STORAGE_CDS_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_CDS_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_ACTIVITY_URL_VIEW_REGEXP,
                              CMS_STORAGE_TEACHER_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_TEACHER_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_ADDRESSBOOK_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_ADDRESSBOOK_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_STRUCTURE_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_STRUCTURE_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_LABORATORY_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_LABORATORY_INFO_URL_VIEW_REGEXP,
                              ]

CMS_STORAGE_APP_REGEXP_URLPATHS = {
    'unicms_unical_storage_handler.handlers.BaseStorageHandler' : CMS_STORAGE_BASE_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.CdSListViewHandler' : CMS_STORAGE_CDS_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.CdSInfoViewHandler' : CMS_STORAGE_CDS_INFO_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.ActivityViewHandler' : CMS_STORAGE_ACTIVITY_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.TeacherListViewHandler' : CMS_STORAGE_TEACHER_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.TeacherInfoViewHandler' : CMS_STORAGE_TEACHER_INFO_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.AddressbookListViewHandler' : CMS_STORAGE_ADDRESSBOOK_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.AddressbookInfoViewHandler' : CMS_STORAGE_ADDRESSBOOK_INFO_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.StructureListViewHandler': CMS_STORAGE_STRUCTURE_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.StructureInfoViewHandler' : CMS_STORAGE_STRUCTURE_INFO_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.LaboratoryListViewHandler': CMS_STORAGE_LABORATORY_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.LaboratoryInfoViewHandler' : CMS_STORAGE_LABORATORY_INFO_URL_VIEW_REGEXP,
}

# cms_storage APIs (ref: https://storage.unical.it)
CMS_STORAGE_BASE_API = 'https://storage.portale.unical.it/api/ricerca/'
CMS_STORAGE_CDS_API = f'{CMS_STORAGE_BASE_API}cds/'
CMS_STORAGE_ACTIVITY_API = f'{CMS_STORAGE_BASE_API}activities/'
CMS_STORAGE_TEACHER_API = f'{CMS_STORAGE_BASE_API}teachers/'
CMS_STORAGE_ADDRESSBOOK_API = f'{CMS_STORAGE_BASE_API}addressbook/'
CMS_STORAGE_STRUCTURE_API = f'{CMS_STORAGE_BASE_API}structures/'
CMS_STORAGE_LABORATORY_API = f'{CMS_STORAGE_BASE_API}laboratories/'

# labels (for breadcrumbs and page title)
CMS_STORAGE_ROOT_LABEL = _("Data storage")
CMS_STORAGE_CDS_LIST_LABEL = _("Study courses")
CMS_STORAGE_ACTIVITIES_LABEL = _("Teachings")
CMS_STORAGE_TEACHERS_LABEL = _("Teachers")
CMS_STORAGE_ADDRESSBOOK_LABEL = _("Persons")
CMS_STORAGE_STRUCTURE_LABEL = _("Structures")
CMS_STORAGE_LABORATORY_LABEL = _("Laboratories")

# API filters
ALLOWED_CDS_COURSETYPES = []
ALLOWED_CDS_LANGUAGES = ['ita', 'eng']
ALLOWED_CDS_JOINT_DEGREES = [
    {'COD': 'N', 'name': _("No")},
    {'COD': 'S', 'name': _("Joint title")},
    {'COD': 'D', 'name': _("Double title")}
]

ALLOWED_ADDRESSBOOK_ROLES = []
ALLOWED_ADDRESSBOOK_STRUCTURE_TYPES = []
ALLOWED_ADDRESSBOOK_STRUCTURE_ID = []

# CDSINFO FIELDS TO SHOW
CDS_INFO_FIELDS = ['CdSGoals', 'CdSAccess', 'CdSAdmission',
                   'CdSProfiles', 'CdSFinalTest', 'CdSFinalTestMode',
                   'CdSSatisfactionSurvey']

# FIELDS TO HIDE IN BLOCKS
ADDRESSBOOK_INFO_NOT_SHOW = ['ID', 'Name', 'Role',
                             'RoleDescription', 'StructureTypeCOD']
TEACHER_INFO_NOT_SHOW = ['TeacherID', 'TeacherDepartmentID',
                         'TeacherLastName', 'TeacherFirstName',
                         'TeacherRole', 'TeacherRoleDescription']

STRUCTURE_INFO_NOT_SHOW = ['StructureId', 'StructureFatherId']

LABORATORY_INFO_NOT_SHOW = ['LaboratoryId', 'CompletionReferentId',
                            'ScientificDirectorId', 'DepartmentReferentId',
                            'LaboratoryErc1Cod', 'LaboratoryErc0Cod',
                            'ResearchPersonnelID', 'TechPersonnelID',
                            'LaboratoryName', 'LaboratoryAcronym',
                            'LaboratoryScope', 'LaboratoryLogo',
                            'LaboratoryErc1', 'LaboratoryResearchPersonnel',
                            'LaboratoryTechPersonnel', 'LaboratoryOfferedServices',
                            'LaboratoryLocation', 'LaboratoryErc0Description',
                            'LaboratoryServicesScope', 'LaboratoryTeachingScope',
                            'LaboratoryResearchScope', 'LaboratoryActivities',
                            'CompletionReferentName', 'TechPersonnelRole']

INITIAL_STRUCTURE_FATHER = ''

# ALMALAUREA Link
ALMALAUREA_LINK = 'http://statistiche.almalaurea.it/universita/statistiche/trasparenza?codicione='
