FROM python:3.6

RUN apt-get update
RUN apt-get install -y libxmlsec1-dev

ENV PYTHONUNBUFFERED 1

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt \
    && groupadd -r django \
    && useradd -r -g django django

RUN pip install uwsgi==2.0.14

COPY . /app
RUN chown -R django /app

COPY ./start.sh /start.sh
RUN sed -i 's/\r//' /start.sh \
    && chmod +x /start.sh \
    && chown django /start.sh

WORKDIR /app

CMD /start.sh
