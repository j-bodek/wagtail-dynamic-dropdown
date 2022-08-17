from django.test import TestCase
from wagtail.tests.utils import WagtailTestUtils
import random

from tests.testapp.models import PageWithDynamicList, PageWithStaticList
from tests.testapp import dynamic_functions
from wagtail_dynamic_dropdown.edit_handlers import DynamicDropdownPanel
from wagtail.core.models import Page
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client



class PageTest(TestCase, WagtailTestUtils):

    def setUp(self):
        root_page = Page.objects.get(path='00010001')

        # Create Page with Dynamic List
        self.dynamic_list_page = PageWithDynamicList(title='Dynamic List Page')
        root_page.add_child(instance=self.dynamic_list_page)
        self.dynamic_list_page.save_revision().publish()
        # Create Page with Static List
        self.static_list_page = PageWithStaticList(title='Static List Page')
        root_page.add_child(instance=self.static_list_page)
        self.static_list_page.save_revision().publish()

        # create new superuser
        self.superuser = User.objects.create_superuser(username='superuser', email='superuser@gmail.com')
        self.superuser.set_password('superuser123')
        self.superuser.save()
        # login superuser
        self.logged_in_superuser = Client()
        self.logged_in_superuser.login(username='superuser', password='superuser123')

    def test_page_status_code(self):
        response = self.client.get(self.dynamic_list_page.get_full_url())
        self.assertEqual(response.status_code, 200)
        response = self.client.get(self.static_list_page.get_full_url())
        self.assertEqual(response.status_code, 200)

    def check_edit_page_choices(self, page):
        edit_page_url = f'{reverse("wagtailadmin_home")}pages/{page.id}/edit/'
        response = self.logged_in_superuser.get(edit_page_url)
        self.assertEqual(response.status_code, 200)
        # check rendered choices
        choices = response.context[36]['widget']['optgroups']
        if page.__class__.__name__ == 'PageWithDynamicList':
            self.assertEqual([(x[1][0].get("value"), x[1][0].get("label")) for x in choices], dynamic_functions.DYNAMIC_LIST)
        if page.__class__.__name__ == 'PageStaticList':
            self.assertEqual([(x[1][0].get("value"), x[1][0].get("label")) for x in choices], dynamic_functions.return_static_list())

    def test_edit_page(self):
        self.check_edit_page_choices(self.dynamic_list_page)
        # change dynamic_list
        dynamic_functions.DYNAMIC_LIST = [
            ('choice_1', 'label_1'),
            ('choice_2', 'label_2'),
            ('choice_3', 'label_3'),
        ]
        self.check_edit_page_choices(self.dynamic_list_page)
        # test PageWithStaticList
        self.check_edit_page_choices(self.static_list_page)
    
    def test_can_change_dynamic_dropdown_value(self):
        self.dynamic_list_page.dynamic_list = 'choice_2'
        self.dynamic_list_page.save_revision().publish()
        self.assertEqual(self.dynamic_list_page.dynamic_list, 'choice_2')
        response = self.client.get(self.dynamic_list_page.get_full_url())
        self.assertEqual(response.context.get("self").dynamic_list, "choice_2")
        
