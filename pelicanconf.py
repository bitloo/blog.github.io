#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Loop'
SITENAME = "Loop's Blog"
SITEURL = 'https://blog.notgame.top/'

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_RSS = "feeds/all.rss.xml"

# Blogroll
LINKS = (('my gitee', 'https://gitee.com/xquid'),)

# Social widget
SOCIAL = (('github', 'https://github.com/bitloo'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# DISPLAY_CATEGORIES_ON_MENU = True
# DISPLAY_PAGES_ON_MENU = True

# #一页最大得文章数
# # Pagination
DEFAULT_PAGINATION = 5
# PAGINATION_PATTERNS = (
#     (1, '{base_name}/', '{base_name}/index.html'),
#     (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
# )
# # Post and Pages path
# ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
# ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
# PAGE_URL = 'pages/{slug}/'
# PAGE_SAVE_AS = 'pages/{slug}/index.html'
# YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
# MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# # Tags and Category path
# CATEGORY_URL = 'category/{slug}'
# CATEGORY_SAVE_AS = 'category/{slug}/index.html'
# CATEGORIES_SAVE_AS = 'catgegories.html'
# TAG_URL = 'tag/{slug}'
# TAG_SAVE_AS = 'tag/{slug}/index.html'
# TAGS_SAVE_AS = 'tags.html'

# # Author
# AUTHOR_URL = 'author/{slug}'
# AUTHOR_SAVE_AS = 'author/{slug}/index.html'
# AUTHORS_SAVE_AS = 'authors.html'

#按时间顺序排序（时间最近的优先）
NEWEST_FIRST_ARCHIVES = True

#主题目录
THEME = 'themes/bootstrap2-dark'

#插件
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]

#tag_cloud
TAG_CLOUD_SORTING = 'alphabetically'
TAG_CLOUD_BADGE = True

DISQUS_SITENAME = 'loopblog'
