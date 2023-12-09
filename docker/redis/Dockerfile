FROM  redis:latest AS redis-replica
LABEL ch.citizenscience.image.authors="daniel.boehler@uzh.ch" \
      ch.citizenscience.image.version="1.0"
COPY --chown=redis:redis ./config/redis-replica/replica.conf /usr/local/etc/redis/replica.conf
CMD ["redis-server", "/usr/local/etc/redis/replica.conf"]



FROM  redis:latest AS redis-sentinel
LABEL ch.citizenscience.image.authors="daniel.boehler@uzh.ch" \
      ch.citizenscience.image.version="1.0"
COPY --chown=redis:redis ./config/redis-sentinel/sentinel.conf /usr/local/etc/redis/sentinel.conf

EXPOSE 26379 

CMD ["redis-server", "/usr/local/etc/redis/sentinel.conf",  "--sentinel"]