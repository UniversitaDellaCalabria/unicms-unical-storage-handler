from django.urls import path

from . api_views import *

urlpatterns = []

# cds website topics in settings
urlpatterns += path('api/cds-websites-topics/', UniCMSCdsWebsitesTopics.as_view(), name='cds-websites-topics'),
