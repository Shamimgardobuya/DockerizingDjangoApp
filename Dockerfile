FROM python:3.10 AS builder

# Build dependencies for psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN pip install --upgrade pip 

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# --------------------------
# Stage 2: production
FROM python:3.10-slim

# Install runtime dependency (no compiler needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user and workdir
RUN useradd -m -r appuser && \
    mkdir -p /app/media && \
    chown -R appuser /app && \
    chmod -R 775 /app/media

WORKDIR /app

# Copy built dependencies from builder
COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Copy project files
COPY --chown=appuser:appuser . .

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

USER appuser

# For dev
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# For prod (uncomment later)
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "todo_list.wsgi:application"]
