# SETUP
import urllib2, csv
from bs4 import BeautifulSoup

# SETUP CSV
csvfile = open('patrol.csv', 'a')
patrol_writer = csv.writer(csvfile)

dates_to_scrape = ['04/07/2019', '04/08/2019', '04/09/2019']

for d in dates_to_scrape:

    # GETTING THE WEBSITE
    url = 'https://www.mshp.dps.missouri.gov/HP68/SearchAction?searchDate=' + d
    html = urllib2.urlopen(url).read()

    # PROCESSING THE HTML

    soup = BeautifulSoup(html, 'html.parser')

    # SCRAPING THE DATA

    table = soup.find('table', {'class': 'accidentOutput'})

    rows = table.find_all('tr')

    for row in rows:
        output_row = []

        cells = row.find_all('td')

        for cell in cells:
            output_row.append(cell.text)

        if len(output_row) > 0:
            patrol_writer.writerow(output_row)