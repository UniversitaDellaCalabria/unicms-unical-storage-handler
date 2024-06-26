import logging

from django import template
from django.conf import settings

from cms.contexts.models import WebPath, WebSite

import unicms_unical_storage_handler.settings as app_settings


logger = logging.getLogger(__name__)
register = template.Library()


ALLOWED_UNICMS_SITES = getattr(settings, 'ALLOWED_UNICMS_SITES',
                               app_settings.ALLOWED_UNICMS_SITES)
CMS_STORAGE_CDS_WEBSITE_PROSPECT_DOCS = getattr(settings, 'CMS_STORAGE_CDS_WEBSITE_PROSPECT_DOCS',
                                                app_settings.CMS_STORAGE_CDS_WEBSITE_PROSPECT_DOCS)


@register.simple_tag
def split_string(s, c):
    result = []
    if not s: return result
    if not c: return result
    l = s.split(c)
    for i in l:
        if i: result.append(i)
    return result


@register.simple_tag
def clean_url(url):
    if url.find('?'): url = url.split('?')[0]
    if url[-1] == '/': return url[:-1]
    return url


@register.simple_tag
def get_cdsid_from_url(url):
    if url.find('?'): url = url.split('?')[0]
    pieces = url.split('/')
    return list(filter(None, pieces))[-1]


@register.simple_tag
def get_allowed_website(host):
    domain_params = host.split(":")
    domain = domain_params[0]
    port = domain_params[1] if len(domain_params)==2 else None
    websites = []
    if '*' in ALLOWED_UNICMS_SITES:
        websites = WebSite.objects.filter(is_active=True)
    else:
        websites = WebSite.objects.filter(pk__in=ALLOWED_UNICMS_SITES,
                                          is_active=True)
    current = websites.filter(domain=domain).first()
    active = current or websites.first()
    if port:
        return f'{active.domain}:{port}'
    return f'{active.domain}'


@register.simple_tag
def get_father_from_url(url):
    import re
    father = re.match('.*father=(.*)', url)
    return None if father is None else father.group(1)


@register.simple_tag
def storage_settings_value(value):
    app_value = getattr(app_settings, value, None)
    return  getattr(settings, value, app_value)


@register.simple_tag
def storage_api_root(value):
    app_root = getattr(app_settings, 'CMS_STORAGE_BASE_API', '')
    settings_root = getattr(settings, 'CMS_STORAGE_BASE_API', app_root)

    app_value = getattr(app_settings, value, '')
    settings_value = getattr(settings, value, app_value)

    return f'{settings_root}{settings_value}'


@register.simple_tag
def get_cds_website_cds_cod(value=None, cds_cod=None):
    if cds_cod: return cds_cod
    if not value: return None
    cms_webpath_cds = getattr(settings, 'CMS_WEBPATH_CDS', {})
    if not cms_webpath_cds: return None
    found = cms_webpath_cds.get(value, None)
    if found: return found
    webpath = WebPath.objects.filter(pk=value).select_related('parent').first()
    if not webpath: return None
    parent = webpath.parent
    if not parent: return None
    return get_cds_website_cds_cod(parent.pk)


@register.simple_tag
def get_cds_website_root_path(webpath=None, cds_cod=None):
    if not cds_cod: return None
    cms_webpath_cds = getattr(settings, 'CMS_WEBPATH_CDS', {})
    if not cms_webpath_cds: return None
    if webpath and cms_webpath_cds.get(webpath.pk) == cds_cod:
        return webpath
    for k,v in cms_webpath_cds.items():
        if v == cds_cod:
            return WebPath.objects.get(pk=k, is_active=True)
    return None


@register.simple_tag
def get_cds_website_current_year(cds_cod):
    current_year = settings.CURRENT_YEAR
    old_year_dict = getattr(settings,
                            'CMS_WEBPATH_CDS_OLD',
                            app_settings.CMS_WEBPATH_CDS_OLD)
    return old_year_dict.get(cds_cod, current_year)


@register.simple_tag
def get_cds_website_new_year(cds_cod):
    current_year = settings.CDS_WEBSITE_CURRENT_YEAR
    old_year_dict = getattr(settings,
                            'CMS_WEBPATH_CDS_OLD',
                            app_settings.CMS_WEBPATH_CDS_OLD)
    return old_year_dict.get(cds_cod, current_year)


@register.simple_tag
def get_cds_website_morph(cds_cod):
    cds_morph = getattr(settings,
                        'CMS_WEBPATH_CDS_MORPH',
                        app_settings.CMS_WEBPATH_CDS_MORPH)
    return cds_morph.get(cds_cod, [])


@register.simple_tag
def get_prospect_docs(lang, cds):
    result = []
    for doc in CMS_STORAGE_CDS_WEBSITE_PROSPECT_DOCS.get(lang, []):
        if isinstance(doc, tuple):
            result.append(doc)
            continue
        cds_docs = doc.get(cds, [])
        for cds_doc in cds_docs:
            result.append(cds_doc)
    return result
