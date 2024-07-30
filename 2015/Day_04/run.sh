#!/bin/bash
# Activate & run the code for this day

# Activate the environment
source ../../venv/bin/activate

# Invoke all the tests
pytest tests/

# Execute the main script
python3 main.py

# Stop the vritual environment
deactivate
