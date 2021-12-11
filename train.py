import requests
import bs4

URL = 'https://habr.com/ru/all/'
HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'ru,en;q=0.9',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Cookie': '_ym_d=1638028483; _ym_uid=16380284831002969016; _ga=GA1.2.1786197767.1638028484; hl=ru; fl=ru; __gads=ID=f2109a86373b47f5-2258ce6009cc00aa:T=1638028484:S=ALNI_MZDKpM6LxBVxdd9A9LHfnkn9ov6HQ; feature_streaming_comments=true; visited_articles=273089:250947:273115:74839; _gid=GA1.2.323979866.1639131132; _ym_isad=2; habr_web_home=ARTICLES_LIST_ALL',
           'Host': 'habr.com',
           'If-None-Match': 'W/"3b4e0-3d11MkVrV8wKQGJkLNaNzGDQwhY"',
           'Referer': 'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
           'sec-ch-ua': '"Chromium";v="94", "Yandex";v="21", ";Not A Brand";v="99"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': '"Windows"',
           'Sec-Fetch-Dest': 'document',
           'Sec-Fetch-Mode': 'navigate',
           'Sec-Fetch-Site': 'same-origin',
           'Sec-Fetch-User': '?1',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.2.773 Yowser/2.5 Safari/537.36',
}
KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'финансы в it', 'физика'}
response = requests.get(URL, headers=HEADERS)
text = response.text
response.raise_for_status()

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    hubs = [hub.find('span').text.lower() for hub in hubs]
    hubs = set(hubs)
    if KEYWORDS & hubs:
        title = article.find('a', class_="tm-article-snippet__title-link")
        article_new = title.find('span').text
        date = article.find('time')['title']
        link = article.find('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2')
        link = link.find('a')['href']
        result = f'{date} - {article_new} - https://habr.com{link}'
        print(result)
        print('----------------------------')
