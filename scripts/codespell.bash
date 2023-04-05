#!/usr/bin/env bash

# This script is used to check the code for spelling errors using codespell.

# Exit immediately if a command exits with a non-zero status.
set -e

# Change to the root directory of the project.
cd "$(dirname "$0")/.."

# Check the code for spelling errors.
codespell --skip '*.git' -w src/*.py src/*.md src/*.txt src/*.java
