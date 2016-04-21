"""All views for the extension."""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin


class IndexPage(LoginRequiredMixin, TemplateView):
    """Main index page."""

    template_name = 'ext_index.html'

    def get_context_data(self, *args, **kwargs):
        """
        GET method for the template.

        Return the context to render the view. Overwrite the method by adding
        the name of my awesome extension to the context.

        Returns
        -------
        dict
            Context.
        """
        return super(IndexPage, self).get_context_data(
            name='My Awesome Extension',
            *args,
            **kwargs
        )
