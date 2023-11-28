from django.conf import settings

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from . settings import CMS_STORAGE_CDS_WEBSITES_PAGE_TOPICS


class UniCMSCdsWebsitesTopics(APIView):
    """
    """
    description = 'Get storage handler app page topics settings value'
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(getattr(settings,
                                'CMS_STORAGE_CDS_WEBSITES_PAGE_TOPICS',
                                CMS_STORAGE_CDS_WEBSITES_PAGE_TOPICS))
