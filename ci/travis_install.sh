#!/bin/bash

set -e

# Package dependencies
pip install bitstring
# Test dependencies
pip install pytest

# Print versions
python --version

python setup.py build_ext --inplace
