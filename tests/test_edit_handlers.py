from django.test import TestCase
from wagtail.tests.utils import WagtailTestUtils
import random
from wagtail_dynamic_dropdown.edit_handlers import DynamicDropdownPanel

class EditHandlersTest(TestCase, WagtailTestUtils):

    def setUp(self):
        self.dynamic_list = []
        self.static_list = [
        ('choice_1','label_1'),
        ('choice_2','label_2'),
        ]

    def dynamic_list_function(self):
        return self.dynamic_list

    def static_list_function(self):
        return self.static_list

    def test_edit_handler_dynamic_list(self):
        self.dynamic_list = [(random.randrange(10), random.randrange(10)) for i in range(5)]
        panel = DynamicDropdownPanel("field", self.dynamic_list_function)
        self.assertIn(type(panel.dynamic_choices).__name__, ['method', 'function'])
        self.assertEqual(panel.dynamic_choices(), self.dynamic_list)

    def test_edit_handler_static_list(self):
        panel = DynamicDropdownPanel("field", self.static_list_function)
        self.assertIn(type(panel.dynamic_choices).__name__, ['method','function'])
        self.assertEqual(panel.dynamic_choices(), self.static_list)

        