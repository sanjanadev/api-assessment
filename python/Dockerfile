FROM python:3.8-alpine

RUN apk add --no-cache postgresql-libs \
    && apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev \
    && apk add --no-cache postgresql-client

ADD . /mnt/

WORKDIR /mnt/

RUN pip install -r requirements.txt \
    && addgroup -S appgroup && adduser -S appuser -G appgroup  \
    && chown -R appuser:appgroup /mnt/

USER appuser

ENTRYPOINT ["ash", "docker-entrypoint.sh"]
