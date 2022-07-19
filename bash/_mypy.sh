#!/bin/sh
# shellcheck disable=SC2046
mypy $(git ls-files '*.py') --strict
