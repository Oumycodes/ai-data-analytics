import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from anthropic import Anthropic
import numpy as np

# =========================
# STUDIO STYLE CSS - DARK THEME
# =========================
studio_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    /* Root Variables - Dark Theme */
    :root {
        --bg-dark: #111827;
        --bg-darker: #0F172A;
        --bg-card: #1F2937;
        --text-primary: #FFFFFF;
        --text-secondary: #9CA3AF;
        --accent-teal: #06B6D4;
        --accent-green: #10B981;
        --border-gray: #374151;
    }
    
    /* Main App Background */
    .main {
        background-color: var(--bg-dark);
        color: var(--text-primary);
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar Styling - Dark */
    [data-testid="stSidebar"] {
        background: var(--bg-darker) !important;
        border-right: 1px solid var(--border-gray);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: var(--bg-darker) !important;
    }
    
    /* Sidebar Logo */
    .sidebar-logo {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 1.5rem 0;
        margin-bottom: 2rem;
    }
    
    .sidebar-logo-icon {
        width: 24px;
        height: 24px;
        color: var(--accent-teal);
    }
    
    .sidebar-logo-text {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--text-primary);
    }
    
    /* Navigation Links */
    .nav-link {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.75rem 1rem;
        margin: 0.25rem 0;
        border-radius: 8px;
        color: var(--text-secondary);
        text-decoration: none;
        transition: all 0.3s;
        cursor: pointer;
    }
    
    .nav-link:hover {
        background: rgba(6, 182, 212, 0.1);
        color: var(--accent-teal);
    }
    
    .nav-link.active {
        background: rgba(6, 182, 212, 0.2);
        color: var(--accent-teal);
    }
    
    /* Credit Section */
    .credit-section {
        margin-top: 2rem;
        padding: 1rem;
        background: var(--bg-card);
        border-radius: 8px;
        border: 1px solid var(--border-gray);
    }
    
    /* Main Content Area */
    .main-content {
        background: var(--bg-dark);
        padding: 2rem;
    }
    
    /* Hero Section */
    .hero-studio {
        text-align: center;
        padding: 4rem 2rem;
        margin-bottom: 3rem;
        position: relative;
    }
    
    .hero-studio h1 {
        font-size: 3.5rem;
        font-weight: 800;
        color: var(--text-primary);
        margin-bottom: 1rem;
        background: none;
        -webkit-text-fill-color: var(--text-primary);
    }
    
    .hero-studio p {
        font-size: 1.25rem;
        color: var(--text-secondary);
        margin-bottom: 2rem;
    }
    
    /* Create Button */
    .btn-create {
        background: var(--accent-green);
        color: white;
        padding: 1rem 2rem;
        border-radius: 8px;
        border: none;
        font-weight: 600;
        font-size: 1rem;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        transition: all 0.3s;
    }
    
    .btn-create:hover {
        background: #059669;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(16, 185, 129, 0.4);
    }
    
    /* Section Headers */
    h2, h3 {
        color: var(--text-primary) !important;
    }
    
    /* Input Styling */
    .stTextInput > div > div > input {
        background: var(--bg-card);
        border: 1px solid var(--border-gray);
        color: var(--text-primary);
        border-radius: 8px;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--accent-teal);
    }
    
    /* File Uploader */
    [data-testid="stFileUploader"] {
        border: 2px dashed var(--border-gray);
        border-radius: 12px;
        background: var(--bg-card);
    }
    
    /* Buttons */
    .stButton > button {
        background: var(--accent-teal);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
    }
    
    .stButton > button:hover {
        background: var(--accent-teal-dark);
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        color: var(--accent-teal);
    }
    
    [data-testid="stMetricLabel"] {
        color: var(--text-secondary);
    }
    
    /* Dataframe */
    .dataframe {
        background: var(--bg-card);
        color: var(--text-primary);
    }
    
    /* Expander */
    [data-testid="stExpander"] {
        background: var(--bg-card);
        border: 1px solid var(--border-gray);
    }
    
    /* Success/Info/Warning */
    .stSuccess {
        background: rgba(16, 185, 129, 0.1);
        border-left: 4px solid var(--accent-green);
        color: var(--text-primary);
    }
    
    .stInfo {
        background: rgba(6, 182, 212, 0.1);
        border-left: 4px solid var(--accent-teal);
        color: var(--text-primary);
    }
    
    .stWarning {
        background: rgba(245, 158, 11, 0.1);
        border-left: 4px solid #F59E0B;
        color: var(--text-primary);
    }
    
    .stError {
        background: rgba(239, 68, 68, 0.1);
        border-left: 4px solid #EF4444;
        color: var(--text-primary);
    }
    
    /* User Profile */
    .user-profile {
        position: fixed;
        top: 1rem;
        right: 2rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        z-index: 100;
    }
    
    .user-avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: var(--accent-teal);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 600;
    }
    
    /* Chat Icon */
    .chat-icon {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        width: 56px;
        height: 56px;
        border-radius: 50%;
        background: var(--accent-teal);
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(6, 182, 212, 0.4);
        z-index: 100;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-darker);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--accent-teal);
        border-radius: 4px;
    }
