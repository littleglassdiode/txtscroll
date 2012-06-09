#!/usr/bin/env python2
# txts2html.py

from sys import argv
from os import listdir

# Constants
gamedir = '%s/' % argv[1]
dirlist = listdir(gamedir)

# Init
counter = 1

for gamefile in dirlist:
    link = ''
    ltxt = ''
    if not gamefile.endswith('.txts'):
        continue
    gf = open(gamedir+gamefile, 'r')
    htmlf = open(gamefile[:-5]+'.html', 'w')

    htmlf.write('''\
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
  <head profile="http://www.w3.org/2005/10/profile">
    <title>TxtScroll HTML</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <div>\n''')

    for line in gf:
        line = line.strip()
        if line.startswith('#'):
            continue
        if not line:
            continue
        elif line.startswith('|=') and line.endswith('=|'):
            htmlf.write('      <h1>'+line.strip('|=')+'</h1>\n')
        elif line.startswith('@'):
            line = line[1:]
            link = line.split(':')[0]
            if link.endswith('.txts'):
                link = link[:-5] + '.html'
            ltxt = line.split(':')[1]
            if link == '$quit$':
                continue
            htmlf.write('      %d. <a href="%s">%s</a><br />\n'%
                        (counter, link, ltxt))
            counter = counter + 1
        else:
            htmlf.write(line+'<br />\n')

    htmlf.write('''\
      <div class='valid'>
        <a href="http://validator.w3.org/check?uri=referer"><img
           src="http://www.w3.org/Icons/valid-xhtml11"
           alt="Valid XHTML 1.1" height="31" width="88" /></a
        ><a href="http://jigsaw.w3.org/css-validator/check/referer"><img
           style="border:0;width:88px;height:31px"
           src="http://jigsaw.w3.org/css-validator/images/vcss"
           alt="Valid CSS!" />
        </a>
      </div>
    </div>
  </body>
</html>\n''')

    htmlf.close()
    gf.close()

    counter = 1
