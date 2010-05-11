Django Section
==============
**Django app for determining site section by request.**

Installation
------------

#. Add *section.context_processors.section* to TEMPLATE_CONTEXT_PROCESSORS in your settings file::

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.contrib.messages.context_processors.messages",
        "section.context_processors.section")

#. Add SECTIONS value to your settings file in the form::

    # Tuple of dictionaries used to match URL pattern names to site sections. 
    # example: ({'name': '<section name>', 'matching_pattern_names': ('<url_name1>', '<url_name2>')},)
    SECTIONS = (
        {'name': 'home', 'matching_pattern_names': ('home',)},
    )

Usage
-----

If you're using generic views you'll now automagically have a *section* variable added to context and available in your templates.

Otherwise have a look at RequestContext objects and how to use them:
    
    http://docs.djangoproject.com/en/dev/ref/templates/api/#id1
