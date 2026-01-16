# InsightForge Project Structure

## 📁 Important Files Kept

### Core Application
- **`app.py`** - Main Streamlit analytics application (62KB)
- **`requirements.txt`** - Full Python dependencies
- **`requirements-deploy.txt`** - Minimal dependencies for deployment

### Frontend (Next.js)
- **`frontend/`** - Complete Next.js application
  - React components
  - Pages (Landing, Features, Studio, Pricing, Dashboard, Analytics)
  - Tailwind CSS styling
  - TypeScript configuration

### Documentation
- **`README.md`** - Main project documentation
- **`QUICK_START.md`** - Quick start guide
- **`DEPLOYMENT.md`** - Deployment instructions
- **`LOVABLE_INTEGRATION.md`** - Lovable integration guide
- **`ADD_LOVABLE_TO_GITHUB.md`** - GitHub setup guide
- **`CLEANUP_DUPLICATES.md`** - Cleanup documentation

### Scripts
- **`start-services.sh`** - Start both services (macOS/Linux)
- **`start-services.bat`** - Start both services (Windows)
- **`quick-github-setup.sh`** - GitHub setup helper

## 🗑️ Files Removed (Obsolete)

### Deleted:
- ❌ `requiremenets.txt` - Typo, empty file
- ❌ `app_chat.py` - Old version of app
- ❌ `app.html` - Obsolete HTML
- ❌ `index.html` - Obsolete HTML
- ❌ `clipbard-landing.html` - Obsolete HTML
- ❌ `insightforge-landing.html` - Obsolete HTML
- ❌ `styles.css` - Obsolete CSS
- ❌ `clipbard-styles.css` - Obsolete CSS
- ❌ `insightforge-styles.css` - Obsolete CSS
- ❌ `script.js` - Obsolete JavaScript
- ❌ `clipbard-script.js` - Obsolete JavaScript
- ❌ `insightforge-script.js` - Obsolete JavaScript
- ❌ `utils.py` - Empty file

**Reason:** These files were from old static HTML/CSS/JS implementations. The project now uses:
- Next.js frontend (`frontend/` directory)
- Streamlit backend (`app.py` with embedded CSS)

## 📊 Project Summary

**Total Important Files:** ~25 files
- 1 main Python app
- 1 Next.js frontend (multiple files)
- 2 requirements files
- 5 documentation files
- 3 helper scripts

**Project is now clean and organized!** ✨
