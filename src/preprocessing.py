from parser import get_steam_reviews
import re
from pymorphy3 import MorphAnalyzer

def new_features(df):
    df['review_length'] = df['review'].str.len()
    df['n_words'] = df['review'].str.split().str.len() # .str перевод всех отзывов в строки .split делит на слова превращая в list, .str снова превращает в строки и .len считает длину
    df['n_exclamations'] = df['review'].str.count('!')
    df['has_over_100h'] = (df['playtime'] >= 100).astype(int)
    
    return df

def clean_reviews(df):
    df = df.copy()

    df['review'] = df['review'].str.lower()
    df['review'] = df['review'].str.replace(r'[\r\n]+', ' ', regex=True)
    df['review'] = df['review'].str.replace(r'http\S+', ' ', regex=True)
    df['review'] = df['review'].str.replace(r'\s+', ' ', regex=True)
    df['review'] = df['review'].str.strip()
    df = df[df['review'].str.len() > 0] # удаление пустых отзывов
    
    return df

morph = MorphAnalyzer()
_lemma_cache = {} # создать кэш со словами. если слов много тысяч, то это сэкономит время

def lemmatize(text):
    if not isinstance(text, str): # если не буквы - отмена
        return ""
    
    words = text.split()
    lemmas = []

    for word in words:
        if word not in _lemma_cache:
            _lemma_cache[word] = morph.parse(word)[0].normal_form # если слова нет в кэше, лемматизируем его и добавляем в кэш. кэш - словарь, пример: _lemmatization_cache['красивыми'] = 'красивый'
        lemmas.append(_lemma_cache[word]) # а потом добавляем его и в строку чтобы вернуть отредаченный отзыв
    
    return ' '.join(lemmas) # все слова в отзыве теперь в начальной форме


# df = get_steam_reviews(appid=2807960, n_pages=30)

# df = new_features(df)
# df = clean_reviews(df)
# print(df.head())
# print(df.shape)
# print(df.columns)


