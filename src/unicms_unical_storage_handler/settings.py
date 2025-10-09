import datetime
import logging

from django.utils.translation import gettext_lazy as _


logger = logging.getLogger(__name__)


# list of website pks allowed to display the pages
ALLOWED_UNICMS_SITES = [1]


# base path
CMS_STORAGE_BASE_PATH = 'storage'

CMS_STORAGE_ACTIVITY_VIEW_PREFIX_PATH = 'activities'
CMS_STORAGE_ADDRESSBOOK_VIEW_PREFIX_PATH = 'addressbook'
CMS_STORAGE_APPLIED_RESEARCH_LINE_VIEW_PREFIX_PATH = 'applied-research-lines'
CMS_STORAGE_BASE_RESEARCH_LINE_VIEW_PREFIX_PATH = 'base-research-lines'
CMS_STORAGE_CDS_VIEW_PREFIX_PATH = 'cds'
CMS_STORAGE_HIGH_FORMATION_MASTERS_VIEW_PREFIX_PATH = 'higher-edu-training'
CMS_STORAGE_LABORATORY_VIEW_PREFIX_PATH = 'laboratories'
CMS_STORAGE_PATENTS_VIEW_PREFIX_PATH = 'patents'
CMS_STORAGE_PHD_ACTIVITIES_VIEW_PREFIX_PATH = 'phd-activities'
CMS_STORAGE_PROJECTS_VIEW_PREFIX_PATH = 'projects'
CMS_STORAGE_PUBLICATIONS_VIEW_PREFIX_PATH = 'publications'
CMS_STORAGE_RESEARCH_GROUP_VIEW_PREFIX_PATH = 'research-groups'
CMS_STORAGE_RESEARCH_LINE_VIEW_PREFIX_PATH = 'research-lines'
CMS_STORAGE_SPINOFF_VIEW_PREFIX_PATH = 'companies'
CMS_STORAGE_STRUCTURE_VIEW_PREFIX_PATH = 'structures'
CMS_STORAGE_TEACHER_VIEW_PREFIX_PATH = 'teachers'
CMS_STORAGE_TEACHER_MATERIALS_VIEW_PREFIX_PATH = 'materials'
CMS_STORAGE_TEACHER_NEWS_VIEW_PREFIX_PATH = 'news'
CMS_STORAGE_ADDRESSBOOK_FRIENDLY_URL_MAIN_EMAIL_DOMAIN = ''

# regexps
CMS_STORAGE_BASE_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})(/)?$' # noqa
CMS_STORAGE_ACTIVITY_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_CDS_VIEW_PREFIX_PATH})/(?P<cdsid>[a-z0-9\-]*)/{CMS_STORAGE_ACTIVITY_VIEW_PREFIX_PATH}/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
CMS_STORAGE_APPLIED_RESEARCH_LINE_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_APPLIED_RESEARCH_LINE_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_BASE_RESEARCH_LINE_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_BASE_RESEARCH_LINE_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_ADDRESSBOOK_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_ADDRESSBOOK_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_ADDRESSBOOK_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_ADDRESSBOOK_VIEW_PREFIX_PATH})/(?P<code>[a-zA-Z0-9\.\-\_\=\:\%]+)(/)?$' # noqa
CMS_STORAGE_CDS_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_CDS_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_CDS_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_CDS_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]+)(/)?$' # noqa
CMS_STORAGE_HIGH_FORMATION_MASTERS_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_HIGH_FORMATION_MASTERS_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_HIGH_FORMATION_MASTERS_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_HIGH_FORMATION_MASTERS_VIEW_PREFIX_PATH})/(?P<code>[a-zA-Z0-9\-\_\=\:\%]+)(/)?$' # noqa
CMS_STORAGE_LABORATORY_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_LABORATORY_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_LABORATORY_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_LABORATORY_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]+)(/)?$' # noqa
CMS_STORAGE_PATENTS_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_PATENTS_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_PHD_ACTIVITES_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_PHD_ACTIVITIES_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_PHD_ACTIVITES_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_PHD_ACTIVITIES_VIEW_PREFIX_PATH})/(?P<code>[a-zA-Z0-9\-\_\=\:\%]+)(/)?$' # noqa
CMS_STORAGE_PROJECTS_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_PROJECTS_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_PROJECTS_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/{CMS_STORAGE_PROJECTS_VIEW_PREFIX_PATH}/(?P<code>[a-z0-9\-]+)(/)?$' # noqa
CMS_STORAGE_PUBLICATIONS_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_PUBLICATIONS_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_PUBLICATIONS_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/{CMS_STORAGE_PUBLICATIONS_VIEW_PREFIX_PATH}/(?P<code>[a-z0-9\-]+)(/)?$' # noqa
CMS_STORAGE_RESEARCH_GROUP_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_RESEARCH_GROUP_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_RESEARCH_LINE_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_RESEARCH_LINE_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_SINGLE_ACTIVITY_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_ACTIVITY_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]+)(/)?$' # noqa
CMS_STORAGE_SPINOFF_URL_LIST_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_SPINOFF_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_SPINOFF_URL_INFO_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_SPINOFF_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]+)(/)?$' # noqa
CMS_STORAGE_STRUCTURE_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_STRUCTURE_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_STRUCTURE_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_STRUCTURE_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]+)(/)?$' # noqa
CMS_STORAGE_TEACHER_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_TEACHER_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_TEACHER_INFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_TEACHER_VIEW_PREFIX_PATH})/(?P<code>[a-zA-Z0-9\.\-\_\=\:\%]+)(/)?$' # noqa
CMS_STORAGE_TEACHER_NEWS_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_TEACHER_VIEW_PREFIX_PATH})/(?P<code>[a-zA-Z0-9\-\_\=\:\%]+)/{CMS_STORAGE_TEACHER_NEWS_VIEW_PREFIX_PATH}(/)?$' # noqa
CMS_STORAGE_ACTIVITIES_LIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_BASE_PATH})/({CMS_STORAGE_ACTIVITY_VIEW_PREFIX_PATH})(/)?$' # noqa


CMS_STORAGE_HANDLERS_PATHS = [
                              CMS_STORAGE_BASE_URL_VIEW_REGEXP,
                              CMS_STORAGE_ACTIVITY_URL_VIEW_REGEXP,
                              CMS_STORAGE_SINGLE_ACTIVITY_URL_VIEW_REGEXP,
                              CMS_STORAGE_ADDRESSBOOK_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_ADDRESSBOOK_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_CDS_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_CDS_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_LABORATORY_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_LABORATORY_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_PATENTS_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_PROJECTS_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_PROJECTS_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_PUBLICATIONS_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_PUBLICATIONS_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_RESEARCH_GROUP_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_BASE_RESEARCH_LINE_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_APPLIED_RESEARCH_LINE_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_RESEARCH_LINE_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_SPINOFF_URL_LIST_VIEW_REGEXP,
                              CMS_STORAGE_SPINOFF_URL_INFO_VIEW_REGEXP,
                              CMS_STORAGE_STRUCTURE_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_STRUCTURE_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_TEACHER_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_TEACHER_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_HIGH_FORMATION_MASTERS_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_HIGH_FORMATION_MASTERS_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_PHD_ACTIVITES_LIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_PHD_ACTIVITES_INFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_TEACHER_NEWS_VIEW_REGEXP,
                              CMS_STORAGE_ACTIVITIES_LIST_URL_VIEW_REGEXP,
                              ]


CMS_STORAGE_APP_REGEXP_URLPATHS = {
    'unicms_unical_storage_handler.handlers.BaseStorageHandler' : CMS_STORAGE_BASE_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.ActivityViewHandler' : CMS_STORAGE_ACTIVITY_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.AddressbookListViewHandler' : CMS_STORAGE_ADDRESSBOOK_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.AddressbookInfoViewHandler' : CMS_STORAGE_ADDRESSBOOK_INFO_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.AppliedResearchLineListViewHandler': CMS_STORAGE_APPLIED_RESEARCH_LINE_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.BaseResearchLineListViewHandler': CMS_STORAGE_BASE_RESEARCH_LINE_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.CdSListViewHandler' : CMS_STORAGE_CDS_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.CdSInfoViewHandler' : CMS_STORAGE_CDS_INFO_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.HighFormationMastersListViewHandler': CMS_STORAGE_HIGH_FORMATION_MASTERS_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.HighFormationMastersInfoViewHandler': CMS_STORAGE_HIGH_FORMATION_MASTERS_INFO_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.LaboratoryListViewHandler': CMS_STORAGE_LABORATORY_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.LaboratoryInfoViewHandler' : CMS_STORAGE_LABORATORY_INFO_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.PatentsListViewHandler' : CMS_STORAGE_PATENTS_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.PhdActivitiesListViewHandler': CMS_STORAGE_PHD_ACTIVITES_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.PhdActivitiesInfoViewHandler': CMS_STORAGE_PHD_ACTIVITES_INFO_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.ProjectsListViewHandler': CMS_STORAGE_PROJECTS_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.ProjectsInfoViewHandler': CMS_STORAGE_PROJECTS_INFO_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.PublicationsListViewHandler': CMS_STORAGE_PUBLICATIONS_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.PublicationsInfoViewHandler': CMS_STORAGE_PUBLICATIONS_INFO_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.ResearchGroupListViewHandler': CMS_STORAGE_RESEARCH_GROUP_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.ResearchLineListViewHandler': CMS_STORAGE_RESEARCH_LINE_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.SingleActivityViewHandler' : CMS_STORAGE_SINGLE_ACTIVITY_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.SpinoffListViewHandler': CMS_STORAGE_SPINOFF_URL_LIST_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.SpinoffInfoViewHandler' : CMS_STORAGE_SPINOFF_URL_INFO_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.StructureListViewHandler': CMS_STORAGE_STRUCTURE_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.StructureInfoViewHandler' : CMS_STORAGE_STRUCTURE_INFO_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.TeacherListViewHandler' : CMS_STORAGE_TEACHER_LIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.TeacherInfoViewHandler' : CMS_STORAGE_TEACHER_INFO_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.TeacherNewsListViewHandler': CMS_STORAGE_TEACHER_NEWS_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.ActivitiesListViewHandler': CMS_STORAGE_ACTIVITIES_LIST_URL_VIEW_REGEXP,

}


# cms_storage APIs (ref: https://storage.unical.it)
CMS_STORAGE_ROOT_API = 'https://pp.storage.unical.it'
CMS_STORAGE_BASE_API = f'{CMS_STORAGE_ROOT_API}/api/ricerca/'

CMS_STORAGE_ACADEMICYEARS_API = 'academicyears/'
CMS_STORAGE_ACTIVITY_API = 'activities/'
CMS_STORAGE_ADDRESSBOOK_API = 'addressbook/'
CMS_STORAGE_APPLIED_RESEARCH_LINE_API = 'appliedresearchlines/'
CMS_STORAGE_ASTER1LIST_API = 'aster1list/'
CMS_STORAGE_BASE_RESEARCH_LINE_API = 'baseresearchlines/'
CMS_STORAGE_RESEARCH_LINE_API = 'allresearchlines/'
CMS_STORAGE_CDS_API = 'cds/'
CMS_STORAGE_CDS_AREAS_API = 'cds-areas/'
CMS_STORAGE_CDS_EXPIRED_API = 'cds-expired/'
CMS_STORAGE_CDS_MORPH_LIST_API = 'cds-morph/'
CMS_STORAGE_CDS_MORPH_DETAIL_API = 'cds-morph/{}/'
CMS_STORAGE_COMMUNITYTYPES_API = 'publicationscommunitytypes/'
CMS_STORAGE_DEGREETYPES_API = 'degreetypes/'
CMS_STORAGE_DEPARTMENTS_API = 'departments/'
CMS_STORAGE_ERC0LIST_API = 'erc0list/'
CMS_STORAGE_ERC1LIST_API = 'erc1list/'
CMS_STORAGE_EROGATIONMODES_API = 'erogation-modes/'
CMS_STORAGE_HIGH_FORMATION_COURSETYPES_API = 'high-formation-course-types/'
CMS_STORAGE_HIGH_FORMATION_MASTERS_API = 'high-formation-masters/'
CMS_STORAGE_INFRASTRUCTURES_API = 'infrastructures/'
CMS_STORAGE_LABORATORY_API = 'laboratories/'
CMS_STORAGE_LABORATORIES_AREAS_API = 'laboratoriesareas/'
CMS_STORAGE_LABORATORIES_SCOPES_API = 'laboratories-scopes/'
CMS_STORAGE_PATENTS_API = 'patents/'
CMS_STORAGE_PENTAHO_API = 'pentaho/'
CMS_STORAGE_PENTAHO_ISODID_API = 'isodid/'
CMS_STORAGE_PHD_ACTIVITIES_API = 'phd-activities-list/'
CMS_STORAGE_PHD_ACTIVITY_TYPOLOGIES_API = 'phd-activity-typologies/'
CMS_STORAGE_PROJECTS_API = 'projects/'
CMS_STORAGE_PROJECTS_PROGRAMS_TYPES_API = 'projects-program-types/'
CMS_STORAGE_PROJECTS_INFRASTRUCTURES_API = 'projects-infrastructures/'
CMS_STORAGE_PROJECTS_TERRITORIAL_SCOPES_API = 'projects-territorial-scopes/'
CMS_STORAGE_PUBLICATIONS_API = 'publications/'
CMS_STORAGE_REF_PHD_API = 'ref-phd/'
CMS_STORAGE_REF_STRUCTURES_API = 'ref-structures/'
CMS_STORAGE_REF_CYCLE_API = 'phd-cycles/'
CMS_STORAGE_REF_SSD_API = 'phd-ssd-list/'
CMS_STORAGE_RESEARCH_GROUP_API = 'researchgroups/'
CMS_STORAGE_ROLES_API = 'roles/'
CMS_STORAGE_SPINOFF_API = 'companies/'
CMS_STORAGE_STRUCTURE_API = 'structures/'
CMS_STORAGE_STRUCTUREFUNCTIONS_API = 'functions/'
CMS_STORAGE_STRUCTURETYPES_API = 'structuretypes/'
CMS_STORAGE_TEACHER_API = 'teachers/'
CMS_STORAGE_TECHAREAS_API = 'tech-areas/'
CMS_STORAGE_TEACHER_NEWS_API = 'news/'



