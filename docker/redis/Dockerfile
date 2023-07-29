FROM  redis:latest AS replica
LABEL ch.citizenscience.image.authors="daniel.boehler@uzh.ch" \
      ch.citizenscience.image.version="1.0"
COPY ./config/redis-replica/replica.conf /usr/local/etc/redis/replica.conf
CMD ["redis-server", "/usr/local/etc/redis/replica.conf"]



FROM  redis:latest AS sentinel
LABEL ch.citizenscience.image.authors="daniel.boehler@uzh.ch" \
      ch.citizenscience.image.version="1.0"
COPY ./config/redis-sentinel/sentinel.conf /usr/local/etc/redis/sentinel.conf
CMD ["redis-server", "/usr/local/etc/redis/sentinel.conf",  "--sentinel"]



FROM  redis:latest AS master
LABEL ch.citizenscience.image.authors="daniel.boehler@uzh.ch" \
      ch.citizenscience.image.version="1.0"
COPY ./config/redis-master/master.conf /usr/local/etc/redis/master.conf
CMD ["redis-server", "/usr/local/etc/redis/master.conf"]