import requests
from bs4 import BeautifulSoup
url = 'https://movie.douban.com/top250'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15'}

for num in range(0,250,25):
    response = requests.get(f'https://movie.douban.com/top250?start={num}', headers=headers)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    all_title = soup.find_all('span',attrs={'class':'title'})
    for title in all_title:
        title_string = title.string
        if '/' not in title_string:
            print(title_string)