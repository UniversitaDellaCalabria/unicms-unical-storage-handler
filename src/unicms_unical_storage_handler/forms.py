from django import forms
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class CdsWebsiteContactForm(forms.Form):
    first_name = forms.CharField(label=_('First name'), required=True)
    last_name = forms.CharField(label=_('Last name'), required=True)
    email = forms.EmailField(label=_('E-mail'), required=True)
    phone = forms.CharField(label=_('Telephone'), required=True)
    message = forms.CharField(label=_('Message'), required=True, widget=forms.Textarea(attrs={"rows":"11"}))
    privacy = forms.BooleanField(label=_("Preso atto dell'informativa di cui all' art. 13 del GDPR EU 2016/679"), required=True)
