#!/usr/bin/env bash
# See https://www.ory.sh/docs/hydra/5min-tutorial
set -euo pipefail

# shellcheck disable=SC2296
if [[ "${BASH_SOURCE[0]}" = */* ]]; then this_dir="${BASH_SOURCE[0]%/*}"; # bash
elif [ -n "${(%):-%N}" ]; then this_dir="${(%):-%N}";                     # zsh
else this_dir=.;
fi

# path setup
repo_root="$(cd "$this_dir/../.." && pwd)"
infra_root="$repo_root/infrastructure/dev"
dotenv="$infra_root/.env"
cd "$infra_root"

docker compose up -d

service_is_healthy() {
  curl -sf http://127.0.0.1:4445/health/ready > "$this_dir/.tmp.health.json" &&
    jq -e '.status' "$this_dir/.tmp.health.json" | grep -q "ok"
}

i=0
printf "Waiting for hydra to be healthy..."
while ! service_is_healthy; do
  printf "."
  i=$((i + 1))
  sleep 1
done
rm -f "$this_dir/.tmp.health.json"
printf " healthy in %d seconds\n" "$i"


client="$(
  docker-compose -f quickstart.yml exec hydra \
    hydra create client \
    --endpoint http://127.0.0.1:4445/ \
    --format json \
    --grant-type client_credentials
)"
client_id="$(echo "$client" | jq -r '.client_id')"
client_secret="$(echo "$client" | jq -r '.client_secret')"

touch "$dotenv"
sed -i "
  s/^CLIENT_ID=//g;
  s/^CLIENT_SECRET=//g;
" "$dotenv"
echo "CLIENT_ID=$client_id" >> "$dotenv"
echo "CLIENT_SECRET=$client_secret" >> "$dotenv"