</style>
"""

st.markdown(studio_css, unsafe_allow_html=True)

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="InsightForge Studio",
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    # Logo
    st.markdown("""
    <div class="sidebar-logo">
        <svg class="sidebar-logo-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M2 17L12 22L22 17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M2 12L12 17L22 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span class="sidebar-logo-text">InsightForge</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    page = st.radio(
        "Navigation",
        ["📊 Analytics", "👤 Profile"],
        label_visibility="collapsed",
        key="nav"
    )

    st.divider()

    # Credit Section
    st.markdown("""
    <div class="credit-section">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="color: var(--text-secondary);">Credit Quota</span>
            <button style="background: var(--accent-teal); color: white; border: none; padding: 0.25rem 0.75rem; border-radius: 4px; font-size: 0.75rem; cursor: pointer;">Buy Credits</button>
        </div>
        <div style="color: var(--text-primary); font-size: 1.25rem; font-weight: 600;">Remaining: <span style="color: var(--accent-teal);">12.00</span></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # API Key Configuration
    st.markdown("### ⚙️ Configuration")
    api_key = st.text_input(
        "Claude API Key",
        type="password",
        help="Get your key at console.anthropic.com",
        label_visibility="visible"
    )
    
    st.divider()
    
    # Footer Links
    st.markdown("""
    <div style="margin-top: auto; padding-top: 2rem;">
        <a href="#" style="color: var(--text-secondary); text-decoration: none; font-size: 0.875rem; display: block; margin-bottom: 0.5rem;">Privacy Policy</a>
        <a href="#" style="color: var(--text-secondary); text-decoration: none; font-size: 0.875rem;">Terms</a>
    </div>
    """, unsafe_allow_html=True)

# =========================
# USER PROFILE (Top Right)
# =========================
st.markdown("""
<div class="user-profile">
    <div class="user-avatar">O</div>
    <span style="color: var(--text-primary); font-weight: 500;">Oumaima</span>
</div>
""", unsafe_allow_html=True)

# =========================
# CHAT ICON (Bottom Right)
# =========================
st.markdown("""
<div class="chat-icon">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
</div>
""", unsafe_allow_html=True)

# =========================
# MAIN CONTENT
# =========================

if page == "📊 Analytics":
    # Hero Section
    st.markdown("""
    <div class="hero-studio">
        <h1>Data Intelligence Amplified</h1>
        <p>Transform raw data into actionable insights with unparalleled ease</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create New Analysis Button
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("➕ Upload New Dataset", type="primary", use_container_width=True):
            st.session_state.show_upload = True
    
    st.markdown("---")
    
    # Explore Analyses Section
    st.markdown("### 📊 Explore Analyses")
    
    # File Upload Section
    uploaded_file = st.file_uploader(
        "Choose a CSV file to analyze",
        type=["csv"],
        help="Upload your dataset to get started",
        label_visibility="visible"
    )

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df

        st.success("✅ Dataset loaded successfully!")
        
        # Data Overview
        st.markdown("### 📈 Data Overview")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Rows", f"{len(df):,}")
        with col2:
            st.metric("Total Columns", len(df.columns))
        with col3:
            st.metric("Numeric Columns", len(df.select_dtypes(include=[np.number]).columns))
        with col4:
            missing_pct = (df.isnull().sum().sum() / df.size) * 100
            st.metric("Missing Data", f"{missing_pct:.1f}%")

        # Data Preview
        with st.expander("🔍 Data Preview", expanded=True):
            st.dataframe(df.head(10), use_container_width=True)
        
        with st.expander("📈 Statistical Summary"):
            st.dataframe(df.describe(), use_container_width=True)

        # Ask Questions Section
        st.markdown("### 🤖 Ask Questions")
        
        question = st.text_input(
            "Ask a question about your data",
            placeholder="Example: What is the average revenue by month?",
            label_visibility="visible"
        )
        
        if question and api_key:
            with st.spinner("🤔 Analyzing..."):
                columns = df.columns.tolist()
                sample_data = df.head(3).to_string()
                
                # Determine if visualization is needed
                viz_prompt = f"""Given this data question: "{question}"

Should this be visualized? Respond with ONLY ONE WORD:
- "line" (for trends over time)
- "bar" (for comparisons)
- "histogram" (for distributions)
- "scatter" (for relationships)
- "pie" (for proportions)
- "none" (if just a number/text answer)
"""
                
                try:
                    client = Anthropic(api_key=api_key)
                    
                    viz_response = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=100,
                        messages=[{"role": "user", "content": viz_prompt}]
                    )
                    
                    chart_type = viz_response.content[0].text.strip().lower()
                    
                    # Generate pandas code
                    code_prompt = f"""You are a data analyst. 
Given a dataframe with these columns: {columns}

Sample data:
{sample_data}

User question: {question}

Generate valid Python pandas code that answers this question.
Use 'df' as the dataframe variable name.
Store the result in a variable called 'result'.
If creating a chart, also create variables for x and y axes.

Only output code. No markdown, no backticks, no explanation.

Example:
result = df.groupby('month')['revenue'].sum()
x_data = result.index
y_data = result.values
"""
                    
                    code_response = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=1024,
                        messages=[{"role": "user", "content": code_prompt}]
                    )
                    
                    code = code_response.content[0].text.strip()
                    
                    # Clean code
                    if '```' in code:
                        parts = code.split('```')
                        for part in parts:
                            clean_part = part.replace('python', '').strip()
                            if clean_part and not clean_part.startswith('#'):
                                code = clean_part
                                break
                    
                    # Display generated code
                    with st.expander("🔧 Generated Code"):
                        st.code(code, language="python")
                    
                    # Execute code
                    local_vars = {"df": df, "pd": pd, "np": np}
                    exec(code, {}, local_vars)
                    
                    # Display result
                    if 'result' in local_vars:
                        result = local_vars['result']
                        
                        col1, col2 = st.columns([1, 2])
                        
                        with col1:
                            st.success("✅ Answer")
                            if isinstance(result, (int, float)):
                                st.metric("Result", f"{result:,.2f}")
                            else:
                                st.write(result)
                        
                        # Create visualization
                        with col2:
                            if chart_type != "none" and 'x_data' in local_vars and 'y_data' in local_vars:
                                st.success("📊 Visualization")
                                
                                x_data = local_vars.get('x_data', [])
                                y_data = local_vars.get('y_data', [])
                                
                                if chart_type == "line":
                                    fig = px.line(x=x_data, y=y_data, markers=True)
                                    fig.update_layout(
                                        xaxis_title="X",
                                        yaxis_title="Y",
                                        plot_bgcolor='#1F2937',
                                        paper_bgcolor='#111827',
                                        font=dict(color='#FFFFFF', family="Inter, sans-serif")
                                    )
                                elif chart_type == "bar":
                                    fig = px.bar(x=x_data, y=y_data)
                                    fig.update_layout(
                                        xaxis_title="Category",
                                        yaxis_title="Value",
                                        plot_bgcolor='#1F2937',
                                        paper_bgcolor='#111827',
                                        font=dict(color='#FFFFFF', family="Inter, sans-serif")
                                    )
                                elif chart_type == "histogram":
                                    fig = px.histogram(df, x=df.columns[0])
                                    fig.update_layout(
                                        plot_bgcolor='#1F2937',
                                        paper_bgcolor='#111827',
                                        font=dict(color='#FFFFFF', family="Inter, sans-serif")
                                    )
                                elif chart_type == "scatter":
                                    fig = px.scatter(x=x_data, y=y_data)
                                    fig.update_layout(
                                        plot_bgcolor='#1F2937',
                                        paper_bgcolor='#111827',
                                        font=dict(color='#FFFFFF', family="Inter, sans-serif")
                                    )
                                else:
                                    fig = px.bar(x=x_data, y=y_data)
                                    fig.update_layout(
                                        plot_bgcolor='#1F2937',
                                        paper_bgcolor='#111827',
                                        font=dict(color='#FFFFFF', family="Inter, sans-serif")
                                    )
                                
                                fig.update_layout(height=400)
                                st.plotly_chart(fig, use_container_width=True)
                
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        
        elif question and not api_key:
            st.warning("⚠️ Please enter your Claude API key in the sidebar.")
        
        # Auto Insights Section
        st.markdown("### 🔍 Automatic Insights")
        
        if st.button("🔍 Generate Insights", type="primary"):
            with st.spinner("Analyzing data patterns..."):
                insights = []
                
                numeric_cols = df.select_dtypes(include=[np.number]).columns
                
                # Outlier Detection
                for col in numeric_cols[:3]:
                    Q1 = df[col].quantile(0.25)
                    Q3 = df[col].quantile(0.75)
                    IQR = Q3 - Q1
                    outliers = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)]
                    
                    if len(outliers) > 0:
                        insights.append(f"⚠️ **Outlier Detection**: Found {len(outliers)} outliers in '{col}'")
                
                # Range Analysis
                for col in numeric_cols[:2]:
                    max_val = df[col].max()
                    min_val = df[col].min()
                    insights.append(f"📊 **Range Analysis**: '{col}' ranges from {min_val:,.2f} to {max_val:,.2f}")
                
                # Trend Detection
                if len(df) > 3 and len(numeric_cols) > 0:
                    col = numeric_cols[0]
                    values = df[col].values
                    if len(values) > 1:
                        trend = "upward" if values[-1] > values[0] else "downward"
                        change = ((values[-1] - values[0]) / values[0] * 100) if values[0] != 0 else 0
                        insights.append(f"📈 **Trend Detection**: '{col}' shows {trend} trend ({change:+.1f}% change)")
                
                for insight in insights:
                    st.markdown(insight)
        
        # Executive Summary
        st.markdown("### 📝 Executive Summary")
        
        if st.button("📝 Generate Executive Summary", type="primary"):
            if api_key:
                with st.spinner("Creating summary..."):
                    try:
                        summary_prompt = f"""You are a senior data analyst presenting to executives.

Data overview:
- {len(df)} rows, {len(df.columns)} columns
- Columns: {', '.join(df.columns.tolist())}
- Key statistics: {df.describe().to_string()}

Generate a concise executive summary with:
1. Key findings (3-4 bullet points)
2. Notable patterns or trends
3. Actionable recommendations

Use clear, business-friendly language. Be specific with numbers."""

                        client = Anthropic(api_key=api_key)
                        summary_response = client.messages.create(
                            model="claude-sonnet-4-20250514",
                            max_tokens=2048,
                            messages=[{"role": "user", "content": summary_prompt}]
                        )
                        
                        summary = summary_response.content[0].text
                        
                        st.markdown("### 📋 Executive Summary")
                        st.markdown(summary)
                        
                    except Exception as e:
                        st.error(f"Error generating summary: {str(e)}")
            else:
                st.warning("Please enter your API key in the sidebar.")
    
    else:
        st.info("👆 Upload a CSV file to get started with your analysis")

elif page == "👤 Profile":
    st.markdown("### 👤 Profile Settings")
    st.markdown("Profile management coming soon...")
