import sys
import requests
import urllib.request
from bs4 import BeautifulSoup
a='''

                /$$$$$$                                   
               /$$__  $$                                  
 /$$  /$$  /$$|__/  \ $$ /$$$$$$/$$$$   /$$$$$$  /$$$$$$$ 
| $$ | $$ | $$   /$$$$$/| $$_  $$_  $$ |____  $$| $$__  $$
| $$ | $$ | $$  |___  $$| $$ \ $$ \ $$  /$$$$$$$| $$  \ $$
| $$ | $$ | $$ /$$  \ $$| $$ | $$ | $$ /$$__  $$| $$  | $$
|  $$$$$/$$$$/|  $$$$$$/| $$ | $$ | $$|  $$$$$$$| $$  | $$
 \_____/\___/  \______/ |__/ |__/ |__/ \_______/|__/  |__/
                                                          
                                                          
                                                          
'''
print(a)

#tag=sys.argv[1]
#url="https://www.w3schools.com/tags/tag_"+tag+".asp"
t=input()
url="https://www.w3schools.com/tags/tag_"+t+".asp"
b= urllib.request.urlopen(url).read()

#soup = BeautifulSoup(b)
soup = BeautifulSoup(b, 'html.parser')

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())

# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)     #print(text)
flag=0
count=0         #global count
s=""
c=0
for i in text.split('\n'):
    if(i=="Definition and Usage"):
        print("\n")
        flag=2
        count=4
        print("DEFINITION AND USAGE\n")
        continue
    if(i=="Example" and c==0):
        c=1
        flag=1
        print("EXAMPLE\n")
        continue
    elif(i=="Try it Yourself »"):
        flag=0    
    if(flag==1):
        print(i)
    if((flag==2)and(count!=0)):
        #print(i)
        s=s+i
        count-=1
s=s[::-1]
r=s.split('.')
r.pop(0)
s=' . '.join(x for x in r)
s=s[::-1]
s=s+'.'
print(s)
