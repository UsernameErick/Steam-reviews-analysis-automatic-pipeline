from config import reports_dir

reports_dir.mkdir(exist_ok=True)

def save_report(df, summary, appid):
    report_path = reports_dir / f'{appid}_report.txt'

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f'AppID: {appid}\n')
        f.write(f'Reviews: {summary["n_reviews"]}\n')
        f.write(f'Positive:\n {summary["positive_pred"]}%\n')
        f.write(f'Negative:\n {summary["negative_pred"]}%\n')
        f.write(f'Average Playtime: {summary["avg_playtime"]} hours\n')
        f.write(f'Average model Confidence: {summary["avg_confidence"]}\n')