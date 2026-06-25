import pandas as pd
# аналитика

def show_top_words(model):
    tfidf = (model.named_steps['preprocessor'].named_transformers_['text'])
    feature_names = tfidf.get_feature_names_out()

    coefs = (model.named_steps['model'].coef_[0])

    words_df = pd.DataFrame({'word': feature_names, 'coef': coefs[:len(feature_names)]}) # [:N] значит выбрать первые N. [:len(feature_names)] значит первые 10000. т.к. нам нужны только текстовые коэффициенты, а коэффициентов всего 10004(ласт 4 - числовые), то мы аккуратно забираем только текст.

    print("Top positive words:\n", words_df.sort_values('coef', ascending = False).head(10))
    print("Top negative words:\n", words_df.sort_values('coef', ascending = True).head(10))


def show_errors(X_test, y_test, pred):
    errors = X_test.copy()

    errors['real'] = y_test.values
    errors['pred'] = pred

    errors = errors[errors['real'] != errors['pred']] # оставляем только ошибочные предсказания

    print("prediction errors:\n", errors[['review', 'real', 'pred']].head(10))

def show_feature_importance(model):
    feature_names = (model.named_steps['preprocessor'].get_feature_names_out()) # вытаскиваем все 10004 признаков
    coefs = model.named_steps['model'].coef_[0]
    importance = pd.DataFrame({'feature': feature_names, 'coefs': coefs})

    print("Top positive features:\n", importance.sort_values('coefs', ascending=False).head(10))
    print("Top negative features:\n", importance.sort_values('coefs').head(10))

def make_summary(df):
    summary = {
        'n_reviews': len(df), 
        'positive_pred': round(df['pred'].mean()*100, 2),
        'negative_pred': round((1-df['pred']).mean()*100, 2), # avg позитивные и негативные предикты в нормальных процентах
        'avg_playtime': round(df['playtime'].mean(), 2),
        'avg_confidence': round(df['proba'].apply(lambda x: max(x, 1-x)).mean(), 2) # покажет то насколько модель в принципе уверена в предикте, неважно true или false
        }
    return summary