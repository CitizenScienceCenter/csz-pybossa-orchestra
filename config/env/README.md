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
Contains postgresql configuration for production environment. Example shows connection to database running on host in same local network (with dns-service).
```
# Configuration for pybossa database
POSTGRES_PASSWORD=<postgres-pw>
POSTGRES_HOST=testing-db-primary.csz.internal
POSTGRES_URL=postgresql://pybossa:${POSTGRES_PASSWORD}@${POSTGRES_HOST}/pybossa
```