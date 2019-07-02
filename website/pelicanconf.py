#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Dummy class
# This has been added to avoid needing the full i18n plugin
class i18n(object):
    # looks for translations in
    # {LOCALE_DIR}/{LANGUAGE}/LC_MESSAGES/{DOMAIN}.mo
    # if not present, falls back to default

    DOMAIN = 'messages'
    LOCALE_DIR = '{THEME}/translations'
    LANGUAGES = ['en']
    NEWSTYLE = True

    __name__ = 'i18n'

    def register(self):
        from pelican.signals import generator_init
        generator_init.connect(self.install_translator)

    def install_translator(self, generator):
        import gettext
        try:
            translator = gettext.translation(
                self.DOMAIN,
                self.LOCALE_DIR.format(THEME=THEME),
                self.LANGUAGES)
        except (OSError, IOError):
            translator = gettext.NullTranslations()
        generator.env.install_gettext_translations(translator, self.NEWSTYLE)

# Create single STPA page from markdown files
filenames = ['../STPA/losses-and-hazards.md', '../STPA/level-2/level-2-control-structure.md', '../STPA/level-2/level-2-UCAs.md', '../STPA/level-2/level-2-scenarios.md']
with open('level-2-concat.md', 'w') as outputfile:
    outputfile.write('Title: level-2\n')
    outputfile.write('URL:\n')
    outputfile.write('save_as: level-2.html\n')
    outputfile.write('toc_headers: ^h[1-3]\n')
    outputfile.write('template: stpa\n')
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outputfile.write(line)

AUTHOR = u'MIT and Codethink'
SITENAME = u'Autonomous Vehicle STPA'
SITEURL = ''

# Paths to files
PATH = ''
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['./']
IGNORE_FILES = ['theme', 'plugins', 'output', 'requirements.txt', 'losses-and-hazards.md', 'level-2', 'level-3']
STATIC_PATHS = ['./images']
OUTPUT_PATH = 'output'

# Themes
THEME = './theme'
BOOTSTRAP_THEME = 'flatly'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = False

DEFAULT_PAGINATION = 10

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ["plugins"]
PLUGINS = [i18n(), "toc", "create-banner"]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MENUITEMS = (
    ('Home', 'index.html'),
    ('Contributing', 'contributing.html'),
    ('STPA Results', 'stpa.html'),
    ('Level 2', 'level-2.html'),)

TOC = {
    'TOC_HEADERS'       : '^h[1-6]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression

    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated

    'TOC_INCLUDE_TITLE': 'false',     # If 'true' include title in toc
}

## pelican-bootstrap3 options
HIDE_SIDEBAR = True
SIDEBAR_ON_LEFT = True
BOOTSTRAP_FLUID = False

BANNER_IMAGE = "./images/level-2-control-diagram.png"
