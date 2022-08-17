Wagtail Dynamic Dropdown
========================

A Django application which allow to use dynamically defined choices that
will be updated every time the user opens edit/create page. Moreover,
the choices are not migrated to the database.

Install
-------

::

   pip install wagtail-dynamic-dropdown==0.0.1

Then add ``wagtail_dynamic_dropdown`` to your installed apps:

::

   INSTALLED_APPS = [
       ...
       'wagtail_dynamic_dropdown'
   ]

Usage
-----

###1. Define function that will return choices

.. code:: python

   def dynamic_choices():
          """
          Choices creation logic
          """
          return choices

This function should return iterable which contains list of touples.
Example of valid choices:

.. code:: python

   choices = (
       ('choice_1','label_1'),
       ('choice_2','label_2')
   )

###2. Use your function with DynamicDropdownPanel

In your model create CharField field. Then pass its name and path to
choice function as arguments in DynamicDropdownPanel

.. code:: python

   from wagtail_dynamic_dropdown.edit_handlers import DynamicDropdownPanel

   class MyModel():
       ...
       my_dynamic_choices = models.CharField(max_length=255, blank=True,null=True)

       content_panels = [
           DynamicDropdownPanel("my_dynamic_choices", "app_name.folder_name.file_name.function_name")
           ]

Or, instead of defining a function path, you can import it and pass it
as an argument

.. code:: python

   from wagtail_dynamic_dropdown.edit_handlers import DynamicDropdownPanel
   from app_name.folder_name.file_name import function_name

   class MyModel():
       ...
       my_dynamic_choices = models.CharField(max_length=255, blank=True,null=True)

       content_panels = [
           DynamicDropdownPanel("my_dynamic_choices", function_name)
           ]
