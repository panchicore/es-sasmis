#!/usr/bin/env bash

export SASMIS_FILE_PATH='/Users/panchicore/www/es-gdelt/data/realtime/*.CSV'
export ES_HOST=http://localhost:9200/
export ES_USER=elastic
export ES_PASSWORD=changeme
export ES_GDELT_INDEX=sasmis
export SOURCE_URL=http://localhost:8000/
export SLACK_NOTIFICATIONS_ENABLED=1
export SLACK_NOTIFICATIONS_URL=https://hooks.slack.com/services/XXXX/YYYYY/ZZZZZ