import requests
import Prediction

from bs4 import BeautifulSoup



def get_news():
    URL="https://zeenews.india.com/gujarati"
    header={
        'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4555.0 Safari/537.36'
    }
    
    r = requests.get(URL,headers=header)
    
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    #print(soup.prettify())
    news=[]
    table = soup.findAll('div', attrs = {'class':'sec-h3'}) 
    for row in table:
        news.append(row.find('a').text.replace('\n',''))
    print("Total news fetched :",len(news))
    return news;


news = get_news()
for n in news:
    emo = Prediction.predicted([n])
    #print(n, ' : ', emo)