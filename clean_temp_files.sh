#!/bin/bash
# Clean all temporary Python files
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$|\.pytest_cache$)" | xargs rm -rf