# labels (for breadcrumbs and page title)
CMS_STORAGE_ACTIVITIES_LABEL = _("Teachings")
CMS_STORAGE_ADDRESSBOOK_LABEL = _("Persons")
CMS_STORAGE_APPLIED_RESEARCH_LINE_LABEL = _("Applied research lines")
CMS_STORAGE_BASE_RESEARCH_LINE_LABEL = _("Base research lines")
CMS_STORAGE_CDS_LIST_LABEL = _("Degree courses")
CMS_STORAGE_HIGH_FORMATION_MASTERS_LABEL = _("Masters and Advanced training courses")
CMS_STORAGE_LABORATORY_LABEL = _("Laboratories")
CMS_STORAGE_PATENTS_LABEL = _("Patents")
CMS_STORAGE_PHD_ACTIVITIES_LABEL = _("PhD Activities")
CMS_STORAGE_PROJECTS_LABEL = _("Projects")
CMS_STORAGE_PUBLICATIONS_LABEL = _("Publications")
CMS_STORAGE_RESEARCH_GROUP_LABEL = _("Research groups")
CMS_STORAGE_RESEARCH_LINE_LABEL = _("Research lines")
CMS_STORAGE_ROOT_LABEL = _("Open data")
CMS_STORAGE_SPINOFF_LABEL = _("Companies")
CMS_STORAGE_STRUCTURE_LABEL = _("Structures")
CMS_STORAGE_TEACHERS_LABEL = _("Teachers")
CMS_STORAGE_TEACHER_NEWS_LABEL = _("News")
CMS_STORAGE_ACTIVITIES_LABEL = _("Activities")


# API filters
ALLOWED_CDS_COURSETYPES = []
ALLOWED_CDS_LANGUAGES = ['ita', 'eng']
ALLOWED_HIGH_FORMATION_MASTERS_LANGUAGES = ['italiano', 'inglese']
ALLOWED_CDS_JOINT_DEGREES = [
    {'COD': 'N', 'name': _("No")},
    {'COD': 'S', 'name': _("Joint title")},
    {'COD': 'D', 'name': _("Double title")}
]


ALLOWED_ADDRESSBOOK_ROLES = []
ALLOWED_ADDRESSBOOK_STRUCTURE_ID = []
ALLOWED_STRUCTURE_TYPES = []
ALLOWED_TEACHER_ROLES = []
ROLE_TEACHER_ROLES = []
CONTRACT_TEACHER_ROLES = []

CDS_INFO_FIELDS = [#'CdSGoals',
                   'CdSAccess', 'CdSAdmission',
                   'CdSProfiles',
                   #'CdSFinalTest', 'CdSFinalTestMode',
                   'CdSSatisfactionSurvey',]
CDS_WEBSITE_COURSE_INFO_FIELDS = [#'CdSGoals',
                                  # 'CdSAccess', 'CdSAdmission',
                                  'CdSProfiles',
                                  #'CdSFinalTest', 'CdSFinalTestMode',
                                  'CdSSatisfactionSurvey',]

# FIELDS TO HIDE IN BLOCKS

STUDY_ACTIVITY_INFO_NOT_SHOW = ['StudyActivityName',
                                'StudyActivityCdSID',
                                'StudyActivityRegDidId',
                                'StudyActivityTeacherID',
                                'StudyActivityID',
                                'StudyActivityContent',
                                'StudyActivityProgram',
                                'StudyActivityLearningOutcomes',
                                'StudyActivityMethodology',
                                'StudyActivityEvaluation',
                                'StudyActivityTextbooks',
                                'StudyActivityWorkload',
                                'StudyActivityCdSCod',
                                'StudyActivityCod',
                                'StudyActivityTeachingUnitTypeCod',
                                'StudyActivityInterclassTeachingUnitTypeCod',
                                'StudyActivityCdSName',
                                'StudyActivitiesBorrowedFromThis',
                                'StudyActivityPartitionCod',
                                'StudyActivityExtendedPartitionCod',
                                'StudyActivityExtendedPartitionDes',
                                'StudyActivityPartitionDes',
                                'StudyActivitySSDCod',
                                'StudyActivityFather',
                                'StudyActivityPdsCod',
                                'StudyActivityPdsDes']

ADDRESSBOOK_INFO_NOT_SHOW = ['ID', 'Name', 'Role',
                             'RoleDescription', 'StructureTypeCOD',
                             'TeacherCVFull', 'TeacherCVShort',
                             'StructureCod', 'StructureTypeName',
                             'StructureCod', 'ProfileId', 'ProfileDescription',
                             'ProfileShortDescription']

TEACHER_INFO_NOT_SHOW = ['TeacherID', 'TeacherDepartmentID',
                         'TeacherLastName', 'TeacherFirstName',
                         'TeacherRole', 'TeacherRoleDescription',
                         'TeacherCVFull', 'TeacherCVShort',
                         'TeacherSSDCod',
                         'TeacherDepartmentCod', 'ProfileId', 'ProfileDescription',
                         'ProfileShortDescription', 'ReceptionHours', 'ReceptionHoursEn',
                         'CVPathIta', 'CVPathEn', 'ShortBio', 'ShortBioEn', 'PhotoPath']

STRUCTURE_INFO_NOT_SHOW = ['StructureId', 'StructureCod', 'StructureFatherId',
                           'StructureTypeCOD', 'StructurePersonnelFunctions',
                           'StructureName']

