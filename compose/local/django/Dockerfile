FROM python:3.5

# ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

ADD /requirements/local.txt $APP_HOME

RUN pip install gunicorn; \
    pip install -r /home/app/web/local.txt; mkdir /log; mkdir /code;

COPY /compose/local/django/entrypoint.sh $APP_HOME

COPY /src/ $APP_HOME

ENTRYPOINT ["/home/app/web/entrypoint.sh"]
RUN ["chmod", "+x", "/home/app/web/entrypoint.sh"]





