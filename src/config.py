from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "RSI-X"
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    ROOT_DIR: Path = Path(__file__).resolve().parents[1]
    DATA_DIR: Path = ROOT_DIR / "data"
    DATABASE_URL: str = "postgresql+psycopg2://rsix:rsix_password@postgres:5432/rsix_db"
    NEO4J_URI: str = "bolt://neo4j:7687"
    NEO4J_PASSWORD: str = "rsix_graph_2024"
    MLFLOW_TRACKING_URI: str = "http://mlflow:5000"
    model_config = {
        "env_file": ".env",
        "case_sensitive": False,
        "extra": "ignore",  # Ignore extra env vars from .env
    }

settings = Settings()
