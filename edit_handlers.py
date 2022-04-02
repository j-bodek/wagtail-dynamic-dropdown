from .widgets import DynamicDropdownWidget
from wagtail.admin.edit_handlers import FieldPanel

class DynamicDropdownPanel(FieldPanel):

    def __init__(self, field_name, dynamic_choices, *args, **kwargs):
        widget = kwargs.pop('widget', None)
        if widget is not None:
            self.widget = widget
        self.comments_enabled = not kwargs.pop('disable_comments', False)
        super(FieldPanel, self).__init__(*args, **kwargs)
        self.field_name = field_name
        self.dynamic_choices = dynamic_choices

    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        kwargs.update(
            field_name=self.field_name,
            dynamic_choices=self.dynamic_choices,
            widget=self.widget if hasattr(self, 'widget') else None,
        )
        return kwargs

    def widget_overrides(self):
        return {
            self.field_name: DynamicDropdownWidget(dynamic_choices=self.dynamic_choices),
        }
