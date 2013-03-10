from lxml import html
from lxml import etree

ARCHIVE_URL = "http://mto.mediatakeout.com/archive"

"""
Given a base URL and a file, write headlines for a single
archive page and return the integer value of the last page.
The return value is really just for convenience.
If MTO changes their DOM structure, this could break.
"""
def writeHeadlines(url, txtfile):
    doc = html.parse(url)
    limit = int(str(doc.getroot().cssselect('div.paging p.tr a:last-child')[0].text_content()))
    for element in doc.getroot().cssselect('a.link,a.article'):
        try:
            line = element.text_content()
            txtfile.write(line+"\n")

        except:
            pass


    return limit

"""
Iterate over all pages and scrape headline text.
"""
txtfile = open("headlines.txt", 'w')
limit = writeHeadlines(ARCHIVE_URL, txtfile)
for i in range (1, limit):
    writeHeadlines(ARCHIVE_URL+"?p="+str(i), txtfile)
    print i,

txtfile.close()
    
