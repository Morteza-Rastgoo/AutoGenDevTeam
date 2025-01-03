#!/bin/bash

# Make scripts executable
chmod +x scripts/*.sh

# Initialize repository and push to GitHub
./scripts/init_repo.sh

# Set up remote environment
./scripts/setup_remote.sh

echo "Project setup complete! You can now run ./scripts/run_project.sh to start the development process." 