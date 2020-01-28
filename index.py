import requests
import re
from bs4 import BeautifulSoup

#declaring variables
alllinks = []
mails = []
url = "https://www.assentcompliance.com/"
response = requests.get(url)
#parse text and get links
soup = BeautifulSoup(response.text, 'html.parser')
links = [a.attrs.get('href') for a in soup.select('a[href]')]



allLinks = []
mails=[]
url = 'https://kore.ai/'
response = requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
links = [a.attrs.get('href') for a in soup.select('a[href]') ]
for i in links:
    if(("contact" in i or "Contact")or("Career" in i or "career" in i))or('about' in i or "About" in i)or('Services' in i or 'services' in i):
        allLinks.append(i)
allLinks=set(allLinks)
def findMails(soup):
    for name in soup.find_all('a'):
        if(name is not None):
            emailText=name.text
            match=bool(re.match('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',emailText))
            if('@' in emailText and match==True):
                emailText=emailText.replace(" ",'').replace('\r','')
                emailText=emailText.replace('\n','').replace('\t','')
                if(len(mails)==0)or(emailText not in mails):
                    print(emailText)
                mails.append(emailText)
for link in allLinks:
    if(link.startswith("http") or link.startswith("www")):
        r=requests.get(link)
        data=r.text
        soup=BeautifulSoup(data,'html.parser')
        findMails(soup)

    else:
        newurl=url+link
        r=requests.get(newurl)
        data=r.text
        soup=BeautifulSoup(data,'html.parser')
        findMails(soup)

mails=set(mails)
if(len(mails)==0):
    print("NO MAILS FOUND")