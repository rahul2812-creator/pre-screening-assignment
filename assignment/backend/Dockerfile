FROM python:3.9
WORKDIR /app
COPY requirements.txt ./
RUN apt update && apt install -y postgresql-client && \
pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000","--reload"]
