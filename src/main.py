import pandas as pd
from parser import get_steam_reviews
from preprocessing import new_features, clean_reviews, lemmatize
from train import train
from pathlib import Path
from analytics import show_top_words, show_errors, show_feature_importance

base_dir = Path(__file__).resolve().parent
data_path = base_dir.parent / "data" / "battlefield6_reviews.parquet"


if Path(data_path).exists(): # если уже спарсили и сохранили, то просто присвоить её df
    df = pd.read_parquet(data_path)
else:
    #parse
    df = get_steam_reviews(appid=2807960, n_pages=30)
    #save raw data
    df.to_parquet(data_path, index=False)

df = pd.read_parquet(data_path)

#preprocess
df = new_features(df)
print(df.shape)
df = clean_reviews(df)
print(df.shape)
df['review'] = df['review'].apply(lemmatize)
print(df.shape)

#train model
model, X_test, y_test, pred = train(df)
print(df.shape)

#analytics
show_top_words(model)
show_feature_importance(model)
show_errors(X_test, y_test, pred)
