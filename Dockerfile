
FROM python:3.6

RUN mkdir /app
WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Update
RUN apt-get update \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

ADD requirements.txt /app/
ADD src/main.py /app/

RUN pip install -r /app/requirements.txt

CMD [ "python", "main.py" ]