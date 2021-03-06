"""Admin classes for the ``document_library`` app."""
from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline
from django.utils.translation import ugettext_lazy as _

from cms.admin.placeholderadmin import PlaceholderAdmin
from hvad.admin import TranslatableAdmin

from .models import Attachment, Document, DocumentCategory


class MulilingualModelAdmin(TranslatableAdmin, PlaceholderAdmin):
    pass


class AttachmentInline(GenericTabularInline):
    model = Attachment
    extra = 1
    raw_id_fields = ['document', ]


class DocumentAdmin(MulilingualModelAdmin):
    """Admin class for the ``Document`` model."""
    list_display = [
        'get_title', 'category', 'position', 'user', 'is_on_front_page',
        'all_translations', 'get_is_published',
    ]

    def get_title(self, obj):
        return obj.title
    get_title.short_description = _('Title')

    def get_is_published(self, obj):
        return obj.is_published
    get_is_published.short_description = _('Is published')
    get_is_published.boolean = True


class DocumentCategoryAdmin(MulilingualModelAdmin):
    """Admin class for the ``DocumentCategory`` model."""
    list_display = ['get_title', 'all_translations', 'is_published']

    def get_title(self, obj):
        return obj.title
    get_title.short_description = _('Title')


admin.site.register(Document, DocumentAdmin)
admin.site.register(DocumentCategory, DocumentCategoryAdmin)
