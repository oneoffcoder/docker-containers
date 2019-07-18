#!/bin/bash

CONFIG_FILE=/usr/share/nginx/html/env.json

echo "{" >> ${CONFIG_FILE}
compgen -v | while read line
  do
    echo "\"$line\": \"${!line}\"," >> ${CONFIG_FILE}
done
echo "\"done\": true" >> ${CONFIG_FILE}
echo "}" >> ${CONFIG_FILE}

exit 0