FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        ffmpeg \
        git \
        libsndfile1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src

RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir .

COPY example_for_mac.py example_tts.py example_vc.py gradio_tts_app.py gradio_vc_app.py multilingual_app.py ./

EXPOSE 7860

CMD ["python", "gradio_tts_app.py"]

