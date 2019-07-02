"""
create-banner.py
"""
import logging
from pelican import signals

logger = logging.getLogger(__name__)

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def create_banner(generator, content):
    """
    Gets a title, intro and img for banner from page.

    Gets the teaser_img metadata from each article, assumed to be a filename of a
    file residing in IMAGE_PATH, and appends it to IMAGE_PATH (assigning the result
    back into teaser_img).

    If no teaser_img attribute found in article's metadata, it is set to DEFAULT_TEASER.
    """

    if content.template == 'index_custom':
        # Get teaser_img from metadata; fallback to None if not present
        c = content._content

        content.bannerintro = find_between( c, '<div id="banner-start"></div>', '<div id="banner-end"></div>' )
        content.bannerimg = find_between( c, '<div id="banner-img-start"></div>', '<div id="banner-img-end"></div>' )
        content._content = find_between( c, '<div id="index-content-start"></div>', '<div id="index-content-end"></div>' )

def register():
    """Register the plugin with Pelican"""
    signals.page_generator_write_page.connect(create_banner)
