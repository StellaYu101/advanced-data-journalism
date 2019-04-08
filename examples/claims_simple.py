import mechanize
from bs4 import BeautifulSoup

urls = [
  'http://156.99.75.64/Weblink8CityClerk/0/fol/244266/Row1.aspx',
  'http://156.99.75.64/Weblink8CityClerk/0/fol/241028/Row1.aspx',
  'http://156.99.75.64/Weblink8CityClerk/0/fol/234040/Row1.aspx',
  'http://156.99.75.64/Weblink8CityClerk/0/fol/196115/Row1.aspx',
  'http://156.99.75.64/Weblink8CityClerk/0/fol/148100/Row1.aspx',
  'http://156.99.75.64/Weblink8CityClerk/0/fol/107617/Row1.aspx',
  'http://156.99.75.64/Weblink8CityClerk/0/fol/86488/Row1.aspx',
  'http://156.99.75.64/Weblink8CityClerk/0/fol/70623/Row1.aspx'
  ]

for url in urls:
    # Open a browser and get the URL
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open(url)

    # Get HTML and make soup
    html = br.response().read()
    soup = BeautifulSoup(html, 'html.parser')

    # Find each row in the table
    rows = soup.find('table', {'class': 'DocumentBrowserDisplayTable'}).find_all('tr')

    # Grab info from each row in the table
    for r in rows:
        cells = r.find_all('td')

        link = r.find_all('a')[1]['href']
        row = link.split('/')

        if len(row) > 1 and row[-3] == 'doc':
            docid = row[-2]
            name = r.find_all('span')[0].text
            pages = int(cells[2].text)

            for i in range(1, pages):
                page_image_url = 'http://156.99.75.64/Weblink8CityClerk/PageImageData.aspx?scale=2681&dID=%s&pageNum=%s&ann=1&r=Gz4JLWNW&search=' % (docid, i)
                print page_image_url    
