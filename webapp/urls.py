# Modules
from django.conf.urls import url
from django_yaml_redirects import load_redirects
from django_template_finder_view import TemplateFinder
from canonicalwebteam.gsa.views import SearchView

# Local
from webapp.views import custom_404, custom_500

# Match any redirects first
urlpatterns = load_redirects()

# Try to find templates
urlpatterns += [
    url(r'^search/?$', SearchView.as_view(template_name='search.html')),
    url(r'^(?P<template>.*)/?$', TemplateFinder.as_view())
]

# Error handlers
handler404 = custom_404
handler500 = custom_500
