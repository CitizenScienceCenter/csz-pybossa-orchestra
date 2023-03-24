FROM --platform=linux/amd64 python:3.8-slim AS base
LABEL c3s.pb.image.authors="daniel.boehler@uzh.ch" \
      c3s.pb.image.version="1.0"

# install dependencies
RUN apt-get update && apt-get install -y \
    git \
    gettext-base \
    postgresql \
    postgresql-server-dev-all \
    libpq-dev \
    python3-psycopg2 \
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

# permissions and pybossa user for tightened security
RUN adduser pybossa
RUN mkdir /app && chown -R pybossa:pybossa /app
USER pybossa

FROM base AS dependencies

# venv
ENV APP_PATH=/app/pybossa
ENV VENV_PATH=/app/venv
RUN python3 -m venv ${VENV_PATH}
ENV PATH="${VENV_PATH}/bin:${PATH}"

# clone pybossa into the container (from github)
WORKDIR /app/pybossa
RUN git clone --recursive https://github.com/Scifabric/pybossa /app/pybossa && \
    pip install --upgrade pip && \
    pip install -r /app/pybossa/requirements.txt

RUN pip install uwsgi
# install dropbox?

# alternative: copy local copy of pybossa to the container
# WORKDIR /app/pybossa
# COPY --chown=pybossa:pybossa apps/pybossa /app/pybossa
# RUN pip install --upgrade pip && \
#     pip install -r /app/pybossa/requirements.txt
    
# reinstall older versions of broken dependencies
RUN pip install 'requests-oauthlib==1.0.0' --force-reinstall && \
    pip install 'oauthlib==2.1.0' --force-reinstall && \
    pip install 'sqlalchemy<2.0' --force-reinstall

FROM dependencies AS configs

# copy static config files to pybossa project
COPY --chown=pybossa:pybossa config/pybossa/settings_local.py /app/pybossa/settings_local.py
COPY --chown=pybossa:pybossa config/uwsgi/pybossa.ini /app/pybossa/pybossa.ini
COPY --chown=pybossa:pybossa config/alembic/templates/alembic.ini.template /app/pybossa/alembic.ini.template
#COPY --chown=pybossa:pybossa templates/index.html /app/pybossa/pybossa/themes/default/templates/admin/index.html

# replace env vars based on different deployments (dev, test, stag, prod) 
COPY --chown=pybossa:pybossa --chmod=0755 docker/pybossa/entrypoint.sh /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

# Run the application
EXPOSE 8080

CMD ["/app/venv/bin/uwsgi", "--ini", "pybossa.ini"]
