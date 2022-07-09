#!/bin/sh
# shellcheck disable=SC2046
pylint $(git ls-files '*.py')