LABORATORY_INFO_NOT_SHOW = ['LaboratoryId', 'CompletionReferentId',
                            'ScientificDirectorId', 'DepartmentReferentId',
                            'LaboratoryErc1Cod', 'LaboratoryErc0Cod',
                            'ResearchPersonnelID', 'TechPersonnelID',
                            'LaboratoryName',
                            'LaboratoryScope', 'LaboratoryLogo',
                            'LaboratoryResearchPersonnel',
                            'LaboratoryTechPersonnel', 'LaboratoryOfferedServices',
                            'LaboratoryServicesScope', 'LaboratoryTeachingScope',
                            'LaboratoryResearchScope', 'LaboratoryActivities',
                            'CompletionReferentName', 'TechPersonnelRole',
                            'ExtraDepartments','LaboratoryEquipment',
                            'Interdepartmental', 'DepartmentReferentCod',
                            'InfrastructureId', 'LaboratoryAcronym',
                            'Visible','ScientificDirectorEmail']

PUBLICATIONS_INFO_NOT_SHOW = ['PublicationId', 'PublicationAbstract',
                              'PublicationTitle', 'PublicationCommunity',
                              'PublicationCollection', 'PublicationReferenceAuthor',
                              'Publication', 'PublicationLabel', 'PublicationUrl']

PROJECTS_INFO_NOT_SHOW = ['ProjectId', 'ProjectDepartmentId',
                          'TerritorialScopeId', 'TypeProgramId',
                          'TechAreaId', 'ProjectTitle',
                          'ProjectDescription', 'ProjectAbstract',
                          'ProjectImage', 'InfrastructureId', 'IsActive']

PROJECTS_PRIN_BANNER_URL = "https://www.unical.it/media/medias/2024/TESTATA_PNRR_PER_UNICAL_ok.webp"

INITIAL_STRUCTURE_FATHER = ''

SPINOFF_INFO_NOT_SHOW = ['SpinoffId', 'SpinoffImage', 'SpinoffTechAreaId',
                         'IsSpinoff', 'IsStartup', 'SpinoffAgencyName',
                         'SpinoffUnicalReferentId', 'SpinoffDescription',
                         'TechAreaId', 'IsActive']

HIGH_FORMATION_MASTERS_INFO_NOT_SHOW = ['ID', 'HighFormationTypeId',
                                        'HighFormationErogationMode']

PHD_ACTIVITIES_INFO_NOT_SHOW = ['ID']

EXCLUDE_STUDY_ACTIVITIES_CODES = []
EXCLUDE_STUDY_ACTIVITIES_ID = []

ADDRESSBOOK_SPECIAL_ROLES = []

# ALMALAUREA Link
ALMALAUREA_LINK = 'http://statistiche.almalaurea.it/universita/statistiche/trasparenza?codicione='

# CURRENT ACADEMIC YEAR
CURRENT_YEAR = ""

# HIGH FORMATION ACADEMIC YEAR
HIGH_FORMATION_YEAR = ""

# DIDACTIC REGULATION YEAR
DIDACTIC_REGULATION_START_YEAR = datetime.datetime.now().year

# DIDACTIC REGULATION YEAR
TEACHING_SYSTEM_START_YEAR = datetime.datetime.now().year

# DIDACTIC REGULATION YEAR
TEACHING_SYSTEM_START_YEAR = ""

# breadcrumb last item class
BREADCRUMB_ITEM = "breadcrumb-item"
BREADCRUMB_LAST = f"{BREADCRUMB_ITEM} active"

# HIGH FORMATION LINKS
HIGH_FORMATION_MASTERS_LINK = 'https://unical.portaleamministrazionetrasparente.it/pagina874_tc-9_master.html'
HIGH_FORMATION_COURSES_LINK = 'https://unical.portaleamministrazionetrasparente.it/pagina874_tc-6_corsi-di-formazioneperfezionamento.html'


############# CDS WEBSITES ###################

# CMS_WEBPATH_CDS = {} # {id_webpath: cds_cod}
# CMS_WEBPATH_CDS_OLD = {} # {cds_cod: last_year, 2022: [], 2021: []}
# CMS_WEBPATH_CDS_MORPH = {} #'0825': ['0762','0761']
CMS_WEBPATH_PROSPECT = {} # {'L': 12, 'LM': 23, 'LM5': 12, ...} webpath id to nest prospect pages
CMS_WEBPATH_PROSPECT_DEFAULT = None # default webpath id to nest prospect pages
CMS_STORAGE_CDS_WEBSITES_BASE_PATH = 'cds'

# paths
CMS_STORAGE_CDS_WEBSITES_REDIRECT_VIEW_PREFIX_PATH = 'redirect'
CMS_STORAGE_CDS_WEBSITES_PROSPECT_VIEW_PREFIX_PATH = 'brochure'
CMS_STORAGE_CDS_WEBSITES_CORSO_VIEW_PREFIX_PATH = 'corso'
CMS_STORAGE_CDS_WEBSITES_ISCRIVERSI_VIEW_PREFIX_PATH = 'iscriversi'
CMS_STORAGE_CDS_WEBSITES_OPPORTUNITA_VIEW_PREFIX_PATH = 'opportunita'
CMS_STORAGE_CDS_WEBSITES_ORGANIZZAZIONE_VIEW_PREFIX_PATH = 'organizzazione'
CMS_STORAGE_CDS_WEBSITES_ISODID_VIEW_PREFIX_PATH = 'isodid'
CMS_STORAGE_CDS_WEBSITES_STUDIARE_VIEW_PREFIX_PATH = 'studiare'
CMS_STORAGE_CDS_WEBSITES_STUDIARE_CALENDAR_VIEW_PREFIX_PATH = 'calendario-esami'
CMS_STORAGE_CDS_WEBSITES_STUDIARE_SCHEDULE_VIEW_PREFIX_PATH = 'orario-lezioni'

