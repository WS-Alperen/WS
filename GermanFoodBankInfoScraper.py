import urllib
import urllib.request
import urllib.error
import urllib.parse
import urllib.robotparser
from bs4 import BeautifulSoup

import csv

with open('GermanFoodBanksInfo.csv', 'a') as csv_file:
  writer = csv.writer(csv_file)

  for pageNumber in range(0, 39):
    page = urllib.request.urlopen('http://www.tafel.de/nc/die-tafeln/tafel-suche/adressenliste.html?tx_brtafel_pi1%5Btest%5D=test&tx_brtafel_pi1%5Bpointer%5D='
                        + str(pageNumber))
    soup = BeautifulSoup(page, 'html.parser').find('dl', 'tafel-liste')
    foodBank_names = soup.find_all('dt')

    for name in foodBank_names:
        writer.writerow(name)

