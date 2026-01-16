# Integrating Streamlit App with Next.js Frontend

This guide explains how to run both the Next.js frontend and the Streamlit app (`app.py`) together so you can access the analytics functionality from the website.

## 🚀 Quick Start

### Option 1: Run Both Services Separately (Recommended)

1. **Start the Streamlit app** (in the project root):
```bash
cd /Users/oumyb/Desktop/ai-data-analytics
streamlit run app.py
```
The Streamlit app will run on `http://localhost:8501`

2. **Start the Next.js frontend** (in a new terminal):
```bash
cd /Users/oumyb/Desktop/ai-data-analytics/frontend
npm run dev
```
The Next.js app will run on `http://localhost:3000`

3. **Access the integrated app**:
   - Visit `http://localhost:3000/app` to see the Streamlit app embedded in the Next.js frontend
   - Or click "Launch App" in the navigation menu

### Option 2: Use a Script to Run Both

Create a script to run both services simultaneously:

**For macOS/Linux** (`start.sh`):
```bash
#!/bin/bash
# Start Streamlit in background
cd /Users/oumyb/Desktop/ai-data-analytics
streamlit run app.py &
STREAMLIT_PID=$!

# Start Next.js
cd /Users/oumyb/Desktop/ai-data-analytics/frontend
npm run dev &
NEXTJS_PID=$!

echo "Streamlit running on http://localhost:8501 (PID: $STREAMLIT_PID)"
echo "Next.js running on http://localhost:3000 (PID: $NEXTJS_PID)"
echo "Press Ctrl+C to stop both services"

# Wait for user interrupt
trap "kill $STREAMLIT_PID $NEXTJS_PID" EXIT
wait
```

**For Windows** (`start.bat`):
```batch
@echo off
start "Streamlit" cmd /k "cd /Users/oumyb/Desktop/ai-data-analytics && streamlit run app.py"
start "Next.js" cmd /k "cd /Users/oumyb/Desktop/ai-data-analytics/frontend && npm run dev"
```

## 📍 Access Points

### From Next.js Frontend:
- **Landing Page**: `http://localhost:3000/` - Click "Launch InsightForge" button
- **App Page**: `http://localhost:3000/app` - Embedded Streamlit app
- **Navigation**: Click "Launch App" in the navbar

### Direct Streamlit Access:
- **Streamlit App**: `http://localhost:8501` - Direct access to the analytics app

## 🔧 What the Streamlit App Does

The `app.py` Streamlit application provides:

1. **Analytics Page**:
   - Upload CSV files for analysis
   - View data overview (rows, columns, missing data)
   - Ask questions about your data using AI (Claude API)
   - Generate automatic insights
   - Create visualizations (line, bar, histogram, scatter charts)
   - Generate executive summaries

2. **Profile Page**:
   - View and edit user profile
   - Manage account settings
   - Delete account option

3. **Features**:
   - AI-powered natural language queries
   - Automatic pattern detection
   - Data visualization with Plotly
   - Statistical analysis
   - Export capabilities

## 🎨 Integration Details

The Next.js frontend includes:
- A dedicated `/app` route that embeds the Streamlit app in an iframe
- Navigation links to access the app from any page
- Instructions displayed if Streamlit isn't running
- Option to open the app in a new tab

## ⚙️ Configuration

### Change Streamlit Port

If you need to run Streamlit on a different port:

1. Update `app.py` or run with:
```bash
streamlit run app.py --server.port 8502
```

2. Update the URL in `frontend/app/app/page.tsx`:
```typescript
const [streamlitUrl, setStreamlitUrl] = useState('http://localhost:8502')
```

### Production Deployment

For production, you'll want to:
1. Deploy Streamlit app (Streamlit Cloud, Heroku, AWS, etc.)
2. Update the `streamlitUrl` in the Next.js app to point to your deployed Streamlit URL
3. Configure CORS if needed
4. Set up authentication/authorization

## 🐛 Troubleshooting

### Streamlit not loading in iframe:
- Check that Streamlit is running on the correct port
- Verify the URL in the browser console
- Some browsers block iframes - use the "Open in New Tab" option

### CORS Issues:
- Streamlit may need CORS configuration for iframe embedding
- Add to `.streamlit/config.toml`:
```toml
[server]
enableCORS = true
enableXsrfProtection = false
```

### Port Conflicts:
- If port 8501 is in use, change it: `streamlit run app.py --server.port 8502`
- Update the URL in the Next.js app accordingly

## 📝 Next Steps

1. **Add Authentication**: Protect the `/app` route with authentication
2. **Environment Variables**: Use environment variables for Streamlit URL
3. **Error Handling**: Add better error handling for connection issues
4. **Loading States**: Improve loading indicators
5. **Responsive Design**: Optimize iframe for mobile devices
