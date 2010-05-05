from setuptools import setup, find_packages

setup(
    name='django-section',
    version='dev',
    description='Django app for determining site section by request.',
    author='Praekelt Consulting',
    author_email='dev@praekelt.com',
    url='http://github.com/praekelt/django-section',
    packages = find_packages(),
    include_package_data=True,
)
