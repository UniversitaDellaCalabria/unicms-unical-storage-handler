import requests

from django.apps import apps
from django.conf import settings
from django.contrib import messages
from django.contrib.admin import ModelAdmin, register, site
from django.db import transaction
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import redirect, reverse
from django.urls import path
from django.utils import timezone
from django.utils.text import slugify
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from cms.contexts.models import WebPath
from cms.pages.models import Page, PageBlock
from cms.templates.models import PageTemplate

from . forms import CdsWebsiteCreationYear
from . models import *


@transaction.atomic
def create_course_websites(request):
    if request.method == "POST":
        form = CdsWebsiteCreationYear(data=request.POST)
        if form.is_valid():
            # retrieve form data
            api_source = form.cleaned_data['api_source']
            api_morph_source = form.cleaned_data['api_morph_source']
            root_id = form.cleaned_data['webpath']
            template = form.cleaned_data['template']
            try:
                # call source api to retrieve courses list
                courses = requests.get(api_source).json()['results']
                # call source api to retrieve morphed courses list
                morphed_courses = requests.get(api_morph_source).json()
                if not courses:
                    messages.success(request, _("No courses to import"))
                else:
                    template = PageTemplate.objects.get(pk=template.pk)
                    root = WebPath.objects.filter(pk=root_id).select_related('site').first()
                    actual_cds_websites = WebPathCdsCod.objects.all().values_list('cds_cod', flat=True)
                    chosen_blocks = CdsWebsiteHomeBlocks.objects.filter()

                    with transaction.atomic():
                        for course in courses:
                            website_found = False
                            if course['CdSCod'] in actual_cds_websites:
                                website_found = True

                            if website_found: continue

                            if morphed_courses.get(course['CdSCod']):
                                for mc in morphed_courses[course['CdSCod']]:
                                    if mc in actual_cds_websites:
                                        website_found = True

                                        cds_website = WebPathCdsCod.objects.filter(cds_cod=mc).select_related('webpath').first()
                                        cds_website.cds_cod = course['CdSCod']
                                        cds_website.save()

                                        cds_webpath = cds_website.webpath
                                        old_path = cds_webpath.path
                                        cds_webpath.path = slugify(course['CdSName'])
                                        cds_webpath.name = course['CdSName']
                                        cds_webpath.save()

                                        cds_webpath_page = Page.objects.filter(webpath=cds_webpath).first()
                                        cds_webpath_page.title = course['CdSName']
                                        cds_webpath_page.name = course['CdSName']
                                        cds_webpath_page.save()

                                        messages.warning(request, f"{_('Updated webpath')} {root}{old_path} in {root}{cds_webpath.path}")

                                        break

                            if not website_found:
                                existent_webpath = WebPath.objects.filter(site=root.site,
                                                                          parent=root,
                                                                          path=f"{slugify(course['CdSName'])}/").exists()
                                # if there is a webpath with same path
                                # append a timestamp to disambiguate
                                p = slugify(course['CdSName'])
                                if existent_webpath:
                                    d = int(timezone.now().timestamp())
                                    wpath = f"{p}-{d}"
                                    messages.warning(request, f"{_('Existent webpath')} {root}{p}: new webpath created with {root}{wpath}")
                                else:
                                    wpath = p

                                webpath = WebPath.objects.create(site=root.site,
                                                                 name=course['CdSName'],
                                                                 parent=root,
                                                                 path=wpath,
                                                                 is_active=True)

                                page = Page.objects.create(webpath=webpath,
                                                           title=webpath.name,
                                                           name=webpath.name,
                                                           date_start=timezone.localtime(),
                                                           base_template=template,
                                                           state='published',
                                                           is_active=True)

                                for cb in chosen_blocks:
                                    PageBlock.objects.create(page=page,
                                                             block=cb.block,
                                                             order=cb.order,
                                                             is_active=cb.is_active,
                                                             section=cb.section)

                                WebPathCdsCod.objects.create(webpath=webpath,
                                                             cds_cod=course['CdSCod'])

                                msg = f"{course['CdSCod']} - {webpath.name} - {_('successfully created')}!"
                                messages.success(request, msg)
            except Exception as e:
                messages.error(request, f"{_('An error occurred')}: {e}")
                raise  # Rilancia l'eccezione per attivare il rollback
            return redirect("admin:unicms_unical_storage_handler_create_course_websites")

    template = 'admin/create_websites_choose_year.html'
    form = CdsWebsiteCreationYear()

    # for admin app label
    current_app_label = __package__.split('.')[0]
    app_config = apps.get_app_config(current_app_label)

    context = {
        **site.each_context(request),
        "title": _("Create course websites starting from the training offer"),
        "breadcrumbs": [
            {"url": reverse("admin:index"), "title": "Pagina iniziale"},
            {"url": reverse("admin:app_list", kwargs={'app_label': current_app_label}), "title": app_config.verbose_name},
            {"url": reverse("admin:unicms_unical_storage_handler_webpathcdscod_changelist"), "title": WebPathCdsCod._meta.verbose_name_plural.capitalize()},
            {"title": _("Create course websites")},
        ],
        "form": form
    }
    return TemplateResponse(request, template, context=context)
