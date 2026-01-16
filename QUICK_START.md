# 🚀 Quick Start Guide - InsightForge

This guide will help you run both the Streamlit analytics app and the Next.js frontend.

## Prerequisites

- **Python 3.8+** with pip
- **Node.js 18+** and npm
- **Streamlit** installed

## Step-by-Step Instructions

### Step 1: Install Python Dependencies

```bash
cd /Users/oumyb/Desktop/ai-data-analytics
pip install -r requirements.txt
```

If you encounter SSL issues, try:
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

### Step 2: Install Node.js Dependencies

```bash
cd /Users/oumyb/Desktop/ai-data-analytics/frontend
npm install
```

### Step 3: Run Both Services

You need to run both services in separate terminals:

#### Terminal 1 - Start Streamlit App

```bash
cd /Users/oumyb/Desktop/ai-data-analytics
streamlit run app.py
```

You should see:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
```

#### Terminal 2 - Start Next.js Frontend

```bash
cd /Users/oumyb/Desktop/ai-data-analytics/frontend
npm run dev
```

You should see:
```
- ready started server on 0.0.0.0:3000
- Local:        http://localhost:3000
```

### Step 4: Access the Application

Open your browser and visit:

- **Frontend Website**: http://localhost:3000
  - Landing page with all marketing content
  - Click "Get Started" or "Launch App" to access analytics

- **Analytics App (Embedded)**: http://localhost:3000/app
  - Full analytics interface embedded in the website

- **Streamlit App (Direct)**: http://localhost:8501
  - Direct access to the Streamlit app

## 🎯 Quick Access

Once both services are running:

1. Go to **http://localhost:3000**
2. Click any **"Get Started"** button
3. You'll be taken to the analytics page where you can:
   - Upload CSV files
   - Ask AI-powered questions
   - Generate insights and visualizations

## 🛠️ Alternative: Use the Startup Script

### macOS/Linux:

```bash
cd /Users/oumyb/Desktop/ai-data-analytics
./start-services.sh
```

### Windows:

```bash
cd /Users/oumyb/Desktop/ai-data-analytics
start-services.bat
```

This will start both services automatically.

## 📋 What Each Service Does

### Streamlit App (`app.py`)
- **Port**: 8501
- **Purpose**: Analytics engine
- **Features**:
  - CSV file upload and analysis
  - AI-powered question answering (requires Claude API key)
  - Data visualizations
  - Automatic insights generation
  - Executive summary creation

### Next.js Frontend
- **Port**: 3000
- **Purpose**: Marketing website and UI
- **Pages**:
  - Landing page (`/`)
  - Features page (`/features`)
  - Studio page (`/studio`)
  - Pricing page (`/pricing`)
  - Dashboard page (`/dashboard`)
  - Analytics app (`/app`) - embeds Streamlit

## 🔧 Troubleshooting

### Port Already in Use

If port 8501 is taken:
```bash
streamlit run app.py --server.port 8502
```
Then update the URL in `frontend/app/app/page.tsx` to `http://localhost:8502`

If port 3000 is taken:
```bash
npm run dev -- -p 3001
```

### Streamlit Not Loading in iframe

- Make sure Streamlit is running on port 8501
- Check browser console for errors
- Try opening Streamlit directly at http://localhost:8501
- Use the "Open in New Tab" button as an alternative

### Missing Dependencies

**Python:**
```bash
pip install streamlit pandas plotly anthropic numpy
```

**Node.js:**
```bash
cd frontend
npm install
```

## 🎨 Features Available

Once running, you can:

1. **Upload Data**: Click "Upload New Dataset" and select a CSV file
2. **Ask Questions**: Type questions like "What is the average revenue by month?"
3. **View Insights**: Click "Generate Insights" for automatic analysis
4. **Create Summaries**: Generate executive summaries with AI
5. **Visualize**: Automatic chart generation based on your questions

## 📝 Notes

- The Streamlit app requires a **Claude API key** for AI features (enter in sidebar)
- Get your API key at: https://console.anthropic.com
- All analytics features work without the API key, but AI-powered questions won't work

## 🆘 Need Help?

- Check that both terminals show the services are running
- Verify ports 3000 and 8501 are accessible
- Make sure all dependencies are installed
- Check the browser console for any errors

---

**Enjoy using InsightForge! 🎉**
