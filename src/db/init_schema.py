from src.db.models import Base
from src.utils import engine, setup_logger

logger = setup_logger(__name__)

def init_db():
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database initialized!")

if __name__ == "__main__":
    init_db()
