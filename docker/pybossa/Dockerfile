FROM --platform=linux/amd64 ubuntu:22.04 AS base
# FROM --platform=linux/amd64 python:3.8-slim AS base
LABEL ch.citizenscience.image.authors="daniel.boehler@uzh.ch" \
      ch.citizenscience.image.version="3.0"

## install dependencies
RUN apt-get update && apt-get install -y \
    git \
    gettext-base \
    python \
    python-setuptools \
    python3-dev \
    python3-pip \
    python3-virtualenv \
    python3-venv \
    postgresql \
    postgresql-server-dev-all \
    libpq-dev \
    python-psycopg2 \
    build-essential \
    libjpeg-dev \
    libssl-dev \
    swig \ 
    libffi-dev \
    dbus \
    libdbus-1-dev \
    libdbus-glib-1-dev \
    libsasl2-dev \
    libldap2-dev \ 
    && rm -rf /var/lib/apt/lists/*

## permissions and pybossa user for tightened security
RUN adduser pybossa
RUN mkdir /app && chown -R pybossa:pybossa /app
USER pybossa



FROM base AS dependencies
## venv
ENV APP_PATH=/app/pybossa
ENV VENV_PATH=/app/venv
RUN python3 -m venv ${VENV_PATH}
ENV PATH="${VENV_PATH}/bin:${PATH}"

## install dependencies
WORKDIR ${APP_PATH}

## copy requirements.txt file and install dependencies to avoid reinstall after dir changes
# COPY --chown=pybossa:pybossa docker/pybossa/requirements.txt ${APP_PATH}/requirements.txt 
# RUN pip install -r ${APP_PATH}/requirements.txt && \
#     rm ${APP_PATH}/requirements.txt

## [alternative]: install with locally adapted copy of requirements.txt
# COPY --chown=pybossa:pybossa pybossa/requirements.txt ${APP_PATH}/requirements.txt 
# COPY --chown=pybossa:pybossa pybossa/setup.py ${APP_PATH}/setup.py
# COPY --chown=pybossa:pybossa pybossa/pybossa/version.txt ${APP_PATH}/pybossa/version.txt
# RUN pip install -r ${APP_PATH}/requirements.txt

## clone pybossa into the container (from github)
# clone pybossa into the container (from github)
RUN git clone --recursive https://github.com/Scifabric/pybossa.git ${APP_PATH}
RUN pip install -r ${APP_PATH}/requirements.txt

## [alternative]: copy local copy of pybossa to the container
# COPY --chown=pybossa:pybossa pybossa ${APP_PATH}

# copy pybossa settings files to pybossa project
COPY --chown=pybossa:pybossa config/pybossa/settings_local.py ${APP_PATH}/settings_local.py



FROM dependencies AS pybossa-scheduler
LABEL ch.citizenscience.env="PROD"

## run scheduler
CMD ["rqscheduler", "--host", "redis-master", "--port", "6379", "--interval", "60" , "--db",  "0"]



FROM dependencies AS pybossa-worker
LABEL ch.citizenscience.env="PROD"

## copy alembic config files to pybossa project
COPY --chown=pybossa:pybossa config/alembic/templates/alembic.ini.template ${APP_PATH}/alembic.ini.template
COPY --chown=pybossa:pybossa --chmod=0755 docker/pybossa/entrypoint.sh /app/entrypoint.sh

## data base setup with env vars replacement for alembic config file based on different deployments (dev, test, stag, prod) 
ENTRYPOINT ["/app/entrypoint.sh"]

## run worker
CMD ["python", "app_context_rqworker.py", "scheduled_jobs", "super", "high", "medium", "low" , "email",  "maintenance"]



FROM dependencies AS pybossa-server
LABEL ch.citizenscience.env="PROD"

## install uwsgi for production 
RUN pip install uwsgi

# copy uwsgi config file to pybossa project
COPY --chown=pybossa:pybossa config/uwsgi/pybossa.ini ${APP_PATH}/pybossa.ini

## [optional]: download and install custom theme for pybossa server
# RUN git clone --recursive https://github.com/MicroPasts/MicroPasts-pybossa-theme ${APP_PATH}/pybossa/themes/MicroPasts-pybossa-theme

## run server (prod)
CMD ["/app/venv/bin/uwsgi", "--ini", "pybossa.ini"]
