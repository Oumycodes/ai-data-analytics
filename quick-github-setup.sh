#!/bin/bash

echo "🚀 Quick GitHub Setup for Lovable Frontend"
echo "=========================================="
echo ""

# Check if we're in a git repo
if [ -d ".git" ]; then
    echo "✅ Git repository already initialized"
else
    echo "📦 Initializing git repository..."
    git init
fi

echo ""
echo "📝 Next steps:"
echo "1. Make sure all your Lovable files are in this directory"
echo "2. Run: git add ."
echo "3. Run: git commit -m 'Initial commit from Lovable'"
echo "4. Create a new repository on GitHub.com"
echo "5. Run: git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git"
echo "6. Run: git branch -M main"
echo "7. Run: git push -u origin main"
echo ""
echo "💡 Tip: Replace YOUR_USERNAME and REPO_NAME with your actual values"
