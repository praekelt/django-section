from django.conf import settings
from django.core.urlresolvers import Resolver404

from snippetscream import resolve_to_name


def section(request):
    """
    Determines the current site section from resolved view pattern and adds
    it to context['section']. Section defaults to the first specified section.
    """
    # If SECTIONS setting is not specified, don't do anything.
    try:
        sections = settings.SECTIONS
    except AttributeError:
        return {}

    # Default return is first section.
    section = sections[0]['name']

    try:
        pattern_name = resolve_to_name(request.path_info)
    except Resolver404:
        pattern_name = None

    if pattern_name:
        for option in settings.SECTIONS:
            if pattern_name in option['matching_pattern_names']:
                section = option['name']

    return {'section': section}
