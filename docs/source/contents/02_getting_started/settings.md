Settings
--------

List of website pks allowed to display the pages.
This can be overridden in settingslocal
````
ALLOWED_UNICMS_SITES = [1]
````

Auto-built webpaths. Can't be overridden.
````
CMS_STORAGE_BASE_PATH = 'storage'
CMS_STORAGE_CDS_VIEW_PREFIX_PATH = 'cds'
CMS_STORAGE_ACTIVITY_VIEW_PREFIX_PATH = 'activities'
CMS_STORAGE_TEACHER_VIEW_PREFIX_PATH = 'teachers'
CMS_STORAGE_ADDRESSBOOK_VIEW_PREFIX_PATH = 'addressbook'
CMS_STORAGE_STRUCTURE_VIEW_PREFIX_PATH = 'structures'
CMS_STORAGE_LABORATORY_VIEW_PREFIX_PATH = 'laboratories'
CMS_STORAGE_PUBLICATIONS_VIEW_PREFIX_PATH = 'publications'
````

Regular expressions managing webpath handling.
Can't be ovverridden.
````
CMS_STORAGE_BASE_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})(/)?$' # noqa
CMS_STORAGE_CDS_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_CDS_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_CDS_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_CDS_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
CMS_STORAGE_ACTIVITY_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_CDS_VIEW_PREFIX_PATH})/(?P<cdsid>[a-z0-9\-]*)/{CMS_STORAGE_ACTIVITY_VIEW_PREFIX_PATH}/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
CMS_STORAGE_TEACHER_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_TEACHER_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_TEACHER_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_TEACHER_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
CMS_STORAGE_PUBLICATIONS_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_TEACHER_VIEW_PREFIX_PATH})/(?P<teacherid>[a-z0-9\-]*)/{CMS_STORAGE_PUBLICATIONS_VIEW_PREFIX_PATH}/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
CMS_STORAGE_ADDRESSBOOK_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_ADDRESSBOOK_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_ADDRESSBOOK_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_ADDRESSBOOK_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
CMS_STORAGE_STRUCTURE_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_STRUCTURE_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_STRUCTURE_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_STRUCTURE_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
CMS_STORAGE_LABORATORY_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_LABORATORY_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_LABORATORY_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_LABORATORY_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
````

Handlers list (used in settingslocal as shown in Setup guide).
````
CMS_STORAGE_HANDLERS_PATHS = [CMS_STORAGE_BASE_URL_VIEW_REGEXP,
                              CMS_STORAGE_ACTIVITY_URL_VIEW_REGEXP,
                              CMS_STORAGE_ADDRESSBOOK_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_ADDRESSBOOK_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_CDS_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_CDS_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_LABORATORY_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_LABORATORY_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_STRUCTURE_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_STRUCTURE_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_TEACHER_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_TEACHER_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_PUBLICATIONS_INFO_URL_VIEW_REGEXP,
                              ]
````

Handlers dictionary (used in settingslocal as shown in Setup guide)
````
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
    'unicms_unical_storage_handler.handlers.PublicationsInfoViewHandler': CMS_STORAGE_PUBLICATIONS_INFO_URL_VIEW_REGEXP,
}
````

API endpoints. These values can be overridden.
````
# cms_storage APIs (ref: https://storage.unical.it)
CMS_STORAGE_BASE_API = 'https://storage.portale.unical.it/api/ricerca/'

CMS_STORAGE_ACADEMICYEARS_API = f'{CMS_STORAGE_BASE_API}academicyears/'
CMS_STORAGE_ACTIVITY_API = f'{CMS_STORAGE_BASE_API}activities/'
CMS_STORAGE_ADDRESSBOOK_API = f'{CMS_STORAGE_BASE_API}addressbook/'
CMS_STORAGE_CDS_API = f'{CMS_STORAGE_BASE_API}cds/'
CMS_STORAGE_COMMUNITYTYPES_API = f'{CMS_STORAGE_BASE_API}publicationscommunitytypes/'
CMS_STORAGE_DEGREETYPES_API = f'{CMS_STORAGE_BASE_API}degreetypes/'
CMS_STORAGE_DEPARTMENTSFILTER_API = f'{CMS_STORAGE_BASE_API}departmentsfilter/'
CMS_STORAGE_ERC0LIST_API = f'{CMS_STORAGE_BASE_API}erc0list/'
CMS_STORAGE_ERC1LIST_API = f'{CMS_STORAGE_BASE_API}erc1list/'
CMS_STORAGE_LABORATORIESAREAS_API = f'{CMS_STORAGE_BASE_API}laboratoriesareas/'
CMS_STORAGE_LABORATORY_API = f'{CMS_STORAGE_BASE_API}laboratories/'
CMS_STORAGE_ROLES_API = f'{CMS_STORAGE_BASE_API}roles/'
CMS_STORAGE_STRUCTURE_API = f'{CMS_STORAGE_BASE_API}structures/'
CMS_STORAGE_STRUCTUREFILTER_API = f'{CMS_STORAGE_BASE_API}structuresfilter/'
CMS_STORAGE_STRUCTURETYPES_API = f'{CMS_STORAGE_BASE_API}structuretypes/'
CMS_STORAGE_TEACHER_API = f'{CMS_STORAGE_BASE_API}teachers/'
````

Labels for titles and breadcrumbs. These can be ovverridden.
````
CMS_STORAGE_ACTIVITIES_LABEL = _("Teachings")
CMS_STORAGE_ADDRESSBOOK_LABEL = _("Persons")
CMS_STORAGE_CDS_LIST_LABEL = _("Study courses")
CMS_STORAGE_LABORATORY_LABEL = _("Laboratories")
CMS_STORAGE_PUBLICATIONS_LABEL = _("Publications")
CMS_STORAGE_ROOT_LABEL = _("Data storage")
CMS_STORAGE_STRUCTURE_LABEL = _("Structures")
CMS_STORAGE_TEACHERS_LABEL = _("Teachers")
````

API filters to take only choosen data in templates.
Each of these can be overridden in settings.
````
# show only these coursetypes (es: ['L','LM'])
ALLOWED_CDS_COURSETYPES = []

# allowed study courses languages
ALLOWED_CDS_LANGUAGES = ['ita', 'eng']

# API base filters
ALLOWED_CDS_JOINT_DEGREES = [
    {'COD': 'N', 'name': _("No")},
    {'COD': 'S', 'name': _("Joint title")},
    {'COD': 'D', 'name': _("Double title")}
]


ALLOWED_ADDRESSBOOK_ROLES = []
ALLOWED_ADDRESSBOOK_STRUCTURE_ID = []


ALLOWED_STRUCTURE_TYPES = []
ALLOWED_COMMUNITY_TYPES = []

# fields to show templates
CDS_INFO_FIELDS = ['CdSGoals', 'CdSAccess', 'CdSAdmission',
                   'CdSProfiles', 'CdSFinalTest', 'CdSFinalTestMode',
                   'CdSSatisfactionSurvey']

# fields to hide in templates
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

PUBLICATIONS_INFO_NOT_SHOW = ['PublicationId', 'PublicationAbstract',
                              'PublicationTitle', 'PublicationCommunity',
                              'PublicationCollection', 'PublicationReferenceAuthor']

# if set, API will retrieve only structures with this parent and later
INITIAL_STRUCTURE_FATHER = ''
````

Almalaurea trasparenza link. This can be overridden.
````
# ALMALAUREA Link
ALMALAUREA_LINK = 'http://statistiche.almalaurea.it/universita/statistiche/trasparenza?codicione='
````
