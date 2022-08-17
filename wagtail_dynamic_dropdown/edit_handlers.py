from .widgets import DynamicDropdownWidget
from wagtail.admin.edit_handlers import FieldPanel

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
            self.field_name: DynamicDropdownWidget(dynamic_choices=self.dynamic_choices),
        }
