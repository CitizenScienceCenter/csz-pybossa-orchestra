# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2013 SF Isle of Man Limited
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.

# Add env support for deployments
from os import environ as env

# DEBUG = True
# ENABLE_DEBUG_TOOLBAR = True 

## host for local development
# HOST = '0.0.0.0'

## PORT used for local development, in production environment let nginx handle this
# PORT = 8080

## use SERVER_NAME instead of HOST for production environment with real URLs
SERVER_NAME = env['HOST_NAME']

SECRET = env['FLASK_SESSIONS_SECRET']
SECRET_KEY = env['FLASK_SESSIONS_SECRET_KEY']

## Test URI overwrites value for testing purposes
SQLALCHEMY_DATABASE_URI = env['POSTGRES_URL']
# SQLALCHEMY_DATABASE_TEST_URI = 'postgresql://rtester:rtester@localhost/pybossa_test'

SQLALCHEMY_TRACK_MODIFICATIONS = False

## Slave configuration for DB
#SQLALCHEMY_BINDS = {
#    'slave': 'postgresql://user:password@server/db'
#}

ITSDANGEROUSKEY = env['ITSDANGEROUSKEY']

THEME = 'default'

## project configuration
BRAND = 'Citizen Science Zurich'
TITLE = 'Citizen Science Zurich'
LOGO = 'default_logo.svg'
COPYRIGHT = 'Citizen Science Zurich'
DESCRIPTION = 'Set the description in your config'
TERMSOFUSE = 'http://okfn.org/terms-of-use/'
DATAUSE = 'http://opendatacommons.org/licenses/by/'
CONTACT_EMAIL = 'info@citizenscience.ch'
CONTACT_TWITTER = 'citscizurich'

## Default number of projects per page
# APPS_PER_PAGE = 20

