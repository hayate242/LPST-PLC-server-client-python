FROM python:3.6.1-alpine
ADD ./python /code
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# CMD ["python", "app.py"]
CMD ["python", "server.py"]