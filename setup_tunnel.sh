#!/bin/bash

# Set up SSH tunnel to remote Ollama server
ssh -N -L 11434:localhost:11434 mrastgo@10.251.165.183 -p 22 