FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install yt-dlp flask mutagen

WORKDIR /app
COPY app.py .
RUN mkdir -p /downloads

EXPOSE 5000
CMD ["python", "app.py"]
