FROM python:3.13-slim

RUN python -m pip install --no-cache-dir \
    pytest==9.0.2 \
    ruff==0.12.7 \
    mypy==1.17.0

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TMPDIR=/tmp

WORKDIR /workspace
ENTRYPOINT []
