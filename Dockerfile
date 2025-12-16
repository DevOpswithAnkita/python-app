# ---------- Build stage ----------
FROM python:3.10-slim AS builder
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --prefix=/install -r requirements.txt

# ---------- Runtime stage ----------
FROM python:3.10-slim
WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY --from=builder /install /usr/local
COPY . .

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]
