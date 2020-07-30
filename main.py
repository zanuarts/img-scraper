import requests
import os
from bs4 import BeautifulSoup

r2 = requests.get("https://alfalah.halalmart.me/herba/") # insert your main url
soup2 = BeautifulSoup(r2.text, "html.parser") # parsing / format html

# array untuk nampung si link img
links = []

x = soup2.select('img[src^="https://halalmart.me/wp-content/uploads"]') # cari link img di inspect element

# ntar si img di masukin ke array links
for img in x:
    links.append(img['src'])

# print for check the link is right
# for l in links:
#     print(l)

# make new direction
os.mkdir('herba')

# save ur fucking image
for index, img_link in enumerate(links):
    img_data = requests.get(img_link).content
    with open("herba/" + str (index+1)+'.jpg', 'wb+') as f:
        f.write(img_data)