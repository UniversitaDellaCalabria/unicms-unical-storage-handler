import requests

from django.conf import settings
from django.contrib.sitemaps import GenericSitemap, Sitemap
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.utils import timezone

from cms.contexts.models import WebSite, WebPath
from cms.contexts.settings import SITEMAP_WEBPATHS_PRIORITY
from cms.contexts.views import _get_site_from_host, uniCMSSiteMap

from . settings import *


class AddressbookSitemap(uniCMSSiteMap):
    def items(self):
        addressbook_response = requests.get(f"{settings.CMS_STORAGE_BASE_API}{CMS_STORAGE_ADDRESSBOOK_API}?role={','.join(settings.ALLOWED_ADDRESSBOOK_ROLES)}&page_size=3000")
        if addressbook_response.status_code == 200:
            return addressbook_response.json()['results']
        return {}

    def location(self, obj):
        return f"/{settings.CMS_PATH_PREFIX}{CMS_STORAGE_BASE_PATH}/{CMS_STORAGE_ADDRESSBOOK_API}{obj.get('ID')}/"

    def lastmod(self, obj):
        return None


def rich_unicms_sitemap(request):
    website = _get_site_from_host(request)

    sitemap_dict = {
        'webpath': uniCMSSiteMap(website=website, protocol=request.scheme)
    }

    if website.pk == settings.MAIN_WEBSITE:
        sitemap_dict['addressbook'] = AddressbookSitemap(website=website, protocol=request.scheme)

    sitemaps = sitemap(request, sitemaps=sitemap_dict)
    return HttpResponse(sitemaps.render(), content_type='text/xml')

