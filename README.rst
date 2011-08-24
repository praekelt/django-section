Django Section
==============
**Django app for determining site section by request.**

.. contents:: Contents
    :depth: 5

Installation
------------

#. Add ``section.context_processors.section`` to your ``TEMPLATE_CONTEXT_PROCESSORS`` setting::

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...other context processors...,
        "section.context_processors.section",
    )

#. Add ``SECTIONS`` setting to your settings file in the form::

    # Tuple of dictionaries used to match URL pattern names to site sections. 
    # example: ({'name': '<section name>', 'matching_pattern_names': ('<url_name1>', '<url_name2>')},)
    SECTIONS = (
        {'name': 'home', 'matching_pattern_names': ('home',)},
    )

Usage
-----

If you're using generic views or `RequestContext <http://docs.djangoproject.com/en/dev/ref/templates/api/#id1>`_ you'll now automagically have a ``section`` variable added to context and available in your templates containing the value of ``name`` as defined for the current view in your ``SECTIONS`` setting. 

**NOTE**: If the current path can not be resolved to a defined section, the first section as defined in the ``SECTION`` settings is returned. This allows you to setup a global fallback section, i.e. *home*.

