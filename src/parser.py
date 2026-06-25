import pandas as pd
import requests
import re

# парсинг отзывов
def get_steam_reviews(appid, n_pages = 30, language='russian'):
    reviews = []
    cursor = '*' # метка начала. стим дает собрать только 100 отзывов за запрос, поэтому используем cursor и делаем несколько запросов подряд
    url = f'https://store.steampowered.com/appreviews/{appid}'

    for _ in range(n_pages): # до 3000 отзывов
        params = {'json': 1, 'language': 'russian', 'filter': 'recent', 'num_per_page': 100, 'cursor': cursor}

        response = requests.get(url, params = params)
        data = response.json()

        if len(data['reviews']) == 0:
            break

        for r in data['reviews']:
            reviews.append({'review': r['review'], 'recommended': r['voted_up'], 'playtime': r['author']['playtime_forever']/60, 'timestamp': r['timestamp_created']})
        
        cursor = data['cursor']
    return pd.DataFrame(reviews)

def get_appid(url): # функция для analyze_game.py
    match = re.search(r'app/(\d+)', url)

    if match:
        return int(match.group(1))

    raise ValueError('Неверная ссылка')

# df = get_steam_reviews(appid=2807960, n_pages=30)
# print(df['review'].sample(20, random_state=42).tolist())
# print(df.head())
# print(df.shape)
# print(df.columns)