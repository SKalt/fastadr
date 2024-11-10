#!/usr/bin/env bash
import subprocess
import time
import requests
import requests.cookies
import logging

logging.basicConfig(level=logging.INFO)
root_log = logging.getLogger(__name__)


def start_docker_compose():
    subprocess.run(["docker", "compose", "up", "-d"], check=True)


def wait_for_authentik():
    # write to stdout
    print("waiting", end="")
    time.sleep(10)  # the first boot is slow as hell
    while True:
        time.sleep(1)
        print(".", end="")
        try:
            response = requests.get("http://localhost:9000")
            response.raise_for_status()
            break
        except requests.exceptions.RequestException:
            pass
    print()


def set_initial_password():
    log = root_log.getChild("set_initial_password")
    root_log.setLevel(logging.DEBUG)
    initial_setup_url = "http://localhost:9000/if/flow/initial-setup/"
    default_headers = {
        "Host": "localhost:9000",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0",
    }
    cookies = requests.cookies.RequestsCookieJar()
    resp = requests.get(
        initial_setup_url,
        cookies=cookies,
        headers={**default_headers},
    )
    log.debug("fetch::%s %s", initial_setup_url, resp)
    assert resp.ok, resp.text
    csrf = resp.cookies.get("authentik-csrf")
    cx = resp.headers.get("Set-Cookie")
    if cx:
        print(cx)
    assert csrf, resp.cookies
    url = "http://localhost:9000/api/v3/flows/executor/initial-setup/?query="
    resp = requests.get(
        url,
        allow_redirects=False,
        cookies=resp.cookies,
        headers={
            **default_headers,
            "referrer": initial_setup_url,
            "origin": "http://localhost:9000",
            **({"X-authentik-csrf": csrf} if csrf else {}),
        },
    )
    log.debug("fetch::%s %s", url, resp)
    assert resp.is_redirect, resp.text
    location = resp.headers["Location"]
    resp = requests.post(
        location,
        allow_redirects=True,
        cookies=resp.cookies,
        headers={
            **default_headers,
            "referrer": initial_setup_url,
            "origin": "http://localhost:9000",
            **({"X-authentik-csrf": csrf} if csrf else {}),
        },
        data='{"email":"admin@example.com","password":"password","password_repeat":"password","component":"ak-stage-prompt"}',
    )
    log.debug("fetch::%s %s", location, resp)
    csrf = resp.cookies.get("authentik-csrf")
    # resp.cookies
    token_name = "admin-token"
    resp = requests.post(
        "http://localhost:9000/api/v3/core/tokens/",
        cookies=resp.cookies,
        headers={**default_headers, **({"X-authentik-csrf": csrf} if csrf else {})},
        data=f'{"identifier":"{token_name}","intent":"api","description":""}',
    )
    log.debug("fetch::%s", resp)
    assert resp.ok, resp.text
    resp = requests.get(
        f"http://localhost:9000/api/v3/core/tokens/{token_name}/view_key/",
        cookies=resp.cookies,
        headers={**default_headers, **({"X-authentik-csrf": csrf} if csrf else {})},
    )
    log.debug("fetch::%s", resp)
    assert resp.ok, resp.text
    key = resp.json()["key"]
    return key


def main():
    # start_docker_compose()
    # wait_for_authentik()
    key = set_initial_password()
    print(key)


if __name__ == "__main__":
    main()

# docker compose up -d # start the services

# # check if localhost:9000 is up
# printf waiting
# while ! curl -sf http://localhost:9000 > /dev/null; do
#   printf '.'
#   sleep 1
# done
# echo


# # python3 -m webbrowser http://localhost:9000/if/flow/initial-setup/
