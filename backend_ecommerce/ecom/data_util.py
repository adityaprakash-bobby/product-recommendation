import requests
import urllib3
from bs4 import BeautifulSoup

urls = [
    "https://www.amazon.in/Lenovo-81D20090IN-15-6-inch-Integrated-Graphics/dp/B07N8K4PVM/ref=pd_sbs_147_9?_encoding=UTF8&pd_rd_i=B07N8K4PVM&pd_rd_r=43653063-4f24-4b86-a3de-d8c2f9518a71&pd_rd_w=2WaGs&pd_rd_wg=Zuqxi&pf_rd_p=2785a4f5-4b62-4bf0-bf3d-365a6e281498&pf_rd_r=GFCQ7SBBJ4F2WZ7XEB54&psc=1&refRID=GFCQ7SBBJ4F2WZ7XEB54",
    "https://www.amazon.in/Acer-A315-41-Ryzen-Radeon-Graphics/dp/B07SBP7145/ref=pd_sbs_147_5/260-5332864-5052556?_encoding=UTF8&pd_rd_i=B07SBP7145&pd_rd_r=c0c84ffe-ef5f-4d30-a6e6-f52b21970e25&pd_rd_w=gb1HI&pd_rd_wg=cl9Wu&pf_rd_p=2785a4f5-4b62-4bf0-bf3d-365a6e281498&pf_rd_r=X19MKKFVY0X22SVSS7RW&psc=1&refRID=X19MKKFVY0X22SVSS7RW",
    "https://www.amazon.in/VivoBook-R5-2500-Windows-X505ZA-EJ563T/dp/B07N8FF1D4?tag=googinhydr18418-21&tag=googinkenshoo-21&ascsubtag=_k_Cj0KCQjwhJrqBRDZARIsALhp1WQobSBFa3-16Zj0d_naoA1afUhUoc-4XTbpuOVa0iT9SbzKIv7-JvMaAvLMEALw_wcB_k_&gclid=Cj0KCQjwhJrqBRDZARIsALhp1WQobSBFa3-16Zj0d_naoA1afUhUoc-4XTbpuOVa0iT9SbzKIv7-JvMaAvLMEALw_wcB",
    "https://www.amazon.in/ASUS-X510UA-EJ1070T-8130-WIN10-15-6/dp/B07GKM647P/ref=pd_sbs_147_27?_encoding=UTF8&pd_rd_i=B07GKM647P&pd_rd_r=9be6917d-4579-4f24-9c8b-427d9143a4a2&pd_rd_w=P3po7&pd_rd_wg=T2ved&pf_rd_p=2785a4f5-4b62-4bf0-bf3d-365a6e281498&pf_rd_r=DE958HZ9G6AVK6GFJ48X&psc=1&refRID=DE958HZ9G6AVK6GFJ48X",
]

def readTechSpecs(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Origin': 'https://www.amazon.in',
        'Referer': 'https://www.amazon.in/Lenovo-81D20090IN-15-6-inch-Integrated-Graphics/dp/B07N8K4PVM/ref=pd_sbs_147_9?_encoding=UTF8&pd_rd_i=B07N8K4PVM&pd_rd_r=43653063-4f24-4b86-a3de-d8c2f9518a71&pd_rd_w=2WaGs&pd_rd_wg=Zuqxi&pf_rd_p=2785a4f5-4b62-4bf0-bf3d-365a6e281498&pf_rd_r=GFCQ7SBBJ4F2WZ7XEB54&psc=1&refRID=GFCQ7SBBJ4F2WZ7XEB54',
    }

    res = requests.get(url, headers=headers)
    # print(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    # Find Price
    bad_chars = [' ', '\xa0', ',', '₹']
    
    price_div = soup.find('div', attrs={'id':'olp_feature_div'})
    # print(price_div)
    price = price_div.find('span', attrs={'class':'a-color-price'})
    price = price.text

    for i in bad_chars:
        price = price.replace(i, '')

    table_div = soup.find('div', class_='pdTab')
    table = table_div.find('tbody')
    # print(table)
    rows = table.find_all('tr')

    specs = {}

    for row in rows:

        [label, value] = row.find_all('td')
        specs[label.text] = value.text

    specs['Price'] = price

    return specs

    # specs_list = []

    # specs_list.append(1)
    # specs_list.append(specs['Screen Size'])
    # specs_list.append(specs['Processor Type'])
    # specs_list.append(specs['RAM Size'])
    # specs_list.append(specs['Graphics Coprocessor'])
    # specs_list.append(specs['Operating System'])
    # specs_list.append(specs['Item Weight'])
    # specs_list.append(specs['Price'])
    # specs_list.append(0)

    # return specs_list

# for url in urls:
from pprint import pprint as pp
pp(readTechSpecs(urls[2]))
