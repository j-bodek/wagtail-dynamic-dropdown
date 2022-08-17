from django.urls import include, path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls

urlpatterns = [
    path("backend/", include(wagtailadmin_urls)),
    path("", include(wagtail_urls)),
]