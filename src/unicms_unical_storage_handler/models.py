from django.conf import settings
from django.db import models

from cms.contexts.models import WebPath


class WebPathCdsCod(models.Model):
    webpath = models.OneToOneField(WebPath, on_delete=models.CASCADE)
    cds_cod = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return f'{ self.webpath.name } - { self.cds_cod }'
