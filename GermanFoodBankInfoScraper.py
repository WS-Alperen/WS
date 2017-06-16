import urllib
import urllib.request
from bs4 import BeautifulSoup
import csv

with open('GermanFoodBankInfo.csv', 'a') as csv_file:
  writer = csv.writer(csv_file)

  for page_number in range(0, 39):
    page = urllib.request.urlopen('http://www.tafel.de/nc/die-tafeln/tafel-suche/adressenliste.html?tx_brtafel_pi1%5Btest%5D=test&tx_brtafel_pi1%5Bpointer%5D='
                                  + str(page_number))
    soup = BeautifulSoup(page, 'html.parser').find('dl', 'tafel-liste')

    fb_names = soup.find_all('dt')
    fb_info = soup.find_all('dd')

    for (name, info) in zip(fb_names, fb_info):
      contact = info.find_all('a')

      mail = ''
      website = ''

      if len(contact) != 0:
        if not contact[0].find('span') is None:
          contact[0].span.replace_with('') #to remove "NO-SPAM" in the HTML code
          mail = contact[0].text

          if len(contact) == 2:
            website = contact[1]['href']

        else:
          website = contact[0]['href']

      #Because two of the URLs contained characters which are not in Unicode, I had to find those URLs and encode them to prevent exception
      try:
        writer.writerow([name.text.strip(), mail, website])
      except:
        writer.writerow([name.text.strip(), mail.encode('utf-8'), website.encode('utf-8')])


