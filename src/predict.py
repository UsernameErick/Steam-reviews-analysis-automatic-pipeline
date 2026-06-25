import joblib
import pandas as pd
from pathlib import Path
from config import base_dir, model_path
# загрузка модели и предикт отзыва

def predict_review(df):
    model = joblib.load(model_path)
    X = df[['review', 'playtime', 'review_length', 'n_words', 'n_exclamations']]
    df = df.copy()

    df['pred'] = model.predict(X)
    df['proba'] = model.predict_proba(X)[:, 1]
    
    return df



# старый вариант когда мы вставляли 1 отзыв
# def predict_review(review, playtime, review_length, n_words, n_exclamations):
#     data = {'review': [review], 'playtime': [playtime], 'review_length': [review_length], 'n_words': [n_words], 'n_exclamations': [n_exclamations]}
#     df = pd.DataFrame(data)

#     pred = model.predict(df)[0]
#     proba = model.predict_proba(df)[0, 1]
#     return pred, proba

# pred, proba = predict_review("Игра крутая но не рекомендую", 500, 28, 5, 1)
# print(pred, proba)