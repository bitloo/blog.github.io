@echo off

set curtime=%date% %time%

start cmd /k "pelican content -o output -s publishconf.py && ghp-import -m "Publish site %curtime=%" --no-jekyll -b gh-pages output && git push origin gh-pages"