# Full Docker Orchestration for pybossa

## Initial Setup Steps:
1. Running in OpenStack Cloud? Modify (or create – if it does not exist) the Docker daemon configuration file at /etc/docker/daemon.json and explicitly set the correct MTU size (accounting for the packet overhead). [_Details / Source_](https://platform9.com/kb/openstack/no-connectivity-to-docker-containers-within-instance)
```
{ "mtu": 1450}
```
2. Create .env.* files  – refer to [_config/env/README.md_](config/env/README.md)
    - .env.secrets
    - .env.mail
    - .env.dev
    - .env.deploy

UNIX vs. TCP sockets: https://blog.myhro.info/2017/01/benchmarking-ip-and-unix-domain-sockets-for-real

Kudos to the following tutorials:
- https://www.digitalocean.com/community/tutorials/how-to-secure-a-containerized-node-js-application-with-nginx-let-s-encrypt-and-docker-compose
- https://blog.devgenius.io/how-to-dockerize-a-production-ready-django-application-django-nginx-uwsgi-a908d3e4d8f8