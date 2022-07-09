FROM python:3.8-bullseye
COPY requirements.txt .
# RUN /usr/local/bin/python -m pip install --upgrade pip
# RUN /usr/local/bin/python -m pip install flask uWSGI
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
# RUN apt-get update
# RUN adduser myuser
# USER myuser
ENV PATH="/home/myuser/.local/bin:${PATH}"


# RUN pip install -r requirements.txt

RUN apt-get update &&\
    /usr/local/bin/python3 -m pip install --upgrade pip &&\
    /usr/local/bin/python3 -m pip install --upgrade setuptools &&\
    /usr/local/bin/python3 -m pip install -r requirements.txt &&\
    adduser myuser

WORKDIR /home/myuser

COPY --chown=myuser:myuser . .

CMD ["uwsgi", "app/app.ini"]
