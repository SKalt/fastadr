#!/usr/bin/env bash
# See https://www.ory.sh/docs/hydra/5min-tutorial
set -euo pipefail

# shellcheck disable=SC2296
if [[ "${BASH_SOURCE[0]}" = */* ]]; then this_dir="${BASH_SOURCE[0]%/*}"; # bash
elif [ -n "${(%):-%N}" ]; then this_dir="${(%):-%N}";                     # zsh
else this_dir=.;
fi

# path setup
repo_root="$(git rev-parse --show-toplevel)"
infra_root="$repo_root/infrastructure/dev"
dotenv="$repo_root/.env"
set -a
# shellcheck source=../../.env
[ -f "$dotenv" ] && . "$dotenv"
set +a 
cd "$infra_root"

CLIENT_ID="${CLIENT_ID:-}"

docker compose up -d

service_is_healthy() {
  curl -sf http://127.0.0.1:4445/health/ready > "$this_dir/.tmp.health.json" &&
    jq -e '.status' "$this_dir/.tmp.health.json" | grep -q "ok"
}

i=0
printf "Waiting for hydra to be healthy..." # podman-compose up --wait isn't yet supported
while ! service_is_healthy; do
  printf "."
  i=$((i + 1))
  sleep 1
done
rm -f "$this_dir/.tmp.health.json"
printf " healthy in %d seconds\n" "$i"

mkdir -p tmp


# TODO: figure out if custom jwks is needed
# docker compose exec hydra \
#   hydra create jwks \
#     --endpoint http://127.0.0.1:4445/ \
#     --alg RS256 \
#     --use sig \
#     --format json-pretty \
#     fastadr_jwks | tee ./tmp/fastadr_jwks.json 



_bl_scopes=(
  read_all
  write_programs
  write_events
  write_reports
  write_subscriptions
  write_vens
)
bl_scopes="$(IFS=,; echo "${_bl_scopes[*]}")"
_ven_scopes=(
  read_all
  write_reports
  write_subscriptions
  write_vens
)
ven_scopes="$(IFS=,; echo "${_ven_scopes[*]}")"

create_client() {
  local kind="$1"
  local name="$2"
  shift; shift;
  local scopes=""; scopes="$(IFS=,; echo "$*")"
  local file="./tmp/client.$kind.$name.json"
  echo "Creating client $name with scopes: $scopes"
  docker compose exec hydra \
    hydra create client \
      --endpoint http://127.0.0.1:4445/ \
      --format json-pretty \
      --grant-type client_credentials \
      --scope "$bl_scopes" | tee "$file"
}
check_client_exists() {
  local kind="$1"
  local name="$2"
  local file="./tmp/client.$kind.$name.json"
  if ! [ -f "$file" ]; then return 1; fi
  local client_id; client_id="$(jq -r '.client_id' "$file")"
  docker compose exec hydra \
    hydra get client "$client_id" \
    --endpoint http://127.0.0.1:4445/ >/dev/null 2>&1
}

ensure_client() {
  local kind="$1"
  local name="$2"
  shift; shift;
  local scopes=""; scopes="$(IFS=,; echo "$*")"
  local file="./tmp/client.$kind.$name.json"
  if ! check_client_exists "$kind" "$name"; then
    create_client "$kind" "$name" "$scopes"
  fi
}

get_token_for() {
  local kind="$1"
  local name="$2"
  shift; shift;
  local scopes=""; scopes="$(IFS=,; echo "$*")"
  local file="./tmp/client.$kind.$name.json"
  local client_id; client_id="$(jq -r '.client_id' "$file")"
  local client_secret; client_secret="$(jq -r '.client_secret' "$file")"
  docker compose exec hydra \
    hydra perform client-credentials \
      --endpoint http://127.0.0.1:4444/ \
      --client-id "$client_id" \
      --client-secret "$client_secret" \
      --format json-pretty \
      --scope "$scopes" \
    > "./tmp/token.$kind.$name.json"
  local token=; token="$(jq -r '.access_token' "./tmp/token.$kind.$name.json")"
  echo "${kind}_${name}_token=$token"
}

ensure_client bl a "${bl_scopes[@]}"
ensure_client bl b "${bl_scopes[@]}"

ensure_client ven x "${ven_scopes[@]}"
ensure_client ven y "${ven_scopes[@]}"

get_token_for bl a "${bl_scopes[@]}"
get_token_for bl b "${bl_scopes[@]}"

get_token_for ven x "${ven_scopes[@]}"
get_token_for ven y "${ven_scopes[@]}"
