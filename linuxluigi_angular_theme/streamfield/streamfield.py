from wagtail.wagtailcore.blocks import RichTextBlock, StreamBlock


class defaultStreamBlock(StreamBlock):
    paragraph = RichTextBlock(icon="pilcrow")
