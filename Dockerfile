FROM python:3.8-bullseye
COPY requirements.txt .
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV PATH="/home/myuser/.local/bin:${PATH}"

RUN apt-get update &&\
    /usr/local/bin/python3 -m pip install --upgrade pip &&\
    /usr/local/bin/python3 -m pip install --upgrade setuptools &&\
    /usr/local/bin/python3 -m pip install -r requirements.txt &&\
    adduser myuser

WORKDIR /home/myuser

COPY --chown=myuser:myuser . .

CMD ["uwsgi", "app/app.ini"]
