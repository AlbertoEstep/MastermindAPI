FROM alpine:3.17

RUN apk add --no-cache python3-dev \
    && apk add py3-pip \
    && pip3 install --upgrade pip

WORKDIR /mastermind

COPY . /mastermind

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "src/mastermind_api.py"]