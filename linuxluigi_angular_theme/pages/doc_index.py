# Doc index page
from django.db import models
from sphinx.locale import _
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from linuxluigi_angular_theme.streamfield.streamfield import defaultStreamBlock


class DocIndexPage(Page):
    class Meta:
        verbose_name = _('Doc index')

    tagline = models.CharField(max_length=100, blank=True)
    body = StreamField(defaultStreamBlock())

    subpage_types = ['linuxluigi_angular_theme.DocPage']

    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('tagline'),
    ]

    api_fields = ('tagline', 'body')


DocIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('tagline', classname="tagline"),
    StreamFieldPanel('body'),
]

DocIndexPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]
