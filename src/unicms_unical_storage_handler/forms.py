from django import forms
from django.contrib import admin
from django.contrib.admin import widgets
from django.utils.translation import gettext_lazy as _

from django_form_builder.forms import BaseDynamicForm
from django_form_builder import dynamic_fields

from cms.templates.models import PageTemplate

from . models import WebPathCdsCod


class CdsWebsiteCreationYear(forms.Form):
    api_source = forms.URLField(required=True, help_text='Es: https://storage.portale.unical.it/api/ricerca/cds/?page_size=300&coursetype=L,LM5,LM6&academicyear=2024')
    webpath = forms.CharField(widget=widgets.ForeignKeyRawIdWidget(
                                rel=WebPathCdsCod._meta.get_field('webpath').remote_field,
                                admin_site=admin.site,
                             ), required=True)
    template = forms.ModelChoiceField(queryset=PageTemplate.objects.filter(), required=True)


class CdsWebsiteContactForm(forms.Form):
    first_name = forms.CharField(label=_('First name'), required=True)
    last_name = forms.CharField(label=_('Last name'), required=True)
    email = forms.EmailField(label=_('E-mail'), required=True)
    phone = forms.CharField(label=_('Telephone'), required=True)
    message = forms.CharField(label=_('Message'), required=True, widget=forms.Textarea(attrs={"rows":"11"}))
    privacy = forms.BooleanField(label=_("Preso atto dell'informativa di cui all' art. 13 del GDPR EU 2016/679"), required=True)


class DynCdsWebsiteContactForm(BaseDynamicForm):
    """ """

    def __init__(self, constructor_dict={}, custom_params={}, *args, **kwargs):

        self.initial_fields = {}
        self.final_fields = {}

        first_name_id = dynamic_fields.format_field_name('first_name')
        first_name_data = {
            "required": True,
            "label": _('Name'),
            "help_text": '',
            "initial": '',
        }
        first_name_field = getattr(
            dynamic_fields, "CustomCharField")(**first_name_data)
        self.initial_fields[first_name_id] = first_name_field

        last_name_id = dynamic_fields.format_field_name('last_name')
        last_name_data = {
            "required": True,
            "label": _('Surname'),
            "help_text": '',
            "initial": '',
        }
        last_name_field = getattr(
            dynamic_fields, "CustomCharField")(**last_name_data)
        self.initial_fields[last_name_id] = last_name_field

        email_id = dynamic_fields.format_field_name('email')
        email_data = {
            "required": True,
            "label": _('Email'),
            "help_text": '',
            "initial": '',
        }
        email_field = getattr(
            dynamic_fields, "CustomEmailField")(**email_data)
        self.initial_fields[email_id] = email_field

        phone_id = dynamic_fields.format_field_name('phone')
        phone_data = {
            "required": True,
            "label": _('Phone'),
            "help_text": '',
            "initial": '',
        }
        phone_field = getattr(
            dynamic_fields, "CustomCharField")(**phone_data)
        self.initial_fields[phone_id] = phone_field

        message_id = dynamic_fields.format_field_name('message')
        message_data = {
            "required": True,
            "label": _('Message'),
            "help_text": '',
            "initial": '',
        }
        message_field = getattr(
            dynamic_fields, "TextAreaField")(**message_data)
        self.initial_fields[message_id] = message_field
        self.initial_fields[message_id].widget = forms.Textarea(attrs={"rows": 11})

        privacy_id = dynamic_fields.format_field_name('privacy')
        privacy_data = {
            "required": True,
            "label": _("I have taken note of the information referred to in art. 13 of the GDPR EU 2016/679"),
            "help_text": '',
            "initial": '',
        }
        privacy_field = getattr(
            dynamic_fields, "CheckBoxField")(**privacy_data)
        self.initial_fields[privacy_id] = privacy_field

        captcha_data = {
            "label": _('Verification code'),
            "captcha_name": dynamic_fields.format_field_name('captcha'),
            "captcha_hidden_name": dynamic_fields.format_field_name(
                'hidden_captcha'
            ),
        }
        captcha_field = getattr(dynamic_fields, "CustomCaptchaComplexField")(
            **captcha_data
        )
        captcha_field.define_value(custom_value="", **custom_params)
        for single_field in captcha_field.get_fields():
            self.final_fields[single_field.name] = single_field

        super().__init__(
            initial_fields=self.initial_fields,
            final_fields=self.final_fields,
            constructor_dict=constructor_dict,
            custom_params=custom_params,
            *args,
            **kwargs
        )
