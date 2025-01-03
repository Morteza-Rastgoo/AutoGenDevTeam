#!/bin/bash

# Create clean .env.example
cat > .env.example << 'EOF'
REMOTE_HOST="your_remote_host"
REMOTE_USER="your_username"
SSH_PORT=22
OLLAMA_BASE_URL="http://your_remote_host:11434/v1"
EOF

# Remove sensitive files from git history
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env" \
  --prune-empty --tag-name-filter cat -- --all

# Force push changes
git push origin --force --all

# Clean up refs and garbage collect
git for-each-ref --format="delete %(refname)" refs/original | git update-ref --stdin
git reflog expire --expire=now --all
git gc --prune=now --aggressive 