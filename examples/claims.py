import mechanize
from bs4 import BeautifulSoup


class ClaimsScraper(object):

    def __init__(self, url):
        self.url = url
        self.br = mechanize.Browser()
        self.soup = None

    def _open_url(self):
        self.br.set_handle_robots(False)
        self.br.open(self.url)
        return

    def _make_soup(self):
        self.soup = BeautifulSoup(self.br.response().read(), 'html.parser')
        return

    def _get_pages(self):
        return [a['href'] for a in self.soup.find_all('a', {'class': 'PageableListJumpToPage'})][:-1]

    def _switch_page(self, page_url):
        self.url = page_url
        self._open_url()
        self._make_soup()
        return 

    def _process_page(self):
        rows = self.soup.find('table', {'class': 'DocumentBrowserDisplayTable'}).find_all('tr')

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

    def scrape(self):
        self._open_url()
        self._make_soup()

        # Process the initial load
        self._process_page()

        for p in self._get_pages():
            page_url = 'http://156.99.75.64' + p

            self._switch_page(page_url)
            self._process_page()


if __name__ == '__main__':
    years = [
      'http://156.99.75.64/Weblink8CityClerk/0/fol/244266/Row1.aspx',
      'http://156.99.75.64/Weblink8CityClerk/0/fol/241028/Row1.aspx',
      'http://156.99.75.64/Weblink8CityClerk/0/fol/234040/Row1.aspx',
      'http://156.99.75.64/Weblink8CityClerk/0/fol/196115/Row1.aspx',
      'http://156.99.75.64/Weblink8CityClerk/0/fol/148100/Row1.aspx',
      'http://156.99.75.64/Weblink8CityClerk/0/fol/107617/Row1.aspx',
      'http://156.99.75.64/Weblink8CityClerk/0/fol/86488/Row1.aspx',
      'http://156.99.75.64/Weblink8CityClerk/0/fol/70623/Row1.aspx'
      ]

    for y in years:
        s = ClaimsScraper(y)
        s.scrape()