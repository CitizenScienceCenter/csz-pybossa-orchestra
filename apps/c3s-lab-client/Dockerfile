FROM node:latest AS base
LABEL c3s.web.image.authors="daniel.boehler@uzh.ch" \
      c3s.web.image.version="1.0"

# install dependencies
RUN apt-get update && apt-get install -y \
    git \
    yarnpkg \
    && rm -rf /var/lib/apt/lists/*

# permissions and pybossa user for tightened security
RUN adduser c3s
RUN mkdir /app && chown -R c3s:c3s /app
USER c3s

FROM base AS dependencies

# clone pybossa into the container (from github)
WORKDIR /app/c3s-lab-client
RUN git clone --recursive https://github.com/CitizenScienceCenter/c3s-lab-client /app/c3s-lab-client

RUN yarnpkg install

    
# alternative: local copy of c3s-lab-client to the container
# COPY --chown=c3s:c3s <c3s-dir> /c3s-lab-client
# RUN yarn install

CMD ["yarnpkg", "run", "dev"]

