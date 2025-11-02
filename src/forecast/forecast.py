from datetime import datetime, timedelta, timezone

def fake_forecast(days: int = 7, start_value: float = 100.0):
    base = start_value
    out = []
    for i in range(days):
        dt = datetime.now(timezone.utc) + timedelta(days=i+1)
        val = base + i * 1.5
        out.append({"date": dt.isoformat(), "predicted": round(val, 2), "low": round(val-3, 2), "high": round(val+3, 2)})
    return out
