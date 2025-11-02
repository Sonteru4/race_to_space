import os
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="RSI-X Dashboard", layout="wide")
st.title("🚀 RSI-X Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Health")
    try:
        r = requests.get(f"{API_URL}/health", timeout=5)
        st.json(r.json())
    except Exception as e:
        st.error(f"API not reachable: {e}")

with col2:
    st.subheader("Top Topics")
    limit = st.slider("How many topics?", 1, 20, 10)
    try:
        r = requests.get(f"{API_URL}/topics", params={"limit": limit}, timeout=10)
        items = r.json().get("items", [])
        st.table(items)
    except Exception as e:
        st.error(f"Failed to fetch topics: {e}")

st.subheader("Forecast (demo)")
days = st.slider("Days ahead", 1, 30, 7, key="forecast_days")
try:
    r = requests.get(f"{API_URL}/forecast", params={"days": days}, timeout=10)
    items = r.json().get("items", [])
    if items:
        st.line_chart({ "predicted": [x["predicted"] for x in items] })
        st.caption("Simple placeholder forecast")
    else:
        st.info("No forecast data.")
except Exception as e:
    st.error(f"Failed to fetch forecast: {e}")
