FROM python:3.5-slim
COPY . .
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 5000
CMD python3 server.py