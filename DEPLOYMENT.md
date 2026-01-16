# Deployment Guide for InsightForge

This guide covers multiple deployment options for your Streamlit application.

## Option 1: Streamlit Cloud (Recommended - Easiest & Free)

Streamlit Cloud is the official hosting platform for Streamlit apps. It's free and very easy to use.

### Steps:

1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/ai-data-analytics.git
   git push -u origin main
   ```

2. **Sign up for Streamlit Cloud**
   - Go to https://share.streamlit.io/
   - Sign in with your GitHub account

3. **Deploy your app**
   - Click "New app"
   - Select your repository: `YOUR_USERNAME/ai-data-analytics`
   - Select branch: `main`
   - Main file path: `app.py`
   - Click "Deploy"

4. **Your app will be live at:**
   - `https://YOUR_APP_NAME.streamlit.app`

### Requirements:
- Your code must be in a GitHub repository
- `requirements.txt` must be in the root directory
- `app.py` should be the main file

---

## Option 2: Heroku

### Steps:

1. **Install Heroku CLI**
   - Download from: https://devcenter.heroku.com/articles/heroku-cli

2. **Create necessary files:**

   **`Procfile`** (create in root directory):
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

   **`.streamlit/config.toml`** (create directory and file):
   ```toml
   [server]
   port = $PORT
   enableCORS = false
   enableXsrfProtection = false
   ```

3. **Deploy:**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

---

## Option 3: Railway

Railway is a modern platform that's easy to use.

### Steps:

1. **Go to Railway**
   - Visit: https://railway.app/
   - Sign up with GitHub

2. **Create new project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Configure**
   - Railway will auto-detect it's a Python app
   - Add start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
   - Deploy!

---

## Option 4: Render

### Steps:

1. **Go to Render**
   - Visit: https://render.com/
   - Sign up with GitHub

2. **Create new Web Service**
   - Connect your GitHub repository
   - Build command: `pip install -r requirements.txt`
   - Start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

3. **Environment variables** (if needed):
   - Add any API keys or secrets in the Environment section

---

## Option 5: Docker + Any Cloud Provider

### Create Dockerfile:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Deploy to:
- **AWS ECS/Fargate**
- **Google Cloud Run**
- **Azure Container Instances**
- **DigitalOcean App Platform**

---

## Important Notes:

### Environment Variables
If your app uses API keys (like Claude API), set them as environment variables in your hosting platform:
- Streamlit Cloud: Settings → Secrets
- Heroku: `heroku config:set API_KEY=your_key`
- Railway/Render: Environment variables section

### Requirements.txt
Make sure your `requirements.txt` includes all dependencies:
```
streamlit
pandas
plotly
anthropic
numpy
scipy
scikit-learn
```

### File Size Limits
- Streamlit Cloud: 1GB repo size limit
- Heroku: 500MB slug size
- Consider using `.gitignore` to exclude large files

### Custom Domain
Most platforms allow custom domains:
- Streamlit Cloud: Settings → Custom domain
- Heroku: Settings → Domains
- Railway/Render: Custom domain settings

---

## Quick Start (Streamlit Cloud)

1. **Ensure requirements.txt exists:**
   ```bash
   pip freeze > requirements.txt
   ```

2. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push
   ```

3. **Deploy on Streamlit Cloud:**
   - Go to https://share.streamlit.io/
   - Click "New app"
   - Select your repo
   - Deploy!

Your app will be live in minutes! 🚀
