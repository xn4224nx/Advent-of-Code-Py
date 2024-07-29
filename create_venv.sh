#!/bin/bash
# Create the Python virtual environment that all days use

VENV_DIR="./venv"

# Remove old versions of the environment if it exists
if [ -f "$REQ_FILE" ]; then
    rm -r $VENV_DIR
fi

# Create it anew
python3 -m venv $VENV_DIR

# Activate the environment
source $VENV_DIR"/bin/activate"

# Install the required modules
pip install -r "./requirements.txt"

deactivate
