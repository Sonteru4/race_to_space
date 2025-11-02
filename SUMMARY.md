# RSI-X: Executive Summary

**Race to Space Intelligence X (RSI-X)** is a production-ready, containerized machine learning platform for space-era data analytics, featuring a complete stack from data ingestion to model deployment with interactive visualizations.

Built on modern Python tooling (FastAPI, Streamlit, MLflow) and enterprise databases (PostgreSQL/pgvector, Neo4j), RSI-X orchestrates six microservices via Docker Compose to deliver an end-to-end ML intelligence pipeline. The architecture separates concerns cleanly: FastAPI serves REST endpoints for topic modeling and forecasting, Streamlit provides real-time dashboards, PostgreSQL handles vector similarity search, Neo4j manages knowledge graphs, MLflow tracks experiments, and Jupyter enables data exploration—all containerized for reproducible, scalable deployments.

In practice, RSI-X processes space-related documents through an ingestion pipeline, extracts topics via lightweight NLP, generates forecasts with confidence intervals, and visualizes results in an interactive dashboard. The system successfully ingests 500+ sample documents, extracts top topics (Mars Exploration, SpaceX Achievements, etc.), and serves predictions through both REST APIs and real-time UI—demonstrating a complete ML workflow from raw data to actionable insights.

**Highlights:**
- 🐳 **Dockerized Stack**: Multi-service orchestration with health checks and dependency management
- 📊 **MLflow Integration**: Experiment tracking and model versioning for reproducible ML
- 🔍 **RAG-Ready Architecture**: Placeholders for retrieval-augmented generation workflows
- ⚡ **FastAPI + Streamlit**: High-performance REST API with interactive visualization layer
- 🗄️ **Vector & Graph DBs**: PostgreSQL/pgvector for embeddings, Neo4j for knowledge graphs
- 🆓 **100% Local**: Runs entirely on localhost, no cloud dependencies required

**Quick Links:** GitHub Repository | **Live Demo Ports:** API `:8000`, Dashboard `:8501`, MLflow `:5001`, Neo4j `:7474`

