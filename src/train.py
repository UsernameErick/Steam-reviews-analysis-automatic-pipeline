import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report
import joblib
from pathlib import Path
from config import base_dir, model_path

def train(df):
    X = df[['review', 'playtime', 'review_length', 'n_words', 'n_exclamations']] # и текст и числа сразу
    y = df['recommended']

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2, stratify=y)
    
    preprocessor = ColumnTransformer(transformers=[('text', TfidfVectorizer(max_features=10000, ngram_range = (1, 2), min_df=5, stop_words=stop_words), 'review')], remainder='passthrough') # трансформируем именно review в векторы чисел, остальное проходят(passthrough присоединяет оставшиеся числовые признаки к тем 10к текстовых признаков. получается 10004 признака в сумме)

    pipeline = Pipeline([('preprocessor', preprocessor), ('model', LogisticRegression(max_iter = 1000))])

    pipeline.fit(X_train, y_train)

    pred = pipeline.predict(X_test)
    print(classification_report(y_test, pred))

    joblib.dump(pipeline, model_path) # сохраняем модель

    return pipeline, X_test, y_test, pred

ru_stop = {
    'и', 'в', 'во', 'на', 'по', 'с', 'со',
    'что', 'это', 'как', 'для', 'из',
    'к', 'у', 'от', 'до', 'же', 'за', 'из-за',
    'быть'
}

en_stop = {
    'the', 'a', 'an', 'in', 'on', 'of',
    'to', 'is', 'are', 'and', 'for'
}

stop_words = list(
    ru_stop | en_stop
)

