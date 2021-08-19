@echo off

set curtime=%date% %time%

set customDomain=blog.notgame.top

set commitMessage=Publish site on %curtime%

start cmd /k "pelican content -o output -s publishconf.py && ghp-import --no-jekyll -b gh-pages output -c "%customDomain%" -m "%commitMessage%" -p"