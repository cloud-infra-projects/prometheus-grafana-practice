from fastapi import FastAPI
from prometheus_client import make_asgi_app, Counter, Summary
import time, random

app = FastAPI()

REQUEST_COUNT = Counter("http_requests_total", "Total HTTP requests", ["method", "endpoint"])
REQUEST_LATENCY = Summary("http_request_latency_seconds", "Request latency in seconds")

@app.get("/hello")
@REQUEST_LATENCY.time()
def hello():
    REQUEST_COUNT.labels(method="GET", endpoint="/hello").inc()
    time.sleep(random.uniform(0.1, 0.5))
    return {"message": "Hello from FastAPI"}

# /metrics 경로를 Prometheus가 스크랩 가능하도록 mount
app.mount("/metrics", make_asgi_app())
