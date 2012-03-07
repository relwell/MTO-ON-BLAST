from lxml import html
from lxml import etree

ARCHIVE_URL = "http://mto.mediatakeout.com/archive"

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

txtfile = open("headlines.txt", 'w')

limit = writeHeadlines(ARCHIVE_URL, txtfile)

for i in range (1, limit):
    writeHeadlines(ARCHIVE_URL+"?p="+str(i), txtfile)
    print i,


    
