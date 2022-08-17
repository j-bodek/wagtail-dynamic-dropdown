from django.test import TestCase
from wagtail.tests.utils import WagtailTestUtils
import random

from wagtail_dynamic_dropdown.widgets import DynamicDropdownWidget
from tests.testapp import dynamic_functions

class WidgetTest(TestCase, WagtailTestUtils):
    
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

    def test_dynamic_dropdown_with_function(self):
        self.dynamic_list = [(random.randrange(10), random.randrange(10)) for i in range(5)]
        function = self.dynamic_list_function
        DynamicDropdown = DynamicDropdownWidget(dynamic_choices=function)
        self.assertEqual(DynamicDropdown.choices, self.dynamic_list)

        function = self.static_list_function
        DynamicDropdown = DynamicDropdownWidget(dynamic_choices=function)
        self.assertEqual(DynamicDropdown.choices, self.static_list)

    def test_specify_function_path(self):
        dynamic_functions.DYNAMIC_LIST = [(random.randrange(10), random.randrange(10)) for i in range(5)]
        DynamicDropdown = DynamicDropdownWidget(dynamic_choices="tests.testapp.dynamic_functions.return_dynamic_list")
        self.assertEqual(DynamicDropdown.choices, dynamic_functions.DYNAMIC_LIST)

        DynamicDropdown = DynamicDropdownWidget(dynamic_choices="tests.testapp.dynamic_functions.return_static_list")
        self.assertEqual(DynamicDropdown.choices, self.static_list)