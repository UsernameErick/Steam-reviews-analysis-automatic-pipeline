from parser import get_appid, get_steam_reviews
from preprocessing import new_features, clean_reviews
from predict import predict_review
from analytics import make_summary
from report import save_report
# использование готовой модели с интерфейсом. запуск отсюда

url = input("Введите ссылку на продукт Steam: ")

appid = get_appid(url)

df = get_steam_reviews(appid)

df = clean_reviews(df)
df = new_features(df)

df = predict_review(df)

summary = make_summary(df)

save_report(df, summary, appid)

print("Отчет сохранён.")