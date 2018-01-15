#Information of Price

import urllib.request
from bs4 import BeautifulSoup

def LinkAddress(address):
    url=str(address)
    url_read = urllib.request.urlopen(url)
    soup = BeautifulSoup(url_read, 'html.parser')

    return FindPrice(soup)

def FindPrice(sourceCode):
    script = sourceCode.find_all('script', limit=None)[25]
    script = str(str(str(script).split('":"')).split('","')).split()
    price=""
    for i in range(0, len(script) + 1):
        if script[i].__contains__('priceText'):
            price = script[i + 1]
            break

    price = price.split("'")[1]+' TL'
    return price

inpAddress=input("Link Address : ")

try:
    print("\nPrice : {}".format(LinkAddress(inpAddress)))
    input("")
except ValueError:
    print("\nOops! This product has not a price or \nThis product is temporarily not available.  Try again...")
    input("")