# regexps
CMS_STORAGE_CDS_WEBSITES_CORSO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_CDS_WEBSITES_BASE_PATH})/({CMS_STORAGE_CDS_WEBSITES_CORSO_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_CDS_WEBSITES_CORSO_ACTIVITY_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_CDS_WEBSITES_BASE_PATH})/({CMS_STORAGE_CDS_WEBSITES_CORSO_VIEW_PREFIX_PATH})/{CMS_STORAGE_ACTIVITY_VIEW_PREFIX_PATH}/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
CMS_STORAGE_CDS_WEBSITES_ISCRIVERSI_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_CDS_WEBSITES_BASE_PATH})/({CMS_STORAGE_CDS_WEBSITES_ISCRIVERSI_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_CDS_WEBSITES_OPPORTUNITA_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_CDS_WEBSITES_BASE_PATH})/({CMS_STORAGE_CDS_WEBSITES_OPPORTUNITA_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_CDS_WEBSITES_ORGANIZZAZIONE_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_CDS_WEBSITES_BASE_PATH})/({CMS_STORAGE_CDS_WEBSITES_ORGANIZZAZIONE_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_CDS_WEBSITES_PROSPECT_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_CDS_WEBSITES_BASE_PATH})/(?P<cds_cod>[0-9]*)-(?P<cds_name>[\/a-z0-9\.\-\_]*)/({CMS_STORAGE_CDS_WEBSITES_PROSPECT_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_CDS_WEBSITES_ISODID_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_CDS_WEBSITES_BASE_PATH})/({CMS_STORAGE_CDS_WEBSITES_ISODID_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_CDS_WEBSITES_REDIRECT_ACTIVITY_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_CDS_WEBSITES_BASE_PATH})/(?P<cds_cod>[0-9]*)/(?P<sub_path>[\/a-z0-9\.\-\_]*)/{CMS_STORAGE_ACTIVITY_VIEW_PREFIX_PATH}/(?P<code>[a-z0-9\-]*)/({CMS_STORAGE_CDS_WEBSITES_REDIRECT_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_CDS_WEBSITES_REDIRECT_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_CDS_WEBSITES_BASE_PATH})/(?P<cds_cod>[0-9]*)/({CMS_STORAGE_CDS_WEBSITES_REDIRECT_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_CDS_WEBSITES_REDIRECT_PROSPECT_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_CDS_WEBSITES_BASE_PATH})/(?P<cds_cod>[0-9]*)/({CMS_STORAGE_CDS_WEBSITES_REDIRECT_VIEW_PREFIX_PATH})/{CMS_STORAGE_CDS_WEBSITES_PROSPECT_VIEW_PREFIX_PATH}(/)?$' # noqa
CMS_STORAGE_CDS_WEBSITES_STUDIARE_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_CDS_WEBSITES_BASE_PATH})/({CMS_STORAGE_CDS_WEBSITES_STUDIARE_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_CDS_WEBSITES_STUDIARE_ACTIVITY_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_CDS_WEBSITES_BASE_PATH})/({CMS_STORAGE_CDS_WEBSITES_STUDIARE_VIEW_PREFIX_PATH})/{CMS_STORAGE_ACTIVITY_VIEW_PREFIX_PATH}/(?P<code>[a-z0-9\-]*)(/)?$' # noqa
CMS_STORAGE_CDS_WEBSITES_STUDIARE_CALENDAR_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_CDS_WEBSITES_BASE_PATH})/({CMS_STORAGE_CDS_WEBSITES_STUDIARE_VIEW_PREFIX_PATH})/{CMS_STORAGE_CDS_WEBSITES_STUDIARE_CALENDAR_VIEW_PREFIX_PATH}(/)?$' # noqa
CMS_STORAGE_CDS_WEBSITES_STUDIARE_SCHEDULE_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_CDS_WEBSITES_BASE_PATH})/({CMS_STORAGE_CDS_WEBSITES_STUDIARE_VIEW_PREFIX_PATH})/{CMS_STORAGE_CDS_WEBSITES_STUDIARE_SCHEDULE_VIEW_PREFIX_PATH}(/)?$' # noqa

