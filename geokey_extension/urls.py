from django.conf.urls import patterns, url

from views import IndexPage


urlpatterns = patterns(
    '',
    url(
        r'^admin/awesome-extension/$',
        IndexPage.as_view(),
        name='index')
)
