from django import forms
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class CdsWebsiteContactForm(forms.Form):
    first_name = forms.CharField(label=_('First name'), required=True)
    last_name = forms.CharField(label=_('Last name'), required=True)
    email = forms.EmailField(label=_('E-mail'), required=True)
    phone = forms.CharField(label=_('Telephone'), required=True)
    text = forms.CharField(label=_('Message'), required=True, widget=forms.Textarea(attrs={"rows":"11"}))
