FROM --platform=linux/amd64 node:latest AS base
LABEL c3s.web.image.authors="daniel.boehler@uzh.ch" \
      c3s.web.image.version="1.0"

# install dependencies
RUN apt-get update && apt-get install -y \
    git \
    yarnpkg \
    && rm -rf /var/lib/apt/lists/*

RUN adduser c3s
RUN mkdir /app && chown -R c3s:c3s /app
USER c3s

FROM base AS build

# clone pybossa into the container (from github)
WORKDIR /app/c3s-lab-client
RUN git clone --recursive https://github.com/CitizenScienceCenter/c3s-lab-client /app/c3s-lab-client

# alternative: local copy of c3s to the container
# COPY --chown=c3s:c3s <c3s-dir> /app/c3s-lab-client

RUN yarnpkg install && yarnpkg build

# replace env vars based on different deployments (dev, test, stag, prod) 
# build application
#COPY --chown=c3s:c3s --chmod=0755 docker/c3s-lab-client/entrypoint.sh /app/entrypoint.sh
#ENTRYPOINT ["/app/entrypoint.sh"]

FROM nginx:latest as production
COPY --from=build /app/c3s-lab-client/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

