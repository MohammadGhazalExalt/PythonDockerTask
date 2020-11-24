FROM python:3.8

WORKDIR /code

RUN pip install flask
RUN pip install flask-sqlalchemy
RUN pip install pymysql
RUN pip install cryptography
COPY src/ .
RUN chmod +x api.py
CMD [ "python", "./api.py" ]
