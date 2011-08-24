from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'some/url', 'section.tests.views.view', name='unmatched_section'),
    url(r'some/other/url', 'section.tests.views.view', name='matched_section'),
    url(r'some/other/matching/url', 'section.tests.views.view', \
            name='matched_section_with_second_path'),
)
