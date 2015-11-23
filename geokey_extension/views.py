from django.views.generic import TemplateView


class IndexPage(TemplateView):

    template_name = 'eb_index.html'

    def get_context_data(self, *args, **kwargs):
        return super(IndexPage, self).get_context_data(
            name='My Awesome Extension',
            *args,
            **kwargs
        )
