#!/bin/bash

# Groq API Key Setup Script
# This script helps you configure the Groq API key

echo "========================================================================"
echo "🌟 Hope-iatry Backend - Groq API Setup"
echo "========================================================================"
echo ""
echo "Groq provides FAST and FREE AI API access!"
echo ""
echo "📝 Steps to get your API key:"
echo "   1. Visit: https://console.groq.com/"
echo "   2. Sign up for a free account"
echo "   3. Go to API Keys section"
echo "   4. Click 'Create API Key'"
echo "   5. Copy the key"
echo ""
echo "========================================================================"
echo ""

# Check if .env file exists
if [ -f ".env" ]; then
    echo "✓ Found .env file"
    
    # Check if key is already set
    if grep -q "GROQ_API_KEY=gsk_" .env; then
        echo "✓ Groq API key appears to be already configured"
        echo ""
        read -p "Do you want to update it? (y/n): " update_key
        if [ "$update_key" != "y" ]; then
            echo "Setup cancelled."
            exit 0
        fi
    fi
else
    echo "Creating .env file..."
    cp .env.example .env
fi

echo ""
read -p "Enter your Groq API Key (starts with gsk_): " api_key

if [ -z "$api_key" ]; then
    echo "❌ No API key provided. Setup cancelled."
    exit 1
fi

# Update .env file
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    sed -i '' "s/GROQ_API_KEY=.*/GROQ_API_KEY=$api_key/" .env
else
    # Linux
    sed -i "s/GROQ_API_KEY=.*/GROQ_API_KEY=$api_key/" .env
fi

echo ""
echo "✅ Groq API key configured successfully!"
echo ""
echo "You can now run the server with:"
echo "   python backend.py"
echo "   or"
echo "   ./start.sh"
echo ""
echo "========================================================================"
