from .widgets import DynamicDropdownWidget
from wagtail.admin.panels import FieldPanel


class DynamicDropdownPanel(FieldPanel):
    def __init__(self, field_name, dynamic_choices, *args, **kwargs):
        super().__init__(field_name, *args, **kwargs)
        self.dynamic_choices = dynamic_choices

    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        kwargs.update(
            dynamic_choices=self.dynamic_choices,
        )
        return kwargs

    def widget_overrides(self):
        return {
            self.field_name: DynamicDropdownWidget(
                dynamic_choices=self.dynamic_choices
            ),
        }

    def get_form_options(self):
        """
        Return a dictionary of attributes such as 'fields', 'formsets' and 'widgets'
        which should be incorporated into the form class definition to generate a form
        that this panel can use.
        This will only be called after binding to a model (i.e. self.model is available).
        """
        options = super().get_form_options()
        options["widgets"] = {
            self.field_name: DynamicDropdownWidget(
                dynamic_choices=self.dynamic_choices
            ),
        }
        return options
