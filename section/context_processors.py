from django.core import urlresolvers
from django.core.urlresolvers import Resolver404
from django.conf import settings
from django.utils.encoding import smart_str

def resolve_pattern_name(resolver, path):
    tried = []
    match = resolver.regex.search(path)
    if match:
        new_path = path[match.end():]
        for pattern in resolver.url_patterns:
            try:
                sub_match = pattern.resolve(new_path)
            except Resolver404, e:
                sub_tried = e.args[0].get('tried')
                if sub_tried is not None:
                    tried.extend([(pattern.regex.pattern + '   ' + t) for t in sub_tried])
                else:
                    tried.append(pattern.regex.pattern)
            else:
                if sub_match:
                    sub_match_dict = dict([(smart_str(k), v) for k, v in match.groupdict().items()])
                    sub_match_dict.update(resolver.default_kwargs)
                    for k, v in sub_match[2].iteritems():
                        sub_match_dict[smart_str(k)] = v
                    try:
                        return pattern.name
                    except AttributeError:
                        return resolve_pattern_name(pattern, new_path)
                tried.append(pattern.regex.pattern)
        raise Resolver404, {'tried': tried, 'path': new_path}
    raise Resolver404, {'path' : path}

def section(request):
    """
    Determines the current site section from resolved view pattern and adds
    it to context['section']. Section defaults to the first specified section.
    """
    # if SECTIONS setting is not specified, don't do anything
    try:
        sections = settings.SECTIONS
    except AttributeError:
        return {}

    section = sections[0]['name']
   
    # get resolver and path
    urlconf = getattr(request, "urlconf", settings.ROOT_URLCONF)
    resolver = urlresolvers.RegexURLResolver(r'^/', urlconf)
    path = request.path_info

    # resolve pattern name
    pattern_name = resolve_pattern_name(resolver, path)

    for option in settings.SECTIONS:
        if pattern_name in option['matching_pattern_names']:
            section = option['name']

    return {'section': section}
