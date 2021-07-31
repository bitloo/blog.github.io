#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'loop'
SITENAME = "loop's blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'Chinese (Simplified)'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/bitloo'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#一页最大得文章数
DEFAULT_PAGINATION = 5

#按时间顺序排序（时间最近的优先）
NEWEST_FIRST_ARCHIVES = True

#主题目录
THEME = 'themes/clean-blog'

COLOR_SCHEME_CSS = 'github.css'