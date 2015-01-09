from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = 'ext_index.html'

    def get_context_data(self, *args, **kwargs):
        return super(IndexPage, self).get_context_data(
            name='GeoKey Extension',
            *args,
            **kwargs
        )
