#!/bin/bash

# Quick ngrok deployment script
# This will expose your local server to the internet instantly!

echo "========================================================================"
echo "🚀 Hope-iatry - Quick Internet Deployment with ngrok"
echo "========================================================================"
echo ""

# Check if ngrok is installed
if ! command -v ngrok &> /dev/null; then
    echo "❌ ngrok is not installed"
    echo ""
    echo "Install it with:"
    echo "  brew install ngrok"
    echo ""
    echo "OR download from: https://ngrok.com/download"
    echo ""
    exit 1
fi

echo "✅ ngrok is installed"
echo ""

# Check if server is running
if ! lsof -Pi :5001 -sTCP:LISTEN -t >/dev/null ; then
    echo "⚠️  Server is not running on port 5001"
    echo ""
    echo "Starting the server..."
    python backend.py &
    sleep 3
    echo "✅ Server started"
    echo ""
fi

echo "🌐 Creating public URL..."
echo ""
echo "⚠️  IMPORTANT: This will create a temporary public URL"
echo "   Share this URL with your team to test the app"
echo "   The URL will stop working when you close this terminal"
echo ""
echo "========================================================================"
echo ""

# Start ngrok
ngrok http 5001
