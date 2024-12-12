from django.conf import settings
from django.db import models

from cms.contexts.models import WebPath
from cms.templates.models import (SectionAbstractModel,
                                  SortableModel,
                                  TemplateBlock)


class WebPathCdsCod(models.Model):
    webpath = models.OneToOneField(WebPath, on_delete=models.CASCADE)
    cds_cod = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return f'{self.webpath.name} - {self.cds_cod}'


class CdsWebsiteHomeBlocks(SectionAbstractModel, SortableModel):
    block = models.ForeignKey(TemplateBlock,
                              limit_choices_to={'is_active': True},
                              on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.block} - {self.section}'
