FROM python:3.11.3-alpine3.18

LABEL maintainer="alysson.silva364@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY desafio /desafio
COPY scripts /scripts

WORKDIR /desafio

EXPOSE 8000

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /desafio/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  mkdir -p /var/www/staticfiles && \
  mkdir -p /data/web/media/profile_pictures && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /desafio && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /var/www/staticfiles && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /desafio && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /var/www/staticfiles && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts

RUN pip install pytest

ENV PATH="/scripts:/venv/bin:$PATH"

USER duser

CMD ["commands.sh"]