from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from wagtail_dynamic_dropdown.edit_handlers import DynamicDropdownPanel
from django import forms


class PageWithDynamicList(Page):
    template = 'testapp/index.html'
    
    dynamic_list = models.CharField(max_length=255, blank=True, null=True)

    content_panels = Page.content_panels + [
        DynamicDropdownPanel('dynamic_list', "tests.testapp.dynamic_functions.return_dynamic_list"),
    ]


class PageWithStaticList(Page):
    template = 'testapp/index.html'
    
    dynamic_list = models.CharField(max_length=255, blank=True, null=True)

    content_panels = Page.content_panels + [
        DynamicDropdownPanel('dynamic_list', "tests.testapp.dynamic_functions.return_static_list"),
    ]

