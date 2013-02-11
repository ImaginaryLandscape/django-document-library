"""django-cms plugin for the ``document_library`` app."""
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from simple_translation.middleware import filter_queryset_language

from document_library.models import Document, DocumentCategory


class DocumentLibraryPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _('Document Library Plugin')
    render_template = "document_library/document_library_plugin.html"

    def render(self, context, instance, placeholder):
        qs = Document.objects.filter(is_published=True)
        qs = filter_queryset_language(context.get('request'), qs)
        context.update({
            'documents': qs,
            'categories': DocumentCategory.objects.all(),
        })
        return context


plugin_pool.register_plugin(DocumentLibraryPlugin)