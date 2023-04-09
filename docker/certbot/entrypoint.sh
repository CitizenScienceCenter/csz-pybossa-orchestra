#!/bin/bash

# source: https://github.com/gchan/auto-letsencrypt/blob/master/entrypoint.sh

CHECK_FREQ="${CHECK_FREQ:-30}"

if [ ! -f /etc/ssl/certs/dhparam-2048-test.pem ]; then
	openssl dhparam -out /etc/ssl/certs/dhparam-2048-test.pem 2048
fi

check() {
  echo "* Starting webroot initial certificate request script..."

    certbot certonly --rsa-key-size 2048 --webroot --webroot-path=/var/www/certbot \
        --email ${ADMIN_EMAIL} --force-renewal --agree-tos --no-eff-email \
        -d ${HOST_NAME} -d www.${HOST_NAME}

  echo "* Certificate request process finished for domains ${HOST_NAME} www.${HOST_NAME}"

  echo "* Reloading Nginx configuration on webserver"
  eval docker kill -s SIGHUP webserver

  echo "* Next check in $CHECK_FREQ days"
  sleep ${CHECK_FREQ}d
  check
}

check