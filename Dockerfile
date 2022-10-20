FROM python:3.9

ENV PYTHONUNBUFFERED 1


WORKDIR /rpa_api

COPY .src /rpa_api


RUN apt-get update 
    # \
    # && apt-get install -y gcc python3-dev
    # && apt-get install -y libffi-dev \
    # && apt-get install -y python3-dev libq-dev

RUN pip install -r /rpa_api/requirements.txt


RUN chmod +x /rpa_api/app_start

