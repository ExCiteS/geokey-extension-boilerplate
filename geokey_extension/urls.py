"""All URLs for the extension."""

from django.conf.urls import url

from views import IndexPage


urlpatterns = [
    url(
        r'^admin/awesome-extension/$',
        IndexPage.as_view(),
        name='index')
]
