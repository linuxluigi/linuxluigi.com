# Home Page
from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from sphinx.locale import _
from taggit.models import TaggedItemBase
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index

from linuxluigi_angular_theme.streamfield.streamfield import defaultStreamBlock


class HomePageTag(TaggedItemBase):
    content_object = ParentalKey('linuxluigi_angular_theme.HomePage', related_name='tagged_home_items')


class HomePage(Page):
    tags = ClusterTaggableManager(through=HomePageTag, blank=True)
    body = StreamField(defaultStreamBlock())
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    class Meta:
        verbose_name = "Homepage"

    api_fields = ('tags', 'body')


HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('tags'),
    StreamFieldPanel('body'),
]
