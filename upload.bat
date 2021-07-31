@echo off

set curtime=%date% %time%

set customDomain = "blog.notgame.top"

start cmd /k "pelican content -o output -s publishconf.py && ghp-import -c %customDomaim% -m "Publish site %curtime=%" --no-jekyll -b gh-pages output && git push origin gh-pages"