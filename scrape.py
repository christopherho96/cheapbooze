from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.thebeerstore.ca/beers/sale'

#opening up connection, grabbing the page
uClient = uReq(my_url)
#loads content into variable
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"right"})
len(containers)

even_containers = page_soup.findAll("tr", {"class":"even"})

for container in containers:

    print(container.span.get_text())

    trs = container("tr")

    for tr in trs:
        tds = container.tr("td")

        for td in tds:
            print(td.get_text())
        print("\n")