CMS_STORAGE_HANDLERS_PATHS += [
                                CMS_STORAGE_CDS_WEBSITES_CORSO_URL_VIEW_REGEXP,
                                CMS_STORAGE_CDS_WEBSITES_CORSO_ACTIVITY_URL_VIEW_REGEXP,
                                CMS_STORAGE_CDS_WEBSITES_ISCRIVERSI_URL_VIEW_REGEXP,
                                CMS_STORAGE_CDS_WEBSITES_OPPORTUNITA_URL_VIEW_REGEXP,
                                CMS_STORAGE_CDS_WEBSITES_ORGANIZZAZIONE_URL_VIEW_REGEXP,
                                CMS_STORAGE_CDS_WEBSITES_ISODID_URL_VIEW_REGEXP,
                                CMS_STORAGE_CDS_WEBSITES_REDIRECT_URL_VIEW_REGEXP,
                                CMS_STORAGE_CDS_WEBSITES_STUDIARE_URL_VIEW_REGEXP,
                                CMS_STORAGE_CDS_WEBSITES_STUDIARE_ACTIVITY_URL_VIEW_REGEXP,
                                CMS_STORAGE_CDS_WEBSITES_STUDIARE_CALENDAR_URL_VIEW_REGEXP,
                                CMS_STORAGE_CDS_WEBSITES_STUDIARE_SCHEDULE_URL_VIEW_REGEXP,
                                CMS_STORAGE_CDS_WEBSITES_PROSPECT_URL_VIEW_REGEXP,
                                CMS_STORAGE_CDS_WEBSITES_REDIRECT_ACTIVITY_URL_VIEW_REGEXP
                              ]

CMS_STORAGE_APP_REGEXP_URLPATHS['unicms_unical_storage_handler.handlers.CdsWebsitesCorsoHandler'] = CMS_STORAGE_CDS_WEBSITES_CORSO_URL_VIEW_REGEXP
CMS_STORAGE_APP_REGEXP_URLPATHS['unicms_unical_storage_handler.handlers.CdsWebsitesCorsoActivityHandler'] = CMS_STORAGE_CDS_WEBSITES_CORSO_ACTIVITY_URL_VIEW_REGEXP
CMS_STORAGE_APP_REGEXP_URLPATHS['unicms_unical_storage_handler.handlers.CdsWebsitesIscriversiHandler'] = CMS_STORAGE_CDS_WEBSITES_ISCRIVERSI_URL_VIEW_REGEXP
CMS_STORAGE_APP_REGEXP_URLPATHS['unicms_unical_storage_handler.handlers.CdsWebsitesOpportunitaHandler'] = CMS_STORAGE_CDS_WEBSITES_OPPORTUNITA_URL_VIEW_REGEXP
CMS_STORAGE_APP_REGEXP_URLPATHS['unicms_unical_storage_handler.handlers.CdsWebsitesOrganizzazioneHandler'] = CMS_STORAGE_CDS_WEBSITES_ORGANIZZAZIONE_URL_VIEW_REGEXP
CMS_STORAGE_APP_REGEXP_URLPATHS['unicms_unical_storage_handler.handlers.CdsWebsitesProspectHandler'] = CMS_STORAGE_CDS_WEBSITES_PROSPECT_URL_VIEW_REGEXP
CMS_STORAGE_APP_REGEXP_URLPATHS['unicms_unical_storage_handler.handlers.CdsWebsitesIsodidHandler'] = CMS_STORAGE_CDS_WEBSITES_ISODID_URL_VIEW_REGEXP
CMS_STORAGE_APP_REGEXP_URLPATHS['unicms_unical_storage_handler.handlers.CdsWebsitesRedirectHandler'] = CMS_STORAGE_CDS_WEBSITES_REDIRECT_URL_VIEW_REGEXP
CMS_STORAGE_APP_REGEXP_URLPATHS['unicms_unical_storage_handler.handlers.CdsWebsitesStudyActivityRedirectHandler'] = CMS_STORAGE_CDS_WEBSITES_REDIRECT_ACTIVITY_URL_VIEW_REGEXP
CMS_STORAGE_APP_REGEXP_URLPATHS['unicms_unical_storage_handler.handlers.CdsWebsitesRedirectProspectHandler'] = CMS_STORAGE_CDS_WEBSITES_REDIRECT_PROSPECT_URL_VIEW_REGEXP
CMS_STORAGE_APP_REGEXP_URLPATHS['unicms_unical_storage_handler.handlers.CdsWebsitesStudiareHandler'] = CMS_STORAGE_CDS_WEBSITES_STUDIARE_URL_VIEW_REGEXP
CMS_STORAGE_APP_REGEXP_URLPATHS['unicms_unical_storage_handler.handlers.CdsWebsitesStudiareActivityHandler'] = CMS_STORAGE_CDS_WEBSITES_STUDIARE_ACTIVITY_URL_VIEW_REGEXP
CMS_STORAGE_APP_REGEXP_URLPATHS['unicms_unical_storage_handler.handlers.CdsWebsitesStudiareCalendarHandler'] = CMS_STORAGE_CDS_WEBSITES_STUDIARE_CALENDAR_URL_VIEW_REGEXP
CMS_STORAGE_APP_REGEXP_URLPATHS['unicms_unical_storage_handler.handlers.CdsWebsitesStudiareScheduleHandler'] = CMS_STORAGE_CDS_WEBSITES_STUDIARE_SCHEDULE_URL_VIEW_REGEXP

