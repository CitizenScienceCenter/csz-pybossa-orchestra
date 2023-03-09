FROM --platform=linux/amd64 python:3.8-slim AS base
LABEL c3s.pb.image.authors="daniel.boehler@uzh.ch" \
      c3s.pb.image.version="1.0"

# install dependencies
RUN apt-get update && apt-get install -y \
    git \
    gettext-base \
    supervisor \
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
    
# alternative: local copy of pybossa to the container
# COPY --chown=pybossa:pybossa <pybossa-dir> /app/pybossa
# RUN pip install -r /app/pybossa/requirements.txt

# reinstall older versions of broken dependencies
RUN pip install 'requests-oauthlib==1.0.0' --force-reinstall && \
    pip install 'oauthlib==2.1.0' --force-reinstall && \
    pip install 'sqlalchemy<2.0' --force-reinstall

#rq==0.13.0
#rq-dashboard==0.3.12
#rq-scheduler==0.9

FROM dependencies AS configs

# copy static config files to pybossa project
COPY --chown=pybossa:pybossa config/pybossa/settings_local.py /app/pybossa/settings_local.py
COPY --chown=pybossa:pybossa config/supervisor/ /etc/supervisor/conf.d/
COPY --chown=pybossa:pybossa config/uwsgi/pybossa.ini /app/pybossa/pybossa.ini
COPY --chown=pybossa:pybossa config/alembic/templates/alembic.ini.template /app/pybossa/alembic.ini.template
COPY --chown=pybossa:pybossa templates/index.html /app/pybossa/pybossa/themes/default/templates/admin/index.html

# replace env vars based on different deployments (dev, test, stag, prod) 
COPY --chown=pybossa:pybossa --chmod=0755 apps/pybossa/entrypoint.sh /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

# Run the application
EXPOSE 8080

#CMD ["python", "/app/pybossa/cli.py",  "db_create"]
CMD ["python", "run.py"]
#CMD ["/usr/bin/supervisord"]