from urllib.request import urlopen
from bs4 import BeautifulSoup, ResultSet
import csv, string, re

def write_file(properties,oper):
    with open('properties.txt',oper) as p_file:
        p_file.writelines("%s\n" % prop for prop in properties)

def read_file():
    #
    with open('properties.txt','r') as p_file:
        filecontent = p_file.readlines()
        for line in filecontent:
            place = line[:-1]
            props.append(place)


#https://www.property.com.au/rent/property-house-with-3-bedrooms-in-wellington+point,+qld+4160/list-1?includeSurrounding=true
url = "https://www.property.com.au/rent/property-house-with-3-bedrooms-in-wellington+point,+qld+4160/list-1?includeSurrounding=true"
next_page_exists = True
pagecounter = 1
property = []

while next_page_exists:
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    type(soup)
    #title = soup.title
    #print(title)
    #text = soup.get_text()
    #print(text)
    #props = soup.find_all('div', class_=lambda s:s.startswith('resultBody platinum tier'))
    match_cond = "'resultBody' and 'tier'"
    props = soup.find_all(class_ = re.compile('resultBody.*tier'))
    #props = soup.find_all(class_='resultBody platinum tier1')
    #props1 = soup.find_all(class_= 'resultBody first platinum tier1')
    #props.extend(props1)
    #props2 = soup.find_all(class_= 'resultBody featured platinum tier1')
    #props.extend(props2)

    for prop in props:
        p = prop.get_text()
        print(p[:40])
        property.append(p)

    next_indicator: ResultSet = soup.find_all(class_="nextLink")
    if len(next_indicator) == 0:
        next_page_exists = False
    else:
        print(next_indicator)
        old_s = 'list-' + str(pagecounter)
        pagecounter+=1
        new_s = 'list-' + str(pagecounter)
        url = url.replace(old_s,new_s,1)

write_file(property, 'a')


        #House: 4  2  2  is bed, bath, car
#pages with pages to follow has li class="nextLink", the last page does not have this
