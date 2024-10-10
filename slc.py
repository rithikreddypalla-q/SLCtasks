import requests
from bs4 import BeautifulSoup
def urlsbr(extension):
    url = 'https://intranet.iiit.ac.in/offices/default/display_all_files'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        k=a['href']
        if(k[len(k)-4:] == extension):
            if(k[0] == '/'):
                links.append('https://intranet.iiit.ac.in' + k)
            else:
                links.append(k)
        
    with open('urls.txt', 'w') as file:
        for link in links:
            file.write(link+"\n")
def byname(name):
    url = 'https://intranet.iiit.ac.in/offices/default/offices_x?office='+name.replace(" ","+")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        k=a['href']
        if(k[len(k)-4:] == '.pdf' or k[len(k)-5:] == '.html'):
            if(k[0] == '/'):
                links.append('https://intranet.iiit.ac.in' + k)
            else:
                links.append(k)
    with open(name.replace(" ","_")+'.txt', 'w') as file:
        for link in links:
            file.write(link+"\n")
urlsbr('.pdf')
byname('Admissions Office')