#!/bin/bash

# Initialize git repository
git init

# Create README
cat > README.md << 'EOF'
# AutoGen Development Team

A multi-agent development system using AutoGen and Ollama for collaborative software development.

## Agents
- Product Owner: Defines requirements and project scope
- Architect: Designs system architecture
- Programmer: Implements features
- DevOps: Handles deployment and infrastructure
- QA Engineer: Ensures quality and testing

## Setup
1. Clone the repository
2. Copy `.env.example` to `.env` and update with your settings
3. Run `./scripts/setup_remote.sh`
4. Run `./scripts/run_project.sh`

## Requirements
- Python 3.8+
- Ollama installed on remote machine
- SSH access to remote machine

## Structure 