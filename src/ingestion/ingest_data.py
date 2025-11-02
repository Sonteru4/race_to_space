import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta
import random
from src.config import settings
from src.utils import setup_logger

logger = setup_logger(__name__)

def generate_sample_data(n_docs: int = 500) -> Path:
    topics = [
        "Satellite Technology", "Rocket Propulsion", "Space Station Development",
        "Mars Exploration", "Lunar Missions", "SpaceX Achievements",
        "NASA Programs", "International Cooperation", "Commercial Space Flight",
        "Space Tourism", "Satellite Communications", "GPS Technology"
    ]
    documents = []
    for i in range(n_docs):
        t = random.choice(topics)
        doc = {
            "doc_id": f"doc_{i:04d}",
            "title": f"{t} - Report {i}",
            "text": f"This is a sample document about {t}. " * 40,
            "date": (datetime.now() - timedelta(days=random.randint(0, 1825))).isoformat(),
            "source": random.choice(["NASA", "SpaceX", "ESA", "Roscosmos", "ISRO"])
        }
        documents.append(doc)
    df = pd.DataFrame(documents)
    out = settings.DATA_DIR / "processed" / "documents.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    logger.info(f"Generated {len(df)} documents → {out}")
    return out

if __name__ == "__main__":
    generate_sample_data()
