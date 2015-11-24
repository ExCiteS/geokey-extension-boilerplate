from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin


class IndexPage(LoginRequiredMixin, TemplateView):

    template_name = 'ext_index.html'

    def get_context_data(self, *args, **kwargs):
        return super(IndexPage, self).get_context_data(
            name='My Awesome Extension',
            *args,
            **kwargs
        )
