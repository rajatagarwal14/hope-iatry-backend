#!/bin/bash

echo "========================================"
echo "Hope-iatry AI Coaching Platform"
echo "========================================"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "ERROR: .env file not found!"
    echo ""
    echo "Please follow these steps:"
    echo "1. Copy .env.example to .env: cp .env.example .env"
    echo "2. Add your ANTHROPIC_API_KEY to .env"
    echo ""
    exit 1
fi

echo "Starting server..."
echo ""
echo "The app will be available at:"
echo "  - Local: http://localhost:5000"
echo "  - Network: http://YOUR_IP:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 backend.py
