import urllib
from lxml import html


ARCHIVE_URL = "http://mto.mediatakeout.com/archive"

content = urllib.urlopen(ARCHIVE_URL).read()

root = html.parse(content)

print root

