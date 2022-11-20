FROM python:3.8.13-buster

COPY . .
RUN pip install --upgrade pip
RUN pip install -r --no-cache-dir requirements.txt

EXPOSE 5000
CMD ["python", "api.py"]