## External Auth providers
TWITTER_CONSUMER_KEY = env['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = env['TWITTER_CONSUMER_SECRET']

## Supported Languages
## NOTE: You need to create a symbolic link to the translations folder, otherwise
## this wont work.
## ln -s pybossa/themes/your-theme/translations pybossa/translations
#DEFAULT_LOCALE = 'en'
#LOCALES = [('en', 'English'), ('es', u'Español'),
#           ('it', 'Italiano'), ('fr', u'Français'),
#           ('ja', u'日本語'),('pt_BR','Brazilian Portuguese')]


## list of administrator emails to which error emails get sent
ADMINS = [env['ADMIN_EMAIL']]

## CKAN URL for API calls
#CKAN_NAME = "Demo CKAN server"
#CKAN_URL = "http://demo.ckan.org"


## logging config
## Sentry configuration
# SENTRY_DSN=''
## set path to enable
# LOG_FILE = '/path/to/log/file'
## Optional log level
# import logging
# LOG_LEVEL = logging.DEBUG

## Mail setup
MAIL_SERVER = env['MAIL_SERVER']
MAIL_USERNAME = env['MAIL_USERNAME']
MAIL_PASSWORD = env['MAIL_PW']
MAIL_PORT = env['MAIL_PORT']
MAIL_USE_SSL = True
MAIL_FAIL_SILENTLY = False
MAIL_DEFAULT_SENDER = env['MAIL_DEFAULT_SENDER']

## SPAM protection
# SPAM = ['spam.com', 'fake.es']

## Announcement messages
## Use any combination of the next type of messages: root, user, and app owners
# ANNOUNCEMENT = {'admin': 'Root Message', 'user': 'User Message', 'owner': 'Owner Message'}

## Enforce Privacy Mode, by default is disabled
## This config variable will disable all related user pages except for admins
## Stats, top users, leaderboard, etc
ENFORCE_PRIVACY = False


## Cache setup. By default it is enabled
## Redis Sentinel
# List of Sentinel servers (IP, port)
# REDIS_CACHE_ENABLED = False
REDIS_SENTINEL = [('redis-sentinel', 26379)]
REDIS_MASTER = 'mymaster'
REDIS_DB = 0
REDIS_KEYPREFIX = 'pybossa_cache'
REDIS_SOCKET_TIMEOUT = None
REDIS_RETRY_ON_TIMEOUT = True

## Redis Settings for no-sentinel setup
REDIS_HOST = 'redis-master'
REDIS_PORT = 6379
# REDIS_PASSWORD = 'your-password'

## For RQ-DASHBOARD
REDIS_URL = 'redis://redis-master:6379'

## Allowed upload extensions
ALLOWED_EXTENSIONS = ['js', 'css', 'png', 'jpg', 'jpeg', 'gif', 'zip']

## If you want to use the local uploader configure which folder
UPLOAD_METHOD = 'local'
UPLOAD_FOLDER = '/app/uploads'

## If you want to use Rackspace for uploads, configure it here
# RACKSPACE_USERNAME = 'username'
# RACKSPACE_API_KEY = 'apikey'
# RACKSPACE_REGION = 'ORD'

## Default number of users shown in the leaderboard
# LEADERBOARD = 20
## Default shown presenters
# PRESENTERS = ["basic", "image", "sound", "video", "map", "pdf"]
# Default Google Docs spreadsheet template tasks URLs
TEMPLATE_TASKS = {
    'image': "https://docs.google.com/spreadsheet/ccc?key=0AsNlt0WgPAHwdHFEN29mZUF0czJWMUhIejF6dWZXdkE&usp=sharing",
    'sound': "https://docs.google.com/spreadsheet/ccc?key=0AsNlt0WgPAHwdEczcWduOXRUb1JUc1VGMmJtc2xXaXc&usp=sharing",
    'video': "https://docs.google.com/spreadsheet/ccc?key=0AsNlt0WgPAHwdGZ2UGhxSTJjQl9YNVhfUVhGRUdoRWc&usp=sharing",
    'map': "https://docs.google.com/spreadsheet/ccc?key=0AsNlt0WgPAHwdGZnbjdwcnhKRVNlN1dGXy0tTnNWWXc&usp=sharing",
    'pdf': "https://docs.google.com/spreadsheet/ccc?key=0AsNlt0WgPAHwdEVVamc0R0hrcjlGdXRaUXlqRXlJMEE&usp=sharing"}

# Expiration time for password protected project cookies
PASSWD_COOKIE_TIMEOUT = 60 * 30

# Expiration time for account confirmation / password recovery links
ACCOUNT_LINK_EXPIRATION = 5 * 60 * 60

# Ratelimit configuration (API)
LIMIT = 300
PER = 5 * 60

## Project cache
# APP_TIMEOUT = 15 * 60
# REGISTERED_USERS_TIMEOUT = 15 * 60
# ANON_USERS_TIMEOUT = 5 * 60 * 60
# STATS_FRONTPAGE_TIMEOUT = 12 * 60 * 60
# STATS_APP_TIMEOUT = 12 * 60 * 60
# STATS_DRAFT_TIMEOUT = 24 * 60 * 60
# N_APPS_PER_CATEGORY_TIMEOUT = 60 * 60
# BROWSE_TASKS_TIMEOUT = 3 * 60 * 60
## Category cache
# CATEGORY_TIMEOUT = 24 * 60 * 60
## User cache
# USER_TIMEOUT = 15 * 60
# USER_TOP_TIMEOUT = 24 * 60 * 60
# USER_TOTAL_TIMEOUT = 24 * 60 * 60

# Disable new account confirmation (via email)
ACCOUNT_CONFIRMATION_DISABLED = False

# Disable blog post updates
DISABLE_EMAIL_NOTIFICATIONS = True

## Mailchimp API key
# MAILCHIMP_API_KEY = "your-key"
# MAILCHIMP_LIST_ID = "your-list-ID"

# Flickr API key and secret
FLICKR_API_KEY = env['FLICKR_API_KEY']
FLICKR_SHARED_SECRET = env['FLICKR_SHARED_SECRET']

# Dropbox app key
DROPBOX_APP_KEY = env['DROPBOX_APP_KEY']

## Send emails weekly update every
# WEEKLY_UPDATE_STATS = 'Sunday'

## Youtube API server key
YOUTUBE_API_SERVER_KEY = 'your-key'

# Enable Server Sent Events
# WARNING: this will require to run PyBossa in async mode. Check the docs.
# WARNING: if you don't enable async when serving PyBossa, the server will lock
# WARNING: and it will not work. For this reason, it's disabled by default.
SSE = False

# Add here any other ATOM feed that you want to get notified.
NEWS_URL = ['https://github.com/Scifabric/enki/releases.atom',
            'https://github.com/Scifabric/pybossa-client/releases.atom',
            'https://github.com/Scifabric/pbs/releases.atom']

# Pro user features. False will make the feature available to all regular users,
# while True will make it available only to pro users
PRO_FEATURES = {
    'auditlog':              True,
    'webhooks':              True,
    'updated_exports':       True,
    'notify_blog_updates':   True,
    'project_weekly_report': True,
    'autoimporter':          True,
    'better_stats':          True
}


# Libsass style. You can use nested, expanded, compact and compressed
LIBSASS_STYLE = 'compressed'

# CORS resources configuration.
# WARNING: Only modify this if you know what you are doing. The below config
# are the defaults, allowing PYBOSSA to have full CORS api.
# For more options, check the Flask-Cors documentation: https://flask-cors.readthedocs.io/en/latest/
# CORS_RESOURCES = {r"/api/*": {"origins": "*",
#                               "allow_headers": ['Content-Type',
#                                                 'Authorization'],
#                               "methods": "*"
#                               }}

## Email notifications for background jobs.
# FAILED_JOBS_MAILS = 7
# FAILED_JOBS_RETRIES = 3

# Language to use stems, full text search, etc. from postgresql.
# FULLTEXTSEARCH_LANGUAGE = 'english'


# Use strict slashes at endpoints, by default True
# This will return a 404 if and endpoint does not have the api/endpoint/
# while if you configured as False, it will return the resource with and without the trailing /
# STRICT_SLASHES = True

## Use SSO on Disqus.com
# DISQUS_SECRET_KEY = 'secret-key'
# DISQUS_PUBLIC_KEY = 'public-key'

## Use Web Push Notifications
# ONESIGNAL_APP_ID = 'Your-app-id'
# ONESIGNAL_API_KEY = 'your-app-key'


## Enable two factor authentication
# ENABLE_TWO_FACTOR_AUTH = True

## Strong password policy for user accounts
# ENABLE_STRONG_PASSWORD = True

## Create new leaderboards based on info field keys from user
# LEADERBOARDS = ['foo', 'bar']

## Unpublish inactive projects
# UNPUBLISH_PROJECTS = True

## Use this config variable to create valid URLs for your SPA
SPA_SERVER_NAME =  'https://' + env['HOST_NAME']

## LDAP
# LDAP_HOST = '127.0.0.1'
# LDAP_BASE_DN = 'ou=users,dc=scifabric,dc=com'
# LDAP_USERNAME = 'cn=yourusername,dc=scifabric,dc=com'
# LDAP_PASSWORD = 'yourpassword'
# LDAP_OBJECTS_DN = 'dn'
# LDAP_OPENLDAP = True
# Adapt it to your specific needs in your LDAP org
# LDAP_USER_OBJECT_FILTER = '(&(objectclass=inetOrgPerson)(cn=%s))'
# LDAP_USER_FILTER_FIELD = 'cn'
# LDAP_PYBOSSA_FIELDS = {'fullname': 'givenName',
#                        'name': 'uid',
#                        'email_addr': 'cn'}
## Flask profiler
# FLASK_PROFILER = {
#     "enabled": True,
#     "storage": {
#         "engine": "sqlite"
#     },
#     "basicAuth":{
#         "enabled": True,
#         "username": "admin",
#         "password": "admin"
#     },
#     "ignore": [
# 	    "^/static/.*"
# 	]
# }
## Specify which key from the info field of task, task_run or result is going to be used as the root key
## for exporting in CSV format
# TASK_CSV_EXPORT_INFO_KEY = 'key'
# TASK_RUN_CSV_EXPORT_INFO_KEY = 'key2'
# RESULT_CSV_EXPORT_INFO_KEY = 'key3'

## Making extra key/value pairs in info field public
# PROJECT_INFO_PUBLIC_FIELDS = ['key1', 'key2']
# USER_INFO_PUBLIC_FIELDS = ['badges', 'key2']
# CATEGORY_INFO_PUBLIC_FIELDS = ['key1', 'key2']

## Add historical contribuations as category
HISTORICAL_CONTRIBUTIONS_AS_CATEGORY = True

## Ignore specific keys when exporting data in CSV format
# IGNORE_FLAT_KEYS = [ 'geojson', 'key1', ...]

# A 32 char string for AES encryption of public IPs.
# NOTE: this is really important, don't use the following one
# as anyone with the source code of pybossa will be able to reverse
# the anonymization of the IPs.
CRYPTOPAN_KEY = env['CRYPTOPAN_KEY']

## TTL for ZIP files of personal data
TTL_ZIP_SEC_FILES = 3

## Instruct PYBOSSA to generate HTTP or HTTPS
PREFERRED_URL_SCHEME='https'

## Instruct PYBOSSA to generate absolute paths or not for avatars
AVATAR_ABSOLUTE = True

# Inactive users months to send email notification
USER_INACTIVE_NOTIFICATION = 5

## Inactive users months to delete users
USER_DELETE_AFTER_NOTIFICATION = '1 month'

## Inactive users email SQL query
INACTIVE_USERS_SQL_QUERY = """SELECT user_id FROM task_run WHERE user_id IS NOT NULL AND to_date(task_run.finish_time, 'YYYY-MM-DD\THH24:MI:SS.US') >= NOW() - '12 month'::INTERVAL AND to_date(task_run.finish_time, 'YYYY-MM-DD\THH24:MI:SS.US') < NOW() - '3 month'::INTERVAL GROUP BY user_id ORDER BY user_id;"""

## When you are using PYBOSSA native JSON support, you will not be building your project presenter within the PYBOSSA structure, but within the JS framework of your choice.
## In such a case, you would like to disable the check for the task_presenter when publishing a project. 
## If you need this, just add this flag to your settings_local.py file:
DISABLE_TASK_PRESENTER = True
