#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

VENV_NAME="private"
VENV_DIR="$SCRIPT_DIR/$VENV_NAME"

if [ ! -d "$VENV_DIR" ]; then
	python -m venv "$VENV_DIR"
fi

# Activate the virtual environment so pip targets it
source "$VENV_DIR/bin/activate"

pip install --upgrade pip
pip install --upgrade streamlit scikit-learn

pip freeze > requirements.txt

streamlit run app.py
