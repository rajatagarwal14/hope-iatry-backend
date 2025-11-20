#!/bin/bash

# Deploy to Render.com - Full Guide
# This helps you deploy to Render (FREE forever!)

echo "========================================================================"
echo "🚀 Hope-iatry - Deploy to Render.com (FREE)"
echo "========================================================================"
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo "📁 Initializing git repository..."
    git init
    echo "✅ Git initialized"
    echo ""
fi

# Create .gitignore if it doesn't exist
if [ ! -f .gitignore ]; then
    echo "📝 Creating .gitignore..."
    cat > .gitignore << EOF
.env
.env.*
!.env.example
__pycache__/
*.pyc
*.pyo
.venv/
venv/
.DS_Store
*.log
EOF
    echo "✅ .gitignore created"
    echo ""
fi

# Check if remote is set
if ! git remote | grep -q origin; then
    echo "⚠️  No git remote found"
    echo ""
    echo "Please create a GitHub repository and add it as remote:"
    echo ""
    echo "  1. Go to https://github.com/new"
    echo "  2. Create a new repository (e.g., 'hope-iatry-backend')"
    echo "  3. Run this command with your repo URL:"
    echo ""
    echo "     git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
    echo ""
    read -p "Press Enter after adding the remote, or Ctrl+C to exit..."
fi

# Add and commit files
echo "📦 Committing files..."
git add .
git commit -m "Prepare for Render deployment" || echo "No changes to commit"

# Push to GitHub
echo ""
echo "📤 Pushing to GitHub..."
git push -u origin main || git push -u origin master

echo ""
echo "========================================================================"
echo "✅ Code pushed to GitHub!"
echo "========================================================================"
echo ""
echo "Next steps:"
echo ""
echo "1. Go to: https://render.com"
echo "2. Sign up (free) with your GitHub account"
echo "3. Click 'New +' → 'Web Service'"
echo "4. Select your repository"
echo "5. Use these settings:"
echo ""
echo "   Name: hope-iatry-backend"
echo "   Environment: Python"
echo "   Build Command: pip install -r requirements.txt"
echo "   Start Command: gunicorn backend:app"
echo ""
echo "6. Add Environment Variable:"
echo "   Key: GROQ_API_KEY"
echo "   Value: YOUR_GROQ_API_KEY (from your .env file)"
echo ""
echo "7. Click 'Create Web Service'"
echo ""
echo "🎉 You'll get a URL like: https://hope-iatry-backend.onrender.com"
echo ""
echo "========================================================================"
