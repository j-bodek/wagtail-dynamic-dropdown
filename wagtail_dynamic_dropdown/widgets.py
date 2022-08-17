from django.forms.widgets import ChoiceWidget
from django.apps import apps
from importlib import import_module
import errno
import os


class DynamicDropdownWidget(ChoiceWidget):

    class Media:
        css = {
            "all": (
                'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.0/font/bootstrap-icons.css',
                "wagtail_dynamic_dropdown/styles/dynamic_dropdown.css",
            )
        }
        js = [
            "wagtail_dynamic_dropdown/js/dynamic_dropdown.js"
        ]


    input_type = 'radio'
    template_name = 'wagtail_dynamic_dropdown/widgets/dynamic_dropdown.html'
    option_template_name = 'wagtail_dynamic_dropdown/widgets/dynamic_dropdown_option.html'

    def __init__(self, attrs=None, dynamic_choices=()):
        super().__init__(attrs)
        # dynamic_choices can be function or path to function
        if type(dynamic_choices).__name__ == 'function' or type(dynamic_choices).__name__ == 'method':
            self.choices = dynamic_choices()
        elif type(dynamic_choices) == str:
            module = import_module(dynamic_choices.rsplit(".",1)[0])
            function = getattr(module, dynamic_choices.rsplit(".",1)[1])
            self.choices = function()

            

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        choices = self.optgroups(name, context['widget']['value'], attrs)
        # If no option is selected, select first as default
        if not any([choice[1][0]['selected'] for choice in choices]):
            choices[0][1][0]['selected'] = True

        context['widget']['optgroups'] = choices
        return context