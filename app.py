import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from anthropic import Anthropic
import numpy as np
from scipy import stats
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# =========================
# BLUE & WHITE THEME CSS
# =========================
studio_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    /* Root Variables - Blue & White Theme */
    :root {
        --bg-main: #FFFFFF;
        --bg-sidebar: #F8F9FA;
        --bg-card: #FFFFFF;
        --bg-card-alt: #F5F7FA;
        --text-primary: #1E293B;
        --text-secondary: #475569;
        --text-muted: #64748B;
        --accent-blue: #2563EB;
        --accent-blue-light: #3B82F6;
        --accent-blue-dark: #1D4ED8;
        --accent-blue-bg: #EFF6FF;
        --accent-red: #DC2626;
        --accent-red-alt: #EF4444;
        --border-gray: #E2E8F0;
        --border-light: #CBD5E1;
    }
    
    /* Main App Background */
    .main {
        background-color: var(--bg-main) !important;
        color: var(--text-primary);
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar Styling - Blue & White */
    [data-testid="stSidebar"] {
        background: var(--bg-sidebar) !important;
        border-right: 1px solid var(--border-gray) !important;
        min-width: 280px !important;
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
    }
    
    [data-testid="stSidebar"][aria-expanded="false"] {
        transform: translateX(-100%) !important;
        visibility: visible !important;
        display: block !important;
    }
    
    [data-testid="stSidebar"][aria-expanded="true"] {
        transform: translateX(0) !important;
        visibility: visible !important;
        display: block !important;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: var(--bg-sidebar) !important;
        padding: 0.75rem 1rem 1rem 1rem;
    }
    
    /* Make sidebar toggle always visible */
    [data-testid="stHeader"] {
        background: white !important;
        border-bottom: 1px solid var(--border-gray) !important;
        visibility: visible !important;
        display: block !important;
        z-index: 999 !important;
    }
    
    /* Sidebar toggle button - make it clickable and visible */
    [data-testid="stHeader"] button,
    button[data-testid="baseButton-header"],
    button[kind="header"] {
        background: var(--accent-blue) !important;
        color: white !important;
        border-radius: 6px !important;
        padding: 0.5rem !important;
        margin: 0.5rem !important;
        box-shadow: 0 2px 4px rgba(37, 99, 235, 0.3) !important;
        visibility: visible !important;
        display: inline-block !important;
        opacity: 1 !important;
        cursor: pointer !important;
        pointer-events: auto !important;
        z-index: 1000 !important;
        position: relative !important;
    }
    
    [data-testid="stHeader"] button:hover,
    button[data-testid="baseButton-header"]:hover,
    button[kind="header"]:hover {
        background: var(--accent-blue-dark) !important;
        cursor: pointer !important;
    }
    
    /* Ensure no overlay blocks the button */
    [data-testid="stHeader"] * {
        pointer-events: auto !important;
    }
    
    /* Sidebar Logo - Clipbard Style */
    .sidebar-logo {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0 0 0.5rem 0;
        margin-bottom: 0.5rem;
        margin-top: 0;
    }
    
    .sidebar-logo-icon {
        width: 28px;
        height: 28px;
        color: var(--accent-blue);
    }
    
    .sidebar-logo-text {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--text-primary);
        letter-spacing: -0.5px;
    }
    
    /* Navigation Links - Blue & White Active State */
    .stRadio > div {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }
    
    .stRadio > div > label {
        padding: 0.75rem 1rem;
        margin: 0.25rem 0;
        border-radius: 8px;
        background: transparent;
        color: var(--text-muted);
        transition: all 0.3s ease;
        cursor: pointer !important;
        position: relative;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        pointer-events: auto !important;
        user-select: none;
    }
    
    .stRadio > div > label:hover {
        background: var(--accent-blue-bg);
        color: var(--accent-blue);
    }
    
    /* Ensure radio inputs are visible and clickable */
    .stRadio input[type="radio"] {
        cursor: pointer !important;
        pointer-events: auto !important;
        margin-right: 0.5rem;
    }
    
    /* Credit Section - Blue & White */
    .credit-section {
        margin-top: auto;
        padding: 1.25rem;
        background: var(--bg-card);
        border-radius: 10px;
        border: 1px solid var(--border-gray);
    }
    
    .credit-section-title {
        color: var(--text-secondary);
        font-size: 0.875rem;
        margin-bottom: 0.5rem;
        font-weight: 500;
    }
    
    .credit-section-value {
        color: var(--text-primary);
        font-size: 1.25rem;
        font-weight: 600;
    }
    
    .credit-section-value span {
        color: var(--accent-blue);
    }
    
    .btn-buy-credits {
        background: transparent;
        border: 1px solid var(--accent-blue);
        color: var(--accent-blue);
        padding: 0.5rem 1rem;
        border-radius: 6px;
        font-size: 0.875rem;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .btn-buy-credits:hover {
        background: var(--accent-blue-bg);
    }
    
    /* Main Content Area */
    .main-content {
        background: var(--bg-main);
        padding: 2rem 3rem;
        min-height: 100vh;
    }
    
    /* Hero Section - Clipbard Style */
    .hero-studio {
        text-align: left;
        padding: 3rem 0;
        margin-bottom: 3rem;
        position: relative;
    }
    
    .hero-studio h1 {
        font-size: 3.5rem;
        font-weight: 800;
        color: var(--text-primary);
        margin-bottom: 1rem;
        line-height: 1.1;
        letter-spacing: -1px;
    }
    
    .hero-studio h1 .accent {
        color: var(--accent-blue);
    }
    
    .hero-studio p {
        font-size: 1.25rem;
        color: var(--text-secondary);
        margin-bottom: 2rem;
        line-height: 1.7;
        max-width: 600px;
        font-weight: 400;
    }
    
    /* Card/Panel Styles - Clipbard Style */
    .content-card {
        background: var(--bg-card);
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        border: 1px solid var(--border-gray);
    }
    
    .content-card h2, .content-card h3 {
        color: var(--text-primary) !important;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    /* Section Headers - Clear Typography */
    h1 {
        color: var(--text-primary) !important;
        font-weight: 800;
        line-height: 1.2;
    }
    
    h2, h3 {
        color: var(--text-primary) !important;
        font-weight: 700;
        line-height: 1.3;
    }
    
    p, li, span, div {
        color: var(--text-primary);
        line-height: 1.7;
    }
    
    /* Input Styling - Blue & White */
    .stTextInput > div > div > input {
        background: var(--bg-main);
        border: 1px solid var(--border-gray);
        color: var(--text-primary);
        border-radius: 8px;
        padding: 0.75rem 1rem;
        font-size: 0.95rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--accent-blue);
        outline: none;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
    }
    
    .stTextInput > label {
        color: var(--text-primary) !important;
        font-weight: 600;
        margin-bottom: 0.5rem;
        font-size: 0.95rem;
    }
    
    /* File Uploader - Clipbard Style */
    [data-testid="stFileUploader"] {
        border: 2px dashed var(--border-gray);
        border-radius: 12px;
        background: var(--bg-card);
        padding: 2rem;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: var(--accent-teal);
        background: rgba(30, 193, 181, 0.05);
    }
    
    /* Buttons - Blue & White */
    .stButton > button {
        background: var(--accent-blue);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.95rem;
        padding: 0.75rem 1.5rem;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background: var(--accent-blue-dark);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }
    
    .stButton > button[kind="secondary"] {
        background: transparent;
        border: 1px solid var(--accent-blue);
        color: var(--accent-blue);
    }
    
    .stButton > button[kind="secondary"]:hover {
        background: var(--accent-blue-bg);
    }
    
    /* Metrics - Blue & White */
    [data-testid="stMetricValue"] {
        color: var(--accent-blue);
        font-size: 2rem;
        font-weight: 700;
    }
    
    [data-testid="stMetricLabel"] {
        color: var(--text-secondary);
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    /* Dataframe - Clipbard Style */
    .dataframe {
        background: var(--bg-card);
        color: var(--text-primary);
        border-radius: 8px;
        overflow: hidden;
    }
    
    /* Expander - Clipbard Style */
    [data-testid="stExpander"] {
        background: var(--bg-card);
        border: 1px solid var(--border-gray);
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    
    [data-testid="stExpander"] > summary {
        color: var(--text-primary) !important;
        font-weight: 600;
        padding: 1rem;
    }
    
    /* Success/Info/Warning - Blue & White */
    .stSuccess {
        background: #F0FDF4;
        border-left: 4px solid #10B981;
        color: var(--text-primary);
        border-radius: 6px;
        padding: 1rem;
        border: 1px solid #D1FAE5;
    }
    
    .stInfo {
        background: var(--accent-blue-bg);
        border-left: 4px solid var(--accent-blue);
        color: var(--text-primary);
        border-radius: 6px;
        padding: 1rem;
        border: 1px solid #DBEAFE;
    }
    
    .stWarning {
        background: #FFFBEB;
        border-left: 4px solid #F59E0B;
        color: var(--text-primary);
        border-radius: 6px;
        padding: 1rem;
        border: 1px solid #FEF3C7;
    }
    
    .stError {
        background: #FEF2F2;
        border-left: 4px solid var(--accent-red);
        color: var(--text-primary);
        border-radius: 6px;
        padding: 1rem;
        border: 1px solid #FEE2E2;
    }
    
    /* User Profile - Clipbard Style */
    .user-profile {
        position: fixed;
        top: 1.5rem;
        right: 2rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        z-index: 100;
        background: var(--bg-sidebar);
        padding: 0.5rem 1rem;
        border-radius: 50px;
        border: 1px solid var(--border-gray);
    }
    
    .user-avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: var(--accent-blue);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 600;
        font-size: 1rem;
    }
    
    .user-name {
        color: var(--text-primary);
        font-weight: 500;
        font-size: 0.95rem;
    }
    
    /* Chat Icon - Blue & White */
    .chat-icon {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        width: 56px;
        height: 56px;
        border-radius: 50%;
        background: var(--accent-blue);
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 4px 16px rgba(37, 99, 235, 0.4);
        z-index: 100;
        transition: all 0.3s;
    }
    
    .chat-icon:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5);
    }
    
    /* Profile Page Styles - Blue & White */
    .profile-card {
        background: var(--bg-card);
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        border: 1px solid var(--border-gray);
    }
    
    .profile-card-danger {
        background: var(--bg-card);
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        border: 2px solid var(--accent-red);
    }
    
    .profile-card h2 {
        color: var(--text-primary) !important;
        font-weight: 700;
        margin-bottom: 1.5rem;
    }
    
    .profile-card-danger h2 {
        color: var(--accent-red) !important;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .profile-input-label {
        color: var(--text-primary);
        font-size: 0.875rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        display: block;
    }
    
    .profile-input-field {
        background: var(--bg-main);
        border: 1px solid var(--border-gray);
        color: var(--text-primary);
        border-radius: 8px;
        padding: 0.75rem 1rem;
        width: 100%;
        font-size: 0.95rem;
    }
    
    
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* Keep header visible for sidebar toggle */
    header {visibility: visible !important;}
    
    /* Scrollbar - Blue & White */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-sidebar);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--accent-blue);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--accent-blue-dark);
    }
    
    /* Typography - Clear Writing */
    body, .main {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        line-height: 1.6;
        color: var(--text-primary);
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary);
        font-weight: 700;
        line-height: 1.3;
    }
    
    p, li, span {
        color: var(--text-primary);
        line-height: 1.7;
    }
    
    /* Dataframe Styling */
    .dataframe {
        background: var(--bg-main);
        color: var(--text-primary);
        border: 1px solid var(--border-gray);
    }
    
    /* Expander Styling */
    [data-testid="stExpander"] {
        background: var(--bg-main);
        border: 1px solid var(--border-gray);
        border-radius: 8px;
    }
    
    [data-testid="stExpander"] > summary {
        color: var(--text-primary) !important;
        font-weight: 600;
        padding: 1rem;
    }
    
    /* Text Area Styling */
    .stTextArea > div > div > textarea {
        background: var(--bg-main);
        border: 1px solid var(--border-gray);
        color: var(--text-primary);
        border-radius: 8px;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: var(--accent-blue);
        outline: none;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
    }
    
    /* File Uploader */
    [data-testid="stFileUploader"] {
        border: 2px dashed var(--border-gray);
        border-radius: 12px;
        background: var(--bg-sidebar);
        padding: 1.5rem;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: var(--accent-blue);
        background: var(--accent-blue-bg);
    }
    
    /* Selectbox */
    .stSelectbox > div > div > select {
        background: var(--bg-main);
        border: 1px solid var(--border-gray);
        color: var(--text-primary);
        border-radius: 8px;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: var(--bg-sidebar);
        border-bottom: 2px solid var(--border-gray);
    }
    
    .stTabs [data-baseweb="tab"] {
        color: var(--text-secondary);
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        color: var(--accent-blue);
        font-weight: 600;
    }
    
    /* Divider Styling */
    hr {
        border-color: var(--border-gray);
        margin: 1.5rem 0;
    }
    
    /* Radio Button Custom Styling - Blue & White Theme */
    .stRadio [role="radiogroup"] {
        gap: 0.5rem;
        flex-direction: column;
    }
    
    .stRadio label {
        padding: 0.75rem 1rem !important;
        margin: 0.25rem 0 !important;
        border-radius: 8px !important;
        background: transparent !important;
        color: var(--text-muted) !important;
        transition: all 0.3s !important;
        cursor: pointer !important;
        display: flex !important;
        align-items: center !important;
        gap: 0.75rem !important;
        pointer-events: auto !important;
        position: relative !important;
        width: 100% !important;
    }
    
    .stRadio label:hover {
        background: var(--accent-blue-bg) !important;
        color: var(--accent-blue) !important;
    }
    
    /* Ensure radio inputs are clickable and visible */
    .stRadio input[type="radio"] {
        cursor: pointer !important;
        pointer-events: auto !important;
        opacity: 1 !important;
        margin: 0 !important;
        margin-right: 0.5rem !important;
    }
    
    /* Navigation buttons styling */
    div[data-testid="column"] button {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-gray) !important;
        color: var(--text-primary) !important;
        font-weight: 500 !important;
        transition: all 0.3s !important;
    }
    
    div[data-testid="column"] button:hover {
        background: var(--accent-blue-bg) !important;
        border-color: var(--accent-blue) !important;
        color: var(--accent-blue) !important;
    }
    
    /* Selectbox Styling */
    .stSelectbox > div > div > select {
        background: var(--bg-card-alt);
        border: 1px solid var(--border-gray);
        color: var(--text-primary);
        border-radius: 8px;
    }
    
    /* Additional spacing improvements */
    .element-container {
        margin-bottom: 0.75rem;
    }
    
    /* Reduce spacing in sidebar */
    [data-testid="stSidebar"] h3 {
        margin-top: 0.75rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    [data-testid="stSidebar"] .element-container {
        margin-bottom: 0.5rem !important;
    }
    
    [data-testid="stSidebar"] code {
        margin: 0.25rem 0 !important;
    }
    
    /* Section spacing */
    section[data-testid="stSidebar"] {
        padding: 0 !important;
        position: relative !important;
    }
    
    /* Sidebar visibility helper */
    .sidebar-help {
        position: fixed;
        top: 1rem;
        left: 1rem;
        background: var(--accent-blue);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        font-size: 0.875rem;
        z-index: 999;
        display: none;
    }
    
    [data-testid="stSidebar"][aria-expanded="false"] ~ .sidebar-help {
        display: block;
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
    initial_sidebar_state="expanded",
    menu_items=None
)

# =========================
# SIDEBAR - BLUE & WHITE THEME
# =========================

# Note: Sidebar can be toggled using the ☰ button in the top left corner

with st.sidebar:
    # Logo - Clipbard Style
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
    
    # Navigation - Blue & White Theme
    st.markdown("### 🧭 Navigation")
    
    # Initialize page state
    if "current_page" not in st.session_state:
        st.session_state.current_page = "📊 Analytics"
    
    # Use buttons for navigation instead of radio
    col1, col2 = st.columns(2)
    with col1:
        analytics_active = st.session_state.current_page == "📊 Analytics"
        if st.button("📊 Analytics", key="nav_analytics", use_container_width=True, type="primary" if analytics_active else "secondary"):
            st.session_state.current_page = "📊 Analytics"
            st.rerun()
    with col2:
        profile_active = st.session_state.current_page == "👤 Profile"
        if st.button("👤 Profile", key="nav_profile", use_container_width=True, type="primary" if profile_active else "secondary"):
            st.session_state.current_page = "👤 Profile"
            st.rerun()
    
    page = st.session_state.current_page

    st.markdown("<div style='margin-top: 0.75rem;'></div>", unsafe_allow_html=True)
    
    # API Key Configuration
    st.markdown("### ⚙️ Configuration")
    api_key = st.text_input(
        "Claude API Key",
        type="password",
        help="Get your key at console.anthropic.com",
        label_visibility="visible"
    )
    
    st.markdown("<div style='margin-top: 0.75rem;'></div>", unsafe_allow_html=True)
    
    # Capabilities Section
    st.markdown("### 🎯 Capabilities")
    st.markdown("""
    - 🤖 Natural language queries
    - 📊 Statistical testing
    - 🔮 ML forecasting
    - 📈 Auto-visualization
    - 🔍 Advanced insights
    - 📝 Executive summaries
    """)
    
    st.markdown("<div style='margin-top: 0.75rem;'></div>", unsafe_allow_html=True)
    
    # Example Questions
    st.markdown("### 📚 Example Questions")
    st.code("What is the average revenue?")
    st.code("Show correlation analysis")
    st.code("Forecast next month")
    st.code("Generate summary")
    
    # Footer Links - Clipbard Style
    st.markdown("""
    <div style="margin-top: auto; padding-top: 2rem;">
        <a href="#" style="color: #A0AEC0; text-decoration: none; font-size: 0.875rem; display: inline-block; margin-right: 1rem;">Privacy Policy</a>
        <a href="#" style="color: #A0AEC0; text-decoration: none; font-size: 0.875rem;">Terms</a>
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
# CHATGPT-LIKE CHAT INTERFACE
# =========================

# Initialize session state variables
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []
if "df" not in st.session_state:
    st.session_state.df = None

# =========================
# MAIN CONTENT
# =========================

if page == "📊 Analytics":
    # Initialize chat messages (already done above, but keeping for safety)
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []
    if "df" not in st.session_state:
        st.session_state.df = None
    
    # Header Section
    st.markdown("""
    <div style="text-align: center; margin-top: -2rem; margin-bottom: 1.5rem;">
        <h1 style="font-size: 2.5rem; font-weight: 700; color: #1E293B; margin-bottom: 0.5rem; background: linear-gradient(135deg, #2563EB 0%, #1E40AF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
            AI Powered Data Analysis
        </h1>
        <p style="font-size: 1.125rem; color: #64748B; font-weight: 400; margin-top: 0.5rem;">
            Transform your data into actionable insights with intelligent analytics
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quote Section at Top
    st.markdown("""
    <div style="background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%); padding: 2.5rem; border-radius: 12px; margin-bottom: 2rem; border-left: 4px solid #2563EB; box-shadow: 0 2px 8px rgba(37, 99, 235, 0.1);">
        <p style="font-size: 1.35rem; font-weight: 500; color: #1E293B; line-height: 1.8; margin: 0; font-style: italic; text-align: center;">
            "Data is the new oil. It's valuable, but if unrefined it cannot really be used. It has to be changed into gas, plastic, chemicals, etc. to create a valuable entity that drives profitable activity; so must data be broken down, analyzed for it to have value."
        </p>
        <p style="text-align: right; margin-top: 1.5rem; color: #475569; font-weight: 600; font-size: 1rem;">
            — Clive Humby
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # ChatGPT-like Chat Interface
    st.markdown("""
    <style>
    .chat-message {
        padding: 1.5rem;
        margin-bottom: 1rem;
        border-radius: 8px;
        animation: fadeIn 0.3s;
    }
    .chat-message.user {
        background: var(--accent-blue-bg);
        border-left: 4px solid var(--accent-blue);
    }
    .chat-message.assistant {
        background: var(--bg-card);
    }
    .message-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 0.75rem;
    }
    .message-avatar {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        font-size: 0.875rem;
    }
    .message-avatar.user {
        background: var(--accent-blue);
        color: white;
    }
    .message-avatar.assistant {
        background: var(--text-secondary);
        color: white;
    }
    .welcome-message {
        text-align: center;
        padding: 4rem 2rem;
        color: var(--text-secondary);
    }
    .welcome-message h1 {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 1rem;
    }
    .welcome-message ul {
        color: var(--text-secondary);
        line-height: 1.8;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Display welcome message if no messages
    if len(st.session_state.chat_messages) == 0:
        st.markdown("""
        <div class="welcome-message">
            <h1>InsightForge</h1>
            <p style="font-size: 1.25rem; margin-bottom: 2rem;">Upload a CSV file or ask me anything about your data</p>
            <p style="font-size: 1rem; color: var(--text-muted); margin-bottom: 1rem;">
                I can help you with:
            </p>
            <ul style="text-align: left; display: inline-block; color: var(--text-muted); font-size: 0.95rem;">
                <li>Natural language data queries</li>
                <li>Statistical analysis & hypothesis testing</li>
                <li>Machine learning predictions & forecasting</li>
                <li>Distribution analysis & correlation</li>
                <li>Advanced insights & executive summaries</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Display chat messages
    for msg in st.session_state.chat_messages:
        role = msg.get("role", "assistant")
        content = msg.get("content", "")
        
        if role == "user":
            st.markdown(f"""
            <div class="chat-message user">
                <div class="message-header">
                    <div class="message-avatar user">You</div>
                </div>
                <div style="color: var(--text-primary); line-height: 1.6;">{content}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message assistant">
                <div class="message-header">
                    <div class="message-avatar assistant">AI</div>
                </div>
                <div style="color: var(--text-primary); line-height: 1.6;">{content}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Display dataframes
        if "dataframe" in msg:
            st.dataframe(msg["dataframe"], use_container_width=True)
        
        # Display charts
        if "chart" in msg:
            st.plotly_chart(msg["chart"], use_container_width=True)
    
    # Chat Input Area
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # File uploader
    uploaded_file = st.file_uploader(
        "📎 Upload CSV file",
        type=["csv"],
        help="Upload a CSV file to analyze",
        label_visibility="collapsed",
        key="file_uploader_chat"
    )

    # Handle file upload
    if uploaded_file and st.session_state.df is None:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state.df = df
            
            # Add assistant message about file upload
            st.session_state.chat_messages.append({
                "role": "assistant",
                "content": f"✅ I've loaded your dataset! It has **{len(df)} rows** and **{len(df.columns)} columns**.\n\n**Columns:** {', '.join(df.columns.tolist())}\n\nWhat would you like to know about this data?"
            })
            st.rerun()
        except Exception as e:
            st.session_state.chat_messages.append({
                "role": "assistant",
                "content": f"❌ Error loading file: {str(e)}"
            })
            st.rerun()
    
    # Text input for chat
    user_question = st.text_area(
        "Type your message...",
        height=100,
        placeholder="Ask me anything about your data, or upload a CSV file to get started...",
        label_visibility="collapsed",
        key="chat_input"
    )
    
    col1, col2 = st.columns([0.9, 0.1])
    with col2:
        send_button = st.button("Send", type="primary", use_container_width=True)
    
    # Handle user input
    if send_button and user_question:
        # Add user message
        st.session_state.chat_messages.append({
            "role": "user",
            "content": user_question
        })
        
        # Process the message
        if st.session_state.df is not None:
            df = st.session_state.df
            
            if api_key:
                # Use AI to answer
                with st.spinner("Thinking..."):
                    try:
                        client = Anthropic(api_key=api_key)
                        
                        # Determine if visualization is needed
                        viz_prompt = f"""Given this data question: "{user_question}"

Should this be visualized? Respond with ONLY ONE WORD:
- "line" (for trends over time)
- "bar" (for comparisons)
- "histogram" (for distributions)
- "scatter" (for relationships)
- "pie" (for proportions)
- "none" (if just a number/text answer)
"""
                        
                        viz_response = client.messages.create(
                            model="claude-sonnet-4-5-20250929",
                            max_tokens=100,
                            messages=[{"role": "user", "content": viz_prompt}]
                        )
                        
                        chart_type = viz_response.content[0].text.strip().lower()
                        
                        # Generate pandas code
                        columns = df.columns.tolist()
                        sample_data = df.head(3).to_string()
                        
                        code_prompt = f"""You are a data scientist with access to advanced libraries.
Given a dataframe with these columns: {columns}

Sample data:
{sample_data}

Available libraries: 
- pandas (pd), numpy (np)
- scipy.stats (stats) - for statistical tests
- plotly.express (px), plotly.graph_objects (go) - for visualizations
- sklearn: LinearRegression, RandomForestRegressor, mean_absolute_error, r2_score

User question: {user_question}

Generate valid Python code that answers this question.
Use 'df' as the dataframe variable name.
Store the result in a variable called 'result'.
If creating a chart, also create variables for x and y axes.
You can use:
- Statistical tests (correlation, t-tests, normality tests)
- ML models (LinearRegression, RandomForestRegressor)
- Advanced visualizations (heatmaps, distributions, forecasts)

Only output code. No markdown, no backticks, no explanation.

Examples:
# Simple aggregation:
result = df.groupby('month')['revenue'].sum()
x_data = result.index
y_data = result.values

# Correlation:
result = df[numeric_cols].corr()
# For correlation heatmap, use px.imshow(result)

# Statistical test:
from scipy.stats import pearsonr
corr_coef, p_value = pearsonr(df['col1'], df['col2'])
result = f"Correlation: {{corr_coef:.4f}}, p-value: {{p_value:.4f}}"
"""
                        
                        code_response = client.messages.create(
                            model="claude-sonnet-4-5-20250929",
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
                        
                        # Execute code with advanced libraries
                        local_vars = {
                            "df": df, 
                            "pd": pd, 
                            "np": np,
                            "stats": stats,
                            "px": px,
                            "go": go,
                            "LinearRegression": LinearRegression,
                            "RandomForestRegressor": RandomForestRegressor,
                            "mean_absolute_error": mean_absolute_error,
                            "r2_score": r2_score
                        }
                        exec(code, {}, local_vars)
                        
                        # Prepare response
                        response_message = {
                            "role": "assistant",
                            "content": ""
                        }
                        
                        if 'result' in local_vars:
                            result = local_vars['result']
                            
                            if isinstance(result, (int, float)):
                                response_message["content"] = f"The answer is: **{result:,.2f}**"
                            elif isinstance(result, pd.Series):
                                response_message["content"] = f"Here are the results:"
                                response_message["dataframe"] = pd.DataFrame(result).T
                            elif isinstance(result, pd.DataFrame):
                                response_message["content"] = "Here's the analysis:"
                                response_message["dataframe"] = result
                            else:
                                response_message["content"] = str(result)
                            
                            # Create visualization if needed
                            if chart_type != "none" and 'x_data' in local_vars and 'y_data' in local_vars:
                                x_data = local_vars.get('x_data', [])
                                y_data = local_vars.get('y_data', [])
                                
                                chart_colors = ['#2563EB', '#3B82F6', '#60A5FA', '#93C5FD']
                                
                                if chart_type == "line":
                                    fig = px.line(x=x_data, y=y_data, markers=True, color_discrete_sequence=chart_colors)
                                elif chart_type == "bar":
                                    fig = px.bar(x=x_data, y=y_data, color_discrete_sequence=chart_colors)
                                elif chart_type == "histogram":
                                    fig = px.histogram(df, x=df.columns[0], color_discrete_sequence=chart_colors)
                                elif chart_type == "scatter":
                                    fig = px.scatter(x=x_data, y=y_data, color_discrete_sequence=chart_colors)
                                else:
                                    fig = px.bar(x=x_data, y=y_data, color_discrete_sequence=chart_colors)
                                
                                fig.update_layout(
                                    plot_bgcolor='#FFFFFF',
                                    paper_bgcolor='#FFFFFF',
                                    font=dict(color='#1E293B', family="Inter, sans-serif", size=12),
                                    xaxis=dict(gridcolor='#E2E8F0', linecolor='#CBD5E1'),
                                    yaxis=dict(gridcolor='#E2E8F0', linecolor='#CBD5E1')
                                )
                                
                                response_message["chart"] = fig
                        
                        st.session_state.chat_messages.append(response_message)
                        
                    except Exception as e:
                        st.session_state.chat_messages.append({
                            "role": "assistant",
                            "content": f"❌ Error: {str(e)}\n\nPlease check your API key and try again."
                        })
            else:
                st.session_state.chat_messages.append({
                    "role": "assistant",
                    "content": "I can see your data, but I need your Claude API key to answer questions. Please enter it in the sidebar settings."
                })
        else:
            # No data uploaded
            if "upload" in user_question.lower() or "file" in user_question.lower():
                st.session_state.chat_messages.append({
                    "role": "assistant",
                    "content": "Please use the file upload button (📎) above to upload a CSV file."
                })
            else:
                st.session_state.chat_messages.append({
                    "role": "assistant",
                    "content": "Hello! I'm InsightForge, your AI data analyst. To get started, please upload a CSV file using the upload button (📎) above. Once you upload data, I can help you analyze it, answer questions, and create visualizations!"
                })
        
        st.rerun()
    
    # =========================
    # ADVANCED FEATURES SECTIONS
    # =========================
    
    if st.session_state.df is not None:
        df = st.session_state.df
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        
        st.markdown("<hr style='border-color: var(--border-gray); margin: 3rem 0;'>", unsafe_allow_html=True)
        
        # Advanced Features Tabs
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📊 Statistical Analysis", 
            "🔮 ML Predictions", 
            "📈 Distributions", 
            "🔍 Advanced Insights",
            "📝 Executive Summary"
        ])
        
        with tab1:
            st.markdown("### 📊 Statistical Analysis")
            
            if len(numeric_cols) >= 2:
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Correlation Analysis")
                    corr_matrix = df[numeric_cols].corr()
                    
                    fig = px.imshow(
                        corr_matrix,
                        labels=dict(color="Correlation"),
                        color_continuous_scale='Blues',
                        aspect="auto",
                        title="Correlation Heatmap"
                    )
                    fig.update_layout(
                        plot_bgcolor='#FFFFFF',
                        paper_bgcolor='#FFFFFF',
                        font=dict(color='#1E293B', family="Inter, sans-serif", size=12)
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Find strong correlations
                    strong_corr = []
                    for i in range(len(corr_matrix.columns)):
                        for j in range(i+1, len(corr_matrix.columns)):
                            if abs(corr_matrix.iloc[i, j]) > 0.5:
                                strong_corr.append({
                                    'Var1': corr_matrix.columns[i],
                                    'Var2': corr_matrix.columns[j],
                                    'Correlation': corr_matrix.iloc[i, j]
                                })
                    
                    if strong_corr:
                        st.success(f"Found {len(strong_corr)} strong correlations")
                        st.dataframe(pd.DataFrame(strong_corr), use_container_width=True)
                
                with col2:
                    st.subheader("Hypothesis Testing")
                    
                    if len(numeric_cols) >= 2:
                        col_a, col_b = numeric_cols[0], numeric_cols[1]
                        data_a = df[col_a].dropna()
                        data_b = df[col_b].dropna()
                        
                        if len(data_a) > 1 and len(data_b) > 1:
                            # Normality test
                            _, p_norm_a = stats.shapiro(data_a[:5000])
                            _, p_norm_b = stats.shapiro(data_b[:5000])
                            
                            st.markdown(f"**Normality Tests:**")
                            st.write(f"- {col_a}: {'Normal' if p_norm_a > 0.05 else 'Non-normal'} (p={p_norm_a:.4f})")
                            st.write(f"- {col_b}: {'Normal' if p_norm_b > 0.05 else 'Non-normal'} (p={p_norm_b:.4f})")
                            
                            # Correlation test
                            corr_coef, p_value = stats.pearsonr(data_a, data_b)
                            
                            st.markdown(f"**Pearson Correlation:**")
                            st.write(f"- Coefficient: {corr_coef:.4f}")
                            st.write(f"- P-value: {p_value:.4f}")
                            
                            if p_value < 0.05:
                                st.success(f"✅ Significant correlation detected (p < 0.05)")
                            else:
                                st.info(f"ℹ️ No significant correlation (p >= 0.05)")
        
        with tab2:
            st.markdown("### 🔮 Machine Learning Predictions")
            
            ml_task = st.selectbox(
                "Select ML task",
                ["Time Series Forecasting", "Feature Prediction", "Anomaly Detection"],
                key="ml_task"
            )
            
            if ml_task == "Time Series Forecasting" and len(numeric_cols) >= 1:
                st.subheader("🔮 Forecast Future Values")
                
                target_col = st.selectbox("Select column to forecast", numeric_cols, key="forecast_col")
                forecast_periods = st.slider("Forecast periods", 1, 12, 3, key="forecast_periods")
                
                if st.button("🚀 Generate Forecast", type="primary", key="forecast_btn"):
                    with st.spinner("Training models..."):
                        data = df[target_col].dropna().values
                        
                        if len(data) > 3:
                            X = np.arange(len(data)).reshape(-1, 1)
                            y = data
                            
                            train_size = int(len(data) * 0.8)
                            X_train, X_test = X[:train_size], X[train_size:]
                            y_train, y_test = y[:train_size], y[train_size:]
                            
                            models = {
                                'Linear Regression': LinearRegression(),
                                'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42)
                            }
                            
                            results = {}
                            
                            for name, model in models.items():
                                model.fit(X_train, y_train)
                                y_pred = model.predict(X_test)
                                
                                mae = mean_absolute_error(y_test, y_pred)
                                r2 = r2_score(y_test, y_pred)
                                
                                results[name] = {
                                    'model': model,
                                    'MAE': mae,
                                    'R²': r2,
                                    'predictions': y_pred
                                }
                            
                            st.subheader("📊 Model Performance")
                            
                            col1, col2 = st.columns(2)
                            
                            with col1:
                                comparison_df = pd.DataFrame({
                                    'Model': list(results.keys()),
                                    'MAE': [r['MAE'] for r in results.values()],
                                    'R² Score': [r['R²'] for r in results.values()]
                                })
                                st.dataframe(comparison_df, use_container_width=True)
                            
                            with col2:
                                best_model_name = min(results, key=lambda k: results[k]['MAE'])
                                st.success(f"🏆 Best Model: **{best_model_name}**")
                                st.metric("MAE", f"{results[best_model_name]['MAE']:.2f}")
                                st.metric("R² Score", f"{results[best_model_name]['R²']:.4f}")
                            
                            # Generate forecasts
                            best_model = results[best_model_name]['model']
                            future_X = np.arange(len(data), len(data) + forecast_periods).reshape(-1, 1)
                            future_pred = best_model.predict(future_X)
                            
                            # Visualization
                            fig = go.Figure()
                            
                            fig.add_trace(go.Scatter(
                                x=list(range(len(data))),
                                y=data,
                                mode='lines+markers',
                                name='Historical',
                                line=dict(color='#2563EB', width=2)
                            ))
                            
                            fig.add_trace(go.Scatter(
                                x=list(range(len(data), len(data) + forecast_periods)),
                                y=future_pred,
                                mode='lines+markers',
                                name='Forecast',
                                line=dict(color='#DC2626', dash='dash', width=2)
                            ))
                            
                            fig.update_layout(
                                title=f"{target_col} - Historical vs Forecast",
                                xaxis_title="Time Period",
                                yaxis_title=target_col,
                                plot_bgcolor='#FFFFFF',
                                paper_bgcolor='#FFFFFF',
                                font=dict(color='#1E293B', family="Inter, sans-serif", size=12),
                                xaxis=dict(gridcolor='#E2E8F0', linecolor='#CBD5E1'),
                                yaxis=dict(gridcolor='#E2E8F0', linecolor='#CBD5E1'),
                                hovermode='x unified'
                            )
                            
                            st.plotly_chart(fig, use_container_width=True)
                            
                            # Forecast values table
                            st.subheader("📋 Forecasted Values")
                            forecast_df = pd.DataFrame({
                                'Period': [f"T+{i+1}" for i in range(forecast_periods)],
                                'Predicted Value': future_pred.round(2)
                            })
                            st.dataframe(forecast_df, use_container_width=True)
                        else:
                            st.warning("Need at least 4 data points for forecasting")
            
            elif ml_task == "Feature Prediction" and len(numeric_cols) >= 2:
                st.subheader("🎯 Predict Target Variable")
                
                target = st.selectbox("Select target variable", numeric_cols, key="target_var")
                
                if st.button("🚀 Train Model", type="primary", key="train_btn"):
                    with st.spinner("Training..."):
                        features = [col for col in numeric_cols if col != target]
                        
                        X = df[features].dropna()
                        y = df.loc[X.index, target]
                        
                        train_size = int(len(X) * 0.8)
                        X_train, X_test = X[:train_size], X[train_size:]
                        y_train, y_test = y[:train_size], y[train_size:]
                        
                        model = RandomForestRegressor(n_estimators=100, random_state=42)
                        model.fit(X_train, y_train)
                        
                        y_pred = model.predict(X_test)
                        
                        mae = mean_absolute_error(y_test, y_pred)
                        r2 = r2_score(y_test, y_pred)
                        
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("MAE", f"{mae:.2f}")
                        with col2:
                            st.metric("R² Score", f"{r2:.4f}")
                        with col3:
                            accuracy = (1 - mae / y_test.mean()) * 100 if y_test.mean() != 0 else 0
                            st.metric("Accuracy", f"{accuracy:.1f}%")
                        
                        # Feature importance
                        st.subheader("📊 Feature Importance")
                        
                        importance_df = pd.DataFrame({
                            'Feature': features,
                            'Importance': model.feature_importances_
                        }).sort_values('Importance', ascending=False)
                        
                        fig = px.bar(importance_df, x='Importance', y='Feature', orientation='h', color_discrete_sequence=['#2563EB'])
                        fig.update_layout(
                            plot_bgcolor='#FFFFFF',
                            paper_bgcolor='#FFFFFF',
                            font=dict(color='#1E293B', family="Inter, sans-serif", size=12),
                            xaxis=dict(gridcolor='#E2E8F0', linecolor='#CBD5E1'),
                            yaxis=dict(gridcolor='#E2E8F0', linecolor='#CBD5E1')
                        )
                        st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            st.markdown("### 📉 Distribution Analysis")
            
            if len(numeric_cols) > 0:
                dist_col = st.selectbox("Select column for distribution analysis", numeric_cols, key="dist_col")
                
                if dist_col:
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        data = df[dist_col].dropna()
                        
                        fig = go.Figure()
                        fig.add_trace(go.Histogram(x=data, name='Data', nbinsx=30, marker_color='#2563EB', opacity=0.7))
                        
                        # Add normal distribution overlay
                        mu, sigma = data.mean(), data.std()
                        x_range = np.linspace(data.min(), data.max(), 100)
                        normal_dist = stats.norm.pdf(x_range, mu, sigma) * len(data) * (data.max() - data.min()) / 30
                        
                        fig.add_trace(go.Scatter(
                            x=x_range, 
                            y=normal_dist, 
                            mode='lines', 
                            name='Normal Distribution',
                            line=dict(color='#DC2626', width=2)
                        ))
                        
                        fig.update_layout(
                            title=f"Distribution of {dist_col}",
                            xaxis_title=dist_col,
                            yaxis_title="Frequency",
                            plot_bgcolor='#FFFFFF',
                            paper_bgcolor='#FFFFFF',
                            font=dict(color='#1E293B', family="Inter, sans-serif", size=12),
                            xaxis=dict(gridcolor='#E2E8F0', linecolor='#CBD5E1'),
                            yaxis=dict(gridcolor='#E2E8F0', linecolor='#CBD5E1')
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    
                    with col2:
                        st.markdown("**Distribution Metrics:**")
                        st.write(f"Mean: {data.mean():.2f}")
                        st.write(f"Median: {data.median():.2f}")
                        st.write(f"Std Dev: {data.std():.2f}")
                        st.write(f"Skewness: {stats.skew(data):.2f}")
                        st.write(f"Kurtosis: {stats.kurtosis(data):.2f}")
                        
                        confidence = 0.95
                        ci = stats.t.interval(confidence, len(data)-1, loc=data.mean(), scale=stats.sem(data))
                        st.write(f"\n**95% Confidence Interval:**")
                        st.write(f"[{ci[0]:.2f}, {ci[1]:.2f}]")
        
        with tab4:
            st.markdown("### 🔍 Advanced Insights")
            
            if st.button("🔍 Generate Deep Insights", type="primary", key="insights_btn"):
                with st.spinner("Analyzing patterns..."):
                    insights = []
                    
                    # Outlier detection (Z-score method)
                    for col in numeric_cols[:3]:
                        data = df[col].dropna()
                        z_scores = np.abs(stats.zscore(data))
                        outliers = data[z_scores > 3]
                        
                        if len(outliers) > 0:
                            insights.append({
                                'type': 'warning',
                                'title': f"⚠️ Outliers Detected in '{col}'",
                                'message': f"Found {len(outliers)} extreme values (>3 std dev). Range: {outliers.min():.2f} to {outliers.max():.2f}"
                            })
                    
                    # Statistical significance of trends
                    for col in numeric_cols[:2]:
                        data = df[col].dropna()
                        if len(data) > 3:
                            X = np.arange(len(data)).reshape(-1, 1)
                            y = data.values
                            
                            model = LinearRegression()
                            model.fit(X, y)
                            
                            slope = model.coef_[0]
                            
                            if abs(slope) > data.std() * 0.1:
                                trend = "upward" if slope > 0 else "downward"
                                insights.append({
                                    'type': 'success',
                                    'title': f"📈 Significant {trend.capitalize()} Trend in '{col}'",
                                    'message': f"Slope: {slope:.2f} per period (statistically significant)"
                                })
                    
                    # Value concentration analysis
                    for col in numeric_cols[:2]:
                        data = df[col].dropna()
                        top_20_pct = data.quantile(0.8)
                        top_values_sum = data[data >= top_20_pct].sum()
                        total_sum = data.sum()
                        
                        concentration = (top_values_sum / total_sum) * 100
                        
                        if concentration > 50:
                            insights.append({
                                'type': 'info',
                                'title': f"📊 High Concentration in '{col}'",
                                'message': f"Top 20% of values account for {concentration:.1f}% of total"
                            })
                    
                    # Display insights
                    for insight in insights:
                        if insight['type'] == 'warning':
                            st.warning(f"**{insight['title']}**\n\n{insight['message']}")
                        elif insight['type'] == 'success':
                            st.success(f"**{insight['title']}**\n\n{insight['message']}")
                        else:
                            st.info(f"**{insight['title']}**\n\n{insight['message']}")
        
        with tab5:
            st.markdown("### 📝 Executive Summary")
            
            if st.button("📝 Generate Executive Summary", type="primary", key="summary_btn"):
                if api_key:
                    with st.spinner("Creating comprehensive summary..."):
                        try:
                            stats_summary = df.describe().to_string()
                            correlations = df[numeric_cols].corr().to_string() if len(numeric_cols) > 1 else "N/A"
                            
                            summary_prompt = f"""You are a senior data scientist presenting to executives.

Data overview:
- {len(df):,} rows, {len(df.columns)} columns
- Columns: {', '.join(df.columns.tolist())}

Statistical Summary:
{stats_summary}

Correlations:
{correlations}

Generate a comprehensive executive summary with:
1. **Key Findings** (3-4 data-driven insights)
2. **Statistical Significance** (mention correlations, trends)
3. **Business Implications** (what this means)
4. **Recommendations** (actionable next steps)

Use clear, business-friendly language with specific numbers."""

                            client = Anthropic(api_key=api_key)
                            summary_response = client.messages.create(
                                model="claude-sonnet-4-5-20250929",
                                max_tokens=2048,
                                messages=[{"role": "user", "content": summary_prompt}]
                            )
                            
                            summary = summary_response.content[0].text
                            
                            st.markdown("### 📋 Executive Summary")
                            st.markdown(summary)
                            
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
                else:
                    st.warning("Please enter your API key in the sidebar")
    
    # Chat interface complete

elif page == "👤 Profile":
    # Profile Page - Clipbard Style
    st.markdown("""
    <div class="profile-card">
        <h2>Profile</h2>
        <div style="margin-bottom: 1.5rem;">
            <label class="profile-input-label">Username</label>
            <input type="text" class="profile-input-field" value="Oumaima Bouanani" readonly style="background: var(--bg-main); border: 1px solid var(--border-gray); color: var(--text-primary); padding: 0.75rem 1rem; border-radius: 8px; width: 100%;">
        </div>
        <div style="margin-bottom: 1.5rem;">
            <label class="profile-input-label">Email</label>
            <input type="email" class="profile-input-field" value="oumaima123bouanani@gmail.com" readonly style="background: var(--bg-main); border: 1px solid var(--border-gray); color: var(--text-primary); padding: 0.75rem 1rem; border-radius: 8px; width: 100%;">
        </div>
        <div style="text-align: right;">
            <button style="background: var(--accent-blue); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s;" onmouseover="this.style.background='var(--accent-blue-dark)'" onmouseout="this.style.background='var(--accent-blue)'">Edit Profile</button>
        </div>
    </div>
    
    <div class="profile-card-danger">
        <h2>Delete Account</h2>
        <p style="color: var(--text-secondary); margin-bottom: 1.5rem; line-height: 1.6;">
            Once your account is deleted, all of your data will be permanently lost. Please be certain before proceeding.
        </p>
        <button style="background: var(--accent-red); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s;" onmouseover="this.style.background='var(--accent-red-alt)'" onmouseout="this.style.background='var(--accent-red)'">Delete My Account</button>
    </div>
    """, unsafe_allow_html=True)
