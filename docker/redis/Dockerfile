FROM  redis:latest AS redis-replica
LABEL ch.citizenscience.image.authors="daniel.boehler@uzh.ch" \
      ch.citizenscience.image.version="1.0"
COPY --chown=redis:redis --chmod=0755 ./config/redis-replica/replica.conf /usr/local/etc/redis/replica.conf
CMD ["redis-server", "/usr/local/etc/redis/replica.conf"]



FROM  redis:latest AS redis-sentinel
LABEL ch.citizenscience.image.authors="daniel.boehler@uzh.ch" \
      ch.citizenscience.image.version="1.0"
COPY --chown=redis:redis --chmod=0755 ./config/redis-sentinel/sentinel.conf /usr/local/etc/redis/sentinel.conf
CMD ["redis-server", "/usr/local/etc/redis/sentinel.conf",  "--sentinel"]