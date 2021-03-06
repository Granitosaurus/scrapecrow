#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# meta info
AUTHOR = "Bernardas Ališauskas"
SITENAME = "Scrapecrow"
SITETITLE = AUTHOR
SITEURL = ""  # this will be update by publishconf
PATH = "content"
TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "en"
SITEDESCRIPTION = (
    "Educational blog about web-scraping, crawling and related data extraction subjects"
)
SITEURL = "http://localhost:8000"
SITELOGO = "/images/logo.svg"
FAVICON = "/images/favicon.ico"

# Theming
AUTHOR_IMG = "images/author.jpg"
AUTHOR_WEB = "http://granitosaur.us"
THEME = "corvid"
TYPOGRIFY = False
# THEME based settings
CONTENT_LICENSE = "CC BY-SA 2021"  #  unused
UTTERANCES_REPO = "granitosaurus/scrapecrow"
EMAILSUB_LINK = "https://716df175.sibforms.com/serve/MUIEALpKPp8WjHrVwQOX6keZXLkJRbnFEh2y6YhTmVmT4Z0Khgbi2MFvPO1OObOrjbMi_S0M7VXkXGkcbh36H-SqEwM3dHXxdrOOXwEPGcp9rTQKkQvMkC70Dq9RmCoikia87nLsRcx0VVGmCG2zyx5s8BwpqevRmh70vKSaLe7e95yZDCROMvm2HcN3UpLw7UsFxl_UbI6TjY_e"
TWITTER_HANDLE = "scrapecrow"
APPLAUSE_BUTTON = True
TOC_INSERT = True  # whether to insert TOC after first paragraph
OG_IMAGE = "/images/logo-og.png"
TAG_DESC = {
    "async": "asynchronous programming paradigm",
    "scaling": "ensuring programs performance scales with the amount of tasks it has to perform",
    "python": "python programming language",
    "beginner": "beginner level article",
    "intermediate": "intermediate level article",
    "advanced": "advanced level article",
    "crawling": "programatically following web links to discover content",
    "discovery-methods": "ways to discover content on a website",
    "discovery": "finding content on a website",
    "indexes": "data indexing and search engines",
    "sitemap": "website content index specifically designed for web scrapers",
    "reverse-engineering": "understanding how piece of technology is working without having access to the source code",
}

# Content
STATIC_PATHS = ["images", "pages", "extra", "examples", "partial", "videos"]
ARTICLE_EXCLUDES = ["partial", "examples"]
DEFAULT_CATEGORY = "articles"
USE_FOLDER_AS_CATEGORY = False
DEFAULT_PAGINATION = 5
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/.nojekyll": {"path": ".nojekyll"},  # required by github
    "images/favicon.ico": {"path": "favicon.ico"},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_DOMAIN = SITENAME
FEED_ATOM = "atom.xml"
FEED_RSS = "rss.xml"

# Main menu
MAIN_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_RSS_ON_MENU = True
MENUITEMS = (
    ("about", "/pages/about.html"),
    ("hire", "/pages/hire.html"),
    ("☕", "/pages/coffee.html"),
    ("#web-scraping on matrix", "https://matrix.to/#/#web-scraping:matrix.org"),
)
FOOTERITEMS = (
    ("Archives", "/archives.html"),
    ("Tags", "/tags.html"),
    ("Made with Pelican", "https://blog.getpelican.com/"),
    ("Source on Github", "https://github.com/granitosaurus/scrapecrow/"),
    ("CC BY-SA", "https://creativecommons.org/licenses/by-sa/4.0/"),
)
SOCIAL = (
    ("github", "https://github.com/granitosaurus"),
    ("twitter", "https://twitter.com/Scrapecrow"),
    ("at", "mailto:bernard@scrapecrow.com"),
    ("matrix-org", "https://matrix.to/#/#web-scraping:matrix.org"),
)


# Plugins and their settings
PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ["shortcodes", "pelican-toc"]
SHORTCODES = {
    "img": """<a href="/images/{{src}}"><img class="{{cls}}" src="/images/{{src}}" width={{width}} title="{{desc}}" loading="lazy"></img></a><figcaption>{{desc}}</figcatpion>""",
    "img-big": """<a href="/images/{{src}}"><img class="bigc" src="/images/{{src}}" title="{{desc}}" loading="lazy"></img></a><figcaption>{{desc}}</figcatpion>""",
    "img-bigger": """<a href="/images/{{src}}"><img class="biggerc" src="/images/{{src}}" title="{{desc}}" loading="lazy"></img></a><figcaption>{{desc}}</figcatpion>""",
    "img-full": """<a href="/images/{{src}}"><img class="fullc" src="/images/{{src}}" title="{{desc}}" loading="lazy"></img></a><figcaption>{{desc}}</figcatpion>""",
    "mp4gif": """<video class="bigc" autoplay loop muted title="{{desc}}"><source src="/videos/{{src}}.mp4" type="video/mp4"></video><figcaption>{{desc}}</figcation>""",
}
TOC = {
    "TOC_HEADERS": "^h[1-6]",
    "TOC_INCLUDE_TITLE": "false",
}
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight", "linenums": True},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "mdx_include": {},
    },
    "output_format": "html5",
}
