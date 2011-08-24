import unittest

from django.conf import settings
from django.test.client import RequestFactory

from section import context_processors


class ContextProcessorsTestCase(unittest.TestCase):
    def test_section(self):
        # Without SECTIONS setting result should be empty.
        request = RequestFactory().get('/some/url/')
        context = context_processors.section(request)
        self.failIf(context)

        # With SECTIONS setting not containing section for requested path
        # result should be first defined section.
        settings.SECTIONS = (
            {'name': 'first', 'matching_pattern_names': ('undefined',)},
            {'name': 'match', 'matching_pattern_names': (\
                'matched_section', 'matched_section_with_second_path',)},
        )
        context = context_processors.section(request)
        self.failUnlessEqual(context['section'], 'first')

        # With SECTIONS setting containing section for requested path
        # result should be matched name.
        request = RequestFactory().get('/some/other/url/')
        context = context_processors.section(request)
        self.failUnlessEqual(context['section'], 'match')

        # With SECTIONS setting containing section for multiple paths
        # result should be matched name.
        request = RequestFactory().get('/some/other/matching/url/')
        context = context_processors.section(request)
        self.failUnlessEqual(context['section'], 'match')
