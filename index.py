#!/usr/bin/python
import sys
import requests
import re
from bs4 import BeautifulSoup

#declaring variables
allLinks = [];mails=[]
url = "https://www.assentcompliance.com/about-leadership-team/"
response = requests.get(url)
#parse text and get links
soup = BeautifulSoup(response.text, 'html.parser')
links = [a.attrs.get('href') for a in soup.select('a[href]')]

for i in links:
    if (("mailto" in i) or ("contact" in i or "Contact" in i) or ("Career" in i or "career" in i )) or ('about' in i or "About" in i) or ('Services' in i or 'services' in i):
        allLinks.append(i)
    if '@' in i:
        mails.append(i)
print(mails)

#function for finding mails
def findMails(soup):
    for name in soup.find_all('a'):
        if (name is not None):
            emailText = name.text
            #checks if text is an email using regex expressions and returns a boolean
            match = bool(re.match('\w+@\w+\.{1}\w+',emailText))
            if ('@' in emailText and match==True) :
                emailText = emailText.replace(" ",'').replace('\r','')
                emailText = emailText.replace('\n','').replace('\t','')
                if (len(mails) == 0) or (emailText not in mails):
                    mails.append(emailText)

#loops through links on page in order to find more links and pass to the finding mails function.
for link in allLinks:
    if (link.startswith("http") or link.startswith("www")):
        r = requests.get(link)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        findMails(soup)
    else:
        newurl = url+link
        r = requests.get(newurl)
        data = r.text
        soup = BeautifulSoup(data,'html.parser')
        findMails(soup)

print(mails)
if (len(mails) == 0):
    print("No mails found")