# APIs
CMS_STORAGE_CDS_BROCHURES_API = 'cds-brochures/'
CMS_STORAGE_CDS_WEBSITES_API = 'cds-websites/'
CMS_STORAGE_CDS_WEBSITES_TOPICS_API = 'cds-websites-topic/'
CMS_STORAGE_CDS_WEBSITES_TOPIC_ARTICLES_API = 'cds-websites-topic-articles/'
CMS_STORAGE_CDS_WEBSITES_STUDYPLANS_API = 'cds-websites-studyplans/'

# labels (for breadcrumbs and page title)
CMS_STORAGE_CDS_WEBSITES_CORSO_LABEL = _("The Course")
CMS_STORAGE_CDS_WEBSITES_ISCRIVERSI_LABEL = _("Enroll")
CMS_STORAGE_CDS_WEBSITES_OPPORTUNITA_LABEL = _("Opportunities")
CMS_STORAGE_CDS_WEBSITES_ORGANIZZAZIONE_LABEL = _("Organization")
CMS_STORAGE_CDS_WEBSITES_PROSPECT_LABEL = _("Brochure")
CMS_STORAGE_CDS_WEBSITES_ISODID_LABEL = _("Student opinions survey")
CMS_STORAGE_CDS_WEBSITES_STUDIARE_LABEL = _("Study")
CMS_STORAGE_CDS_WEBSITES_STUDIARE_CALENDAR_LABEL = _("Exam calendar")
CMS_STORAGE_CDS_WEBSITES_STUDIARE_SCHEDULE_LABEL = _("Class schedule")

CMS_STORAGE_CDS_WEBSITES_PAGE_TOPICS = {}

CMS_STORAGE_CDS_WEBSITE_PROSPECT_COLLAPSE_FIELDS = [
    #'CDSAdmission',
    'CDSGoals',
    'CDSJobOpportunities'
]

CMS_STORAGE_CDS_WEBSITE_PROSPECT_COLLAPSE_FIELDS_2 = [
    'CDSTaxes',
    'CDSScholarships',
    'CDSConcessions'
]

CMS_STORAGE_CDS_WEBSITE_BROCHURE_IS_VISIBLE = True

CMS_STORAGE_CDS_WEBSITE_PROSPECT_DOCS = {
    # 'it': [
        # (
            # 'Regolamento tasse',
            # 'https://www.unical.it/media/medias/2023/Regolamento_tasse_contributi_ed_esoneri.pdf'
        # ),
        # (
            # 'Guida Esse3',
            # 'https://unical.esse3.cineca.it/Home.do'
        # )
        # '0773': [
            # (
                # 'Guida corso',
                # 'https://unical.esse3.cineca.it/Home.do'
            # )
        # ],
    # ],
    # 'en': [
        # (
            # 'Tax regulation',
            # '#'
        # ),
        # (
            # 'Esse3 guide',
            # '#'
        # ),
        # '0773': [
            # (
                # 'Course guide',
                # 'https://unical.esse3.cineca.it/Home.do'
            # )
        # ],
    # ]
}

CMS_STORAGE_CDS_WEBSITES_CAROUSEL_BACKGROUNDS_URL = {
    "Socio-Economica": "cover-area-socio-economica.jpg",
    "Umanistica": "cover-area-umanistica.jpg",
    "Scienze": "cover-area-scienze.jpg",
    "Ingegneria e Tecnologia": "cover-area-ingegneria-tecnologica.jpg",
    "Medico Sanitaria": "cover-area-medico-sanitaria.jpg",
    "Formazione di Educatori e Insegnanti": "cover-area-formazione-insegnanti.jpg",
    # eng
    "Socio-Economics": "cover-area-socio-economica.jpg",
    "Humanities": "cover-area-umanistica.jpg",
    "Sciences": "cover-area-scienze.jpg",
    "Engineering and Technology": "cover-area-ingegneria-tecnologica.jpg",
    "Medical and Health-care": "cover-area-medico-sanitaria.jpg",
    "Training of Educators and Teachers": "cover-area-formazione-insegnanti.jpg",
}

CDS_WEBSITE_CURRENT_YEAR = ""
CDS_WEBSITE_PROSPECT_CURRENT_YEAR = ""

CMS_STORAGE_CDS_WEBSITE_PROSPECT_EMAIL_RECIPIENTS = []
CMS_STORAGE_CDS_WEBSITE_PROSPECT_EMAIL_BCC_RECIPIENTS = []

CDS_STORAGE_CDS_WEBSITE_CAPTCHA_AUDIO = False

CDS_STORAGE_CDS_WEBSITE_INTERNATIONAL_CDS_TO_EXCLUDE = []

CDS_STORAGE_CDS_WEBSITE_DEFAULT_IMAGE = None

PENTAHO_ISODID_REPORT_START_YEAR = ""
PENTAHO_ISODID_REPORT_END_YEAR = ""
