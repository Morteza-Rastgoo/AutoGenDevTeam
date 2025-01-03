#!/bin/bash

# Load environment variables
set -a
source .env
set +a

# Environment variables
REMOTE_HOST="10.251.165.183"
REMOTE_USER="mrastgo"
SSH_PORT=22

# Ensure Ollama server is running
ssh -p $SSH_PORT $REMOTE_USER@$REMOTE_HOST "
    if ! pgrep ollama > /dev/null; then
        ollama serve > /dev/null 2>&1 &
        sleep 5  # Wait for server to start
    fi
"

# Run the AutoGen team setup
python3 team_setup.py 