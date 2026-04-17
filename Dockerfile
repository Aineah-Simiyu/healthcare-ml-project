FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install dependencies using uv and the lockfile
COPY pyproject.toml uv.lock ./
RUN uv pip install --system -e . && \
    uv pip install --system asyncpg

# Copy application code
COPY . .

# Environment
ENV PYTHONPATH=/app
ENV AIRFLOW_HOME=/app/airflow

EXPOSE 5000
