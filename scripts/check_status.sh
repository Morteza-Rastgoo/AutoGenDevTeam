#!/bin/bash

# Load environment variables
set -a
source .env
set +a

# Check Ollama server status
ssh -p $SSH_PORT $REMOTE_USER@$REMOTE_HOST "
    if pgrep ollama > /dev/null; then
        echo 'Ollama server is running'
        echo 'Available models:'
        ollama list
    else
        echo 'Ollama server is not running'
    fi
"

# Check project directory structure
ssh -p $SSH_PORT $REMOTE_USER@$REMOTE_HOST "
    echo 'Project structure:'
    tree ~/autogen_project
" 