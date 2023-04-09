## Full Docker Orchestration for pybossa

### Initial Setup Steps:
1. Create Diffie-Hellmann key – refer to [_config/nginx/dhparam/README.md_](config/nginx/dhparam/README.md)
2. Running in OpenStack Cloud? Modify (or create – if it does not exist) the Docker daemon configuration file at /etc/docker/daemon.json and explicitly set the correct MTU size (accounting for the packet overhead). [_Details / Source_](https://platform9.com/kb/openstack/no-connectivity-to-docker-containers-within-instance)
```
{ "mtu": 1450}
```
3. Create .env.* files
    - .env.secrets
    - .env.mail
    - .env.dev
    - .env.prod

#### .env.secrets
Contains secrets for pybossa dependencies. Generate a different 32-char-key for each of the following vars
```
FLASK_SESSIONS_SECRET=<32-char-str>
FLASK_SESSIONS_SECRET_KEY=<32-char-str>
CRYPTOPAN_KEY=<32-char-str>
ITSDANGEROUSKEY=<32-char-str>
```
#### .env.mail
Contains configuration of the mail server pybossa uses to send its system emails
```
MAIL_PW=<mail-pw>
MAIL_SERVER=asmtp.mailstation.ch
MAIL_USERNAME=no-reply@citizenscience.ch
MAIL_PORT=465
MAIL_DEFAULT_SENDER='C3S Project Builder<no-reply@citizenscience.ch>'
```

#### .env.dev
Contains postgresql configuration for development environment (default). Example shows connection to local database running in docker container on the same host.
```
# Configuration for pybossa database
POSTGRES_PASSWORD=<postgres-pw>
POSTGRES_HOST=postgres
POSTGRES_URL=postgresql://pybossa:${POSTGRES_PASSWORD}@${POSTGRES_HOST}/pybossa
```

#### .env.prod
Contains postgresql configuration for production environment with ssl-certificates. Example shows connection to database running on host in same local network (with dns-service).
```
# Configuration for pybossa database
POSTGRES_PASSWORD=<postgres-pw>
POSTGRES_HOST=db-master-testing.c3s.internal
POSTGRES_URL=postgresql://pybossa:${POSTGRES_PASSWORD}@${POSTGRES_HOST}/pybossa

# Configuration for domain and networking
HOST_NAME=pybossa-testing.citizenscience.ch
ADMIN_EMAIL=dev@citizenscience.ch
```

UNIX vs. TCP sockets: https://blog.myhro.info/2017/01/benchmarking-ip-and-unix-domain-sockets-for-real

Kudos to the following tutorials:
- https://www.digitalocean.com/community/tutorials/how-to-secure-a-containerized-node-js-application-with-nginx-let-s-encrypt-and-docker-compose
- https://blog.devgenius.io/how-to-dockerize-a-production-ready-django-application-django-nginx-uwsgi-a908d3e4d8f8