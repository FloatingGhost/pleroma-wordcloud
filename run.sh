#!/bin/bash
set -euxo pipefail
psql -tc "select data->>'content' from objects where data->>'type'='Note' and data->>'id' like 'https://$1%'" pleroma_dev > words.txt
pipenv run python proc.py
pipenv run wordcloud_cli --text words.final.txt --imagefile cloud.png --width 2000 --height 2000
pipenv run python run.py
