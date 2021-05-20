FROM pymesh/pymesh:py3.7

RUN apt-get update && apt-get install -y \
    ffmpeg \
    && apt-get -y autoremove && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/
RUN pip --no-cache-dir install -r /tmp/requirements.txt

WORKDIR /project

CMD [ "bash" ]