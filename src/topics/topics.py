import pandas as pd
from pathlib import Path
from collections import Counter
from src.config import settings

def top_topics(limit: int = 10):
    csv = settings.DATA_DIR / "processed" / "documents.csv"
    if not csv.exists():
        return []
    df = pd.read_csv(csv)
    df["topic_name"] = df["title"].str.split(" - ").str[0]
    counts = Counter(df["topic_name"].tolist())
    items = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:limit]
    return [{"name": k, "count": v} for k, v in items]
