# Race to Space Intelligence X (RSI-X)

**An open, modular ML intelligence stack for space-era data analytics.**

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39-FF4B4B.svg)](https://streamlit.io/)
[![MLflow](https://img.shields.io/badge/MLflow-2.17-0194E2.svg)](https://mlflow.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Overview

RSI-X is a production-ready, containerized machine learning platform designed for space and aerospace data analytics. It provides a complete stack for data ingestion, topic modeling, forecasting, and graph-based intelligence—all orchestrated through Docker Compose and accessible via RESTful APIs and interactive dashboards.

The platform combines modern ML tooling (MLflow, scikit-learn) with enterprise databases (PostgreSQL with pgvector, Neo4j) and intuitive UIs (Streamlit, FastAPI docs) to deliver an end-to-end analytics experience that's 100% local and free to run.

---

## ✨ Key Features

- **🚀 Multi-Service Stack**: FastAPI REST API, Streamlit dashboard, PostgreSQL/pgvector (vector search), Neo4j (graph DB), MLflow (experiment tracking), Jupyter notebooks
- **🐳 Full Containerization**: Docker Compose orchestration with health checks, dependency management, and persistent volumes
- **📊 End-to-End ML Pipeline**: Reproducible workflows for data ingestion → topic modeling → forecasting → RAG (retrieval-augmented generation) placeholders
- **🆓 100% Local & Free**: No cloud dependencies—runs entirely on localhost with Docker Desktop
- **🔧 Developer-Friendly**: Makefile commands, hot-reload capabilities, comprehensive logging
- **📈 Production-Ready**: Structured logging, error handling, CORS middleware, database migrations

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    RSI-X Stack Architecture                  │
└─────────────────────────────────────────────────────────────┘

┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Streamlit  │────▶│  FastAPI     │────▶│  PostgreSQL  │
│  Dashboard   │     │    API       │     │  (pgvector)  │
│  :8501       │     │   :8000      │     │    :5432     │
└──────────────┘     └──────┬───────┘     └──────────────┘
                            │
                            ├────▶┌──────────────┐
                            │     │    Neo4j     │
                            │     │ Graph DB     │
                            │     │ :7474, :7687 │
                            │     └──────────────┘
                            │
                            └────▶┌──────────────┐
                                  │    MLflow    │
                                  │  Tracking    │
                                  │    :5001     │
                                  └──────────────┘

┌──────────────┐
│   Jupyter   │
│ Notebooks   │
│   :8888     │
└──────────────┘

Data Flow:
  data/ → ingestion/ → topics/ → forecast/ → API → Streamlit
         └──────────→ models/ (MLflow tracked)
```

---

## 📁 Repository Structure

```
race_to_space/
├── src/                    # Core application code
│   ├── api/               # FastAPI REST endpoints
│   │   ├── main.py        # API entry point
│   │   ├── routes/        # API route modules
│   │   └── models/       # Pydantic models
│   ├── app/               # Streamlit dashboard
│   │   ├── streamlit_app.py
│   │   └── pages/         # Multi-page Streamlit views
│   ├── db/                # Database layer
│   │   ├── models.py      # SQLAlchemy models
│   │   └── init_schema.py # Schema initialization
│   ├── ingestion/         # Data ingestion pipeline
│   ├── topics/            # Topic modeling module
│   ├── forecast/          # Forecasting module
│   ├── rag/              # RAG placeholder
│   ├── graph/             # Neo4j graph operations
│   ├── metrics/           # ML metrics
│   ├── validation/        # Data validation
│   ├── monitoring/        # Observability
│   ├── config.py          # Settings management
│   └── utils.py           # Shared utilities
│
├── data/                   # Data directories
│   ├── raw/               # Raw input data
│   ├── processed/         # Processed CSV/JSON
│   ├── embeddings/        # Vector embeddings
│   └── exports/           # Export outputs
│
├── models/                 # Trained ML models
│   ├── topics/            # Topic models
│   ├── forecasts/         # Forecast models
│   └── embeddings/       # Embedding models
│
├── notebooks/             # Jupyter notebooks
├── tests/                 # Test suite
│   ├── unit/             # Unit tests
│   └── integration/      # Integration tests
│
├── reports/               # Analysis reports
│   ├── evidently/        # Data drift reports
│   ├── great_expectations/ # Data quality
│   └── metrics/          # Performance metrics
│
├── deploy/                # Deployment configs
│   ├── kubernetes/       # K8s manifests
│   └── terraform/        # Infrastructure as code
│
├── dbt/                   # dbt models
├── docs/                  # Documentation
│
├── docker-compose.yml     # Service orchestration
├── Dockerfile.api         # API container
├── Dockerfile.streamlit   # Streamlit container
├── Dockerfile.jupyter     # Jupyter container
├── Makefile              # Convenience commands
├── requirements.txt      # Python dependencies
└── .env                  # Environment variables
```

---

## 🛠️ Tech Stack

| Category | Technology | Version | Purpose |
|----------|-----------|---------|---------|
| **API Framework** | FastAPI | 0.115.0 | REST API with auto-docs |
| **Web UI** | Streamlit | 1.39.0 | Interactive dashboard |
| **ML Tracking** | MLflow | 2.17.1 | Experiment tracking & model registry |
| **Relational DB** | PostgreSQL + pgvector | 16 | Vector similarity search |
| **Graph DB** | Neo4j | 5.25.1 | Knowledge graph storage |
| **ORM** | SQLAlchemy | 2.0.36 | Database abstraction |
| **Data Processing** | pandas | 2.2.3 | Data manipulation |
| **ML Library** | scikit-learn | 1.5.2 | Machine learning models |
| **NLP** | nltk | 3.9.1 | Natural language processing |
| **Visualization** | Plotly | 5.24.1 | Interactive charts |
| **Validation** | Pydantic | 2.9.2 | Data validation |
| **Orchestration** | Docker Compose | Latest | Container orchestration |
| **Notebooks** | Jupyter | Latest | Data exploration |

---

## 🚀 Quickstart Guide

### Prerequisites

- **Docker Desktop** (macOS/Windows/Linux) - [Download](https://www.docker.com/products/docker-desktop)
- **Git** - For cloning the repository
- **Make** (optional, but recommended) - Pre-installed on macOS/Linux

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/race_to_space.git
   cd race_to_space
   ```

2. **Configure environment** (optional)
   ```bash
   # Edit .env if you need custom ports or credentials
   # Default values work out of the box
   ```

3. **Build and start services**
   ```bash
   make quickstart
   # Or manually:
   docker compose build
   docker compose up -d
   ```

4. **Initialize database and load sample data**
   ```bash
   make init-db      # Create tables
   make pipeline     # Ingest sample data
   ```

### Access URLs

Once services are running, access:

| Service | URL | Description |
|---------|-----|-------------|
| **Streamlit Dashboard** | http://localhost:8501 | Interactive UI with topics & forecasts |
| **FastAPI Docs** | http://localhost:8000/docs | Interactive API documentation (Swagger) |
| **MLflow UI** | http://localhost:5001 | ML experiment tracking dashboard |
| **Neo4j Browser** | http://localhost:7474 | Graph database browser |
| **Jupyter Notebooks** | http://localhost:8888 | Data exploration environment |

---

## 📖 Usage

### API Endpoints

#### Health Check
```bash
curl http://localhost:8000/health
# Response: {"status": "ok", "app": "RSI-X"}
```

#### Get Top Topics
```bash
curl "http://localhost:8000/topics?limit=5"
# Response: {"items": [{"name": "Mars Exploration", "count": 48}, ...]}
```

#### Get Forecast
```bash
curl "http://localhost:8000/forecast?days=7"
# Response: {"items": [{"date": "...", "predicted": 100.0, "low": 97.0, "high": 103.0}, ...]}
```

### Streamlit Dashboard Features

- **Health Status**: Real-time API connectivity check
- **Topics Visualization**: Interactive table showing top topics with counts
- **Forecast Charts**: Line charts with confidence intervals
- **Real-time Updates**: Live data refresh from API

### Jupyter Environment

Jupyter notebooks are pre-configured with:
- Full access to `src/` modules
- Pre-loaded dependencies (pandas, numpy, scikit-learn)
- Direct database connections via SQLAlchemy

Access at **http://localhost:8888** (no password required in dev mode).

---

## 🔧 Development

### Common Commands

```bash
# Start all services
make up

# View logs (follow mode)
make logs

# Check service status
make status

# Rebuild containers (after code changes)
make rebuild

# Stop all services
make down

# Clean everything (containers + volumes)
make clean

# Run demo/test endpoints
make demo
```

### Rebuilding After Changes

```bash
# After modifying Python code:
docker compose build api streamlit
docker compose up -d api streamlit

# After modifying requirements.txt:
make rebuild
```

### Extending the ML Pipeline

1. **Add a new ML module**:
   ```bash
   mkdir -p src/your_module
   touch src/your_module/__init__.py
   touch src/your_module/your_model.py
   ```

2. **Register with MLflow**:
   ```python
   import mlflow
   mlflow.set_tracking_uri(settings.MLFLOW_TRACKING_URI)
   mlflow.log_metric("your_metric", value)
   ```

3. **Expose via API**:
   ```python
   # In src/api/main.py
   @app.get("/your-endpoint")
   def your_endpoint():
       return your_module.your_function()
   ```

4. **Add to Streamlit**:
   ```python
   # In src/app/streamlit_app.py
   st.subheader("Your Feature")
   # ... visualization code
   ```

### Future Roadmap Hooks

- **RAG Integration**: Placeholder in `src/rag/` for retrieval-augmented generation
- **Advanced Topic Modeling**: BERTopic integration (commented in `requirements.txt`)
- **Real-time Event Processing**: `src/events/` ready for Kafka/streaming
- **Model Monitoring**: Evidently AI integration in `reports/evidently/`
- **dbt Transformations**: Data modeling in `dbt/models/`

---

## 🚢 Deployment

### Local Development
Already configured—just run `make quickstart`.

### Cloud Deployment Options

#### AWS (EC2/ECS)
```bash
# Build and push images
docker build -t your-ecr/repo:tag -f Dockerfile.api .
docker push your-ecr/repo:tag

# Use ECS task definitions or EC2 with docker-compose
```

#### GCP (Cloud Run/Compute Engine)
```bash
# Build with Cloud Build
gcloud builds submit --tag gcr.io/PROJECT_ID/rsi-x-api

# Deploy to Cloud Run
gcloud run deploy rsi-x-api --image gcr.io/PROJECT_ID/rsi-x-api
```

#### Kubernetes
```bash
# Use manifests in deploy/kubernetes/
kubectl apply -f deploy/kubernetes/
```

#### Heroku (with Docker)
```bash
# Use Heroku Container Registry
heroku container:push web -a your-app
heroku container:release web -a your-app
```

### Production Considerations

- Set strong passwords in `.env`
- Enable SSL/TLS (use reverse proxy like nginx)
- Configure persistent volumes for production databases
- Set up monitoring (Prometheus, Grafana)
- Enable MLflow artifact storage (S3/GCS)
- Use managed databases (RDS, Cloud SQL, Neo4j Aura)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add docstrings to all functions/classes
- Write tests for new features
- Update README.md for new features
- Use meaningful commit messages

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Credits

- **Author**: Sanjana Onteru
- **Maintainer**: Open-source contributors
- **Inspiration**: Space data analytics, ML engineering best practices

---

## 📞 Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Check existing documentation in `docs/`
- Review example notebooks in `notebooks/`

---

**Built with ❤️ for the space data community**
