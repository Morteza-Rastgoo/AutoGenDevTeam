#!/bin/bash

# Load environment variables
set -a
source .env
set +a

# SSH connection details
REMOTE_HOST="10.251.165.183"
REMOTE_USER="mrastgo"
SSH_PORT=22

# Create project directory structure on remote
ssh -p $SSH_PORT $REMOTE_USER@$REMOTE_HOST "mkdir -p ~/autogen_project/{src,scripts,tests,config}"

# Copy necessary files to remote
scp -P $SSH_PORT -r ./* $REMOTE_USER@$REMOTE_HOST:~/autogen_project/

# Install Ollama on remote if not already installed
ssh -p $SSH_PORT $REMOTE_USER@$REMOTE_HOST "
    if ! command -v ollama &> /dev/null; then
        curl -fsSL https://ollama.ai/install.sh | sh
    fi
"

# Pull required Ollama models
ssh -p $SSH_PORT $REMOTE_USER@$REMOTE_HOST "
    ollama pull codellama
    ollama pull llama2
"

# Start Ollama server
ssh -p $SSH_PORT $REMOTE_USER@$REMOTE_HOST "
    ollama serve > /dev/null 2>&1 &
" 