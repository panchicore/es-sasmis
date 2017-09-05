#!/usr/bin/env bash

export SASMIS_FILE_PATH='/data/es-gdelt/data/realtime/*.CSV'
export SASMIS_UPLOAD_METHOD='requests'
export ES_HOST=http://localhost:9200/
export ES_USER=elastic
export ES_PASSWORD=changeme
export ES_SASMIS_INDEX=simsas
export SOURCE_URL=https://simsas.wfp.org/
export SLACK_NOTIFICATIONS_ENABLED=0
export SLACK_NOTIFICATIONS_URL=https://hooks.slack.com/services/XXXX/YYYYY/ZZZZZ
