#!/bin/bash

# Load environment variables
set -a
source .env
set +a

# Ensure Ollama server is running
ssh -p $SSH_PORT $REMOTE_USER@$REMOTE_HOST "
    if ! pgrep ollama > /dev/null; then
        ollama serve > /dev/null 2>&1 &
        sleep 5  # Wait for server to start
    fi
"

# Run the AutoGen team setup
python3 src/team_setup.py 