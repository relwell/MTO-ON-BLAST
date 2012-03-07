import urllib
from lxml import etree
from lxml.cssselect import CSSSelector

ARCHIVE_URL = "http://mto.mediatakeout.com/archive"

content = urllib.urlopen(ARCHIVE_URL).read()

root = etree.fromstring(content)
print etree.tostring(root)
