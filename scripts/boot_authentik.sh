#!/usr/bin/env bash
docker compose up -d
# check if localhost:9000 is up
printf waiting
while ! curl -sf http://localhost:9000 > /dev/null; do
  printf '.'
  sleep 1
done
echo
