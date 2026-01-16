# InsightForge - AI-Powered Data Analytics Platform

A comprehensive data science platform that combines AI-powered natural language queries with advanced statistical analysis, machine learning predictions, and interactive visualizations. Built with Streamlit for the analytics engine and a modern Next.js frontend designed with Lovable for an intuitive user experience.

## 🌐 Live Demo

**Access the deployed website:** [https://insforge.lovable.app/](https://insforge.lovable.app/)

Try it out! Upload your data, ask questions, and get AI-powered insights instantly.

## 🎯 What This Project Does

InsightForge is an intelligent data analytics platform that transforms raw data into actionable insights through:

### Core Data Science Capabilities

- **🤖 AI-Powered Natural Language Queries**
  - Ask questions about your data in plain English
  - Get instant answers with automatically generated visualizations
  - Powered by Claude AI for intelligent code generation and analysis

- **📊 Advanced Statistical Analysis**
  - Correlation analysis and heatmaps
  - Hypothesis testing (normality tests, Pearson correlation)
  - Distribution analysis with confidence intervals
  - Statistical significance testing

- **🔮 Machine Learning Predictions**
  - Time series forecasting with multiple models (Linear Regression, Random Forest)
  - Feature prediction and importance analysis
  - Model performance metrics (MAE, R² score)
  - Anomaly detection using Z-score methods

- **📈 Interactive Visualizations**
  - Auto-generated charts based on your questions
  - Plotly-powered interactive graphs
  - Distribution histograms with normal curve overlays
  - Correlation heatmaps and trend analysis

- **🔍 Advanced Insights**
  - Outlier detection
  - Trend analysis and pattern recognition
  - Value concentration analysis
  - Executive summary generation

## 🏗️ Architecture

### Backend: Streamlit Analytics Engine
- **`app.py`** - Main Streamlit application with embedded AI-powered analytics
- ChatGPT-like chat interface for data interaction
- Real-time code generation and execution
- Advanced statistical and ML libraries (scipy, scikit-learn, plotly)

### Frontend: Modern Web Interface
- **`frontend/`** - Next.js application with Tailwind CSS
- Professional SaaS-style layout and navigation
- Responsive design for all devices
- Seamless integration with Streamlit backend via iframe

**Note:** The frontend was initially built manually, then enhanced using [Lovable](https://lovable.dev/) to create a polished, professional layout with improved UX/UI design patterns.

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- Claude API key (for AI features) - Get one at [console.anthropic.com](https://console.anthropic.com)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-data-analytics.git
   cd ai-data-analytics
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install frontend dependencies**
   ```bash
   cd frontend
   npm install
   cd ..
   ```

### Running the Application

#### Option 1: Run Both Services (Recommended)
```bash
# macOS/Linux
./start-services.sh

# Windows
start-services.bat
```

#### Option 2: Run Separately

**Backend (Streamlit):**
```bash
streamlit run app.py
```
Access at: http://localhost:8501

**Frontend (Next.js):**
```bash
cd frontend
npm run dev
```
Access at: http://localhost:3000

## 📊 Features in Detail

### 1. Data Upload & Quality Check
- Upload CSV files (up to 100MB)
- Automatic data quality reports
- Missing data analysis
- Column type detection

### 2. Natural Language Queries
Ask questions like:
- "What is the average revenue by month?"
- "Show me the correlation between sales and marketing spend"
- "Predict next quarter's revenue"
- "Are there any outliers in the customer data?"

### 3. Statistical Analysis
- **Correlation Analysis**: Identify relationships between variables
- **Hypothesis Testing**: Test statistical significance
- **Distribution Analysis**: Understand data distributions with confidence intervals
- **Normality Tests**: Check if data follows normal distribution

### 4. Machine Learning
- **Time Series Forecasting**: Predict future values using historical data
- **Feature Prediction**: Predict target variables using multiple features
- **Model Comparison**: Compare Linear Regression vs Random Forest
- **Feature Importance**: Understand which features matter most

### 5. Advanced Insights
- **Outlier Detection**: Find anomalies using Z-score method
- **Trend Analysis**: Identify significant upward/downward trends
- **Value Concentration**: Analyze data concentration patterns
- **Executive Summaries**: Generate comprehensive business reports

## 🛠️ Technology Stack

### Data Science & Analytics
- **Streamlit** - Interactive web app framework
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **SciPy** - Statistical functions
- **Scikit-learn** - Machine learning models
- **Plotly** - Interactive visualizations
- **Anthropic Claude API** - AI-powered code generation

### Frontend
- **Next.js 14** - React framework
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Lucide React** - Icon library

### Design & UX
- Frontend layout enhanced with [Lovable](https://lovable.dev/) for professional SaaS design patterns

## 📁 Project Structure

```
ai-data-analytics/
├── app.py                      # Main Streamlit analytics application
├── requirements.txt            # Python dependencies
├── requirements-deploy.txt    # Minimal dependencies for deployment
├── frontend/                  # Next.js frontend application
│   ├── app/                   # Next.js app directory
│   │   ├── page.tsx           # Landing page
│   │   ├── app/               # Analytics page (embeds Streamlit)
│   │   ├── features/          # Features page
│   │   ├── pricing/           # Pricing page
│   │   └── studio/            # Studio/workspace page
│   └── components/            # React components
│       ├── Navbar.tsx
│       └── Footer.tsx
├── start-services.sh          # Start both services (macOS/Linux)
├── start-services.bat         # Start both services (Windows)
└── README.md                  # This file
```

## 🔧 Configuration

### API Key Setup
1. Get your Claude API key from [console.anthropic.com](https://console.anthropic.com)
2. Enter it in the sidebar when running the Streamlit app
3. The API key is stored in session state (not saved to disk)

### Environment Variables (Frontend)
Create `frontend/.env.local`:
```
NEXT_PUBLIC_STREAMLIT_URL=http://localhost:8501
```

For production, set this to your deployed Streamlit app URL.

## 📈 Example Use Cases

- **Business Analytics**: Analyze sales data, revenue trends, customer behavior
- **Financial Analysis**: Forecast revenue, detect anomalies, analyze correlations
- **Research Data**: Statistical testing, distribution analysis, hypothesis validation
- **Marketing Analytics**: Campaign performance, conversion analysis, trend identification

## 🚀 Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed deployment instructions.

### Quick Deploy Options:
- **Streamlit Cloud** (Backend) - Free, official Streamlit hosting
- **Vercel/Netlify** (Frontend) - Recommended for Next.js apps
- **Railway/Render** - Full-stack deployment options

## 📚 Documentation

- [QUICK_START.md](./QUICK_START.md) - Detailed setup and running instructions
- [DEPLOYMENT.md](./DEPLOYMENT.md) - Deployment guide for various platforms
- [PROJECT_STRUCTURE.md](./PROJECT_STRUCTURE.md) - Project organization

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the analytics engine
- Frontend enhanced with [Lovable](https://lovable.dev/) for professional design
- Powered by [Anthropic Claude](https://www.anthropic.com/) for AI capabilities
- Visualization powered by [Plotly](https://plotly.com/)

---

**Built with ❤️ for data scientists and analysts who want to turn data into insights faster.**
