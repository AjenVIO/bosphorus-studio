#!/usr/bin/env bash
# Run one workflow step with bash -eo pipefail and keep a copy of its output for failure reports.
exec > >(tee -a "${RUNNER_TEMP:-/tmp}/steps.log") 2>&1
set -eo pipefail
. "$1"
