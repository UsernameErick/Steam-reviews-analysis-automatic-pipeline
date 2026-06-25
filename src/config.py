from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent # 1 parent -> src, 2 parent -> steam bf6 reviews auto pipeline

data_path = base_dir / "data" / "battlefield6_reviews.parquet"
model_path = base_dir / "models" / "bf6_review_model.pkl"

reports_dir = base_dir / "reports"
