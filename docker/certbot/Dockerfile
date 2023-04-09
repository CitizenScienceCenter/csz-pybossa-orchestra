FROM certbot/certbot:latest AS base
LABEL ch.citizenscience.image.authors="daniel.boehler@uzh.ch" \
      ch.citizenscience.image.version="2.0"

## copy entrypoint script to certbot image
COPY --chmod=0755 docker/certbot/entrypoint.sh /entrypoint.sh

## data base setup with env vars replacement for alembic config file based on different deployments (dev, test, stag, prod) 
ENTRYPOINT ["/entrypoint.sh"]

