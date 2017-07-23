# Doc page
from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from sphinx.locale import _
from taggit.models import TaggedItemBase
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from linuxluigi_angular_theme.streamfield.streamfield import defaultStreamBlock


class DocPageTag(TaggedItemBase):
    content_object = ParentalKey('linuxluigi_angular_theme.DocPage', related_name='tagged_items')


class DocPage(Page):
    class Meta:
        verbose_name = _('Doc page')
        verbose_name_plural = _('Doc pages')

    tagline = models.CharField(max_length=100, blank=True)
    tags = ClusterTaggableManager(through=DocPageTag, blank=True)
    body = StreamField(defaultStreamBlock())
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]
    api_fields = ('tagline', 'body', 'tags')


DocPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('tagline', classname="tagline"),
    StreamFieldPanel('body'),
    FieldPanel('tags'),
]

DocPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]
