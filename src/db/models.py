from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, JSON
from datetime import datetime, timezone

Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"
    doc_id = Column(String, primary_key=True)
    title = Column(String)
    text = Column(Text)
    date = Column(DateTime)
    source = Column(String)
    topic_id = Column(Integer)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class Topic(Base):
    __tablename__ = "topics"
    topic_id = Column(Integer, primary_key=True)
    name = Column(String)
    keywords = Column(JSON)
    count = Column(Integer)
    coherence = Column(Float)
    diversity = Column(Float)

class Forecast(Base):
    __tablename__ = "forecasts"
    id = Column(Integer, primary_key=True)
    metric_name = Column(String)
    model_name = Column(String)
    model_version = Column(String)
    forecast_date = Column(DateTime)
    predicted_value = Column(Float)
    lower_bound = Column(Float)
    upper_bound = Column(Float)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class Event(Base):
    __tablename__ = "events"
    event_id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(Text)
    event_date = Column(DateTime)
    event_type = Column(String)
    entities = Column(JSON)
