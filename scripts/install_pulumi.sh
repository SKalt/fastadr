#!/bin/sh
set -eu 
mkdir -p ./bin
./scripts/download_pulumi.sh --install-root . --no-edit-path
