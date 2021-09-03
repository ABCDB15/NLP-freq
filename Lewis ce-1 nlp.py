#!/usr/bin/env python
# coding: utf-8

# In[10]:


from bs4 import BeautifulSoup
#  The beautifulsoup is used for cleaning of the words from a given set 
import urllib.request

import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
#stop words are words that are generally not needed for doing the visualising in the NLP
response = urllib.request.urlopen('https://blogs.nasa.gov/commercialcrew/category/spacex/')
#The urllib.request.urlopen is used to open or crawl the targetted webpage
html = response.read()
soup = BeautifulSoup(html,"html5lib")
# in the soup variable in the above, the html word is removed from the extracted resulted text from the web page
text = soup.get_text(strip=True)
tokens = [t for t in text.split()]
# text.split 
clean_tokens = tokens[:]

#print(clean_tokens)
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
new_token = []
#new_token1 = []
for f1 in clean_tokens:
    i=0
    for f2 in clean_tokens:
        if (f1 == f2):
            i=i+1
        if (i == 5):
            new_token.append(f1)
            break

freq = nltk.FreqDist(new_token)
freq.plot(10, cumulative=False)
bar_freq = {i:j for i,j in freq.items() if j > 30}
plt.bar(bar_freq.keys(), bar_freq.values())
plt.show()


# In[ ]:




