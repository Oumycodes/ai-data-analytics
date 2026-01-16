import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from anthropic import Anthropic
import numpy as np
from datetime import datetime
import json

# =========================
# CHATGPT-INSPIRED STYLE CSS
# =========================
chat_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    /* Root Variables - ChatGPT-inspired */
    :root {
        --bg-main: #343541;
        --bg-sidebar: #202123;
        --bg-message-user: #444654;
        --bg-message-assistant: #343541;
        --bg-input: #40414f;
        --text-primary: #ececf1;
        --text-secondary: #8e8ea0;
        --accent-green: #10a37f;
        --border-gray: #565869;
    }
    
    /* Main App Background */
    .main {
        background-color: var(--bg-main) !important;
        color: var(--text-primary);
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: var(--bg-sidebar) !important;
        border-right: 1px solid var(--border-gray);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: var(--bg-sidebar) !important;
        padding: 1rem;
    }
    
    /* Chat Container */
    .chat-container {
        display: flex;
        flex-direction: column;
        height: calc(100vh - 120px);
        max-width: 768px;
        margin: 0 auto;
        padding: 1rem;
    }
    
    /* Chat Messages */
    .chat-message {
        padding: 1.5rem;
        margin-bottom: 1rem;
        border-radius: 8px;
        animation: fadeIn 0.3s;
    }
    
    .chat-message.user {
        background: var(--bg-message-user);
    }
    
    .chat-message.assistant {
        background: var(--bg-message-assistant);
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
        border-radius: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        font-size: 0.875rem;
    }
    
    .message-avatar.user {
        background: var(--accent-green);
        color: white;
    }
    
    .message-avatar.assistant {
        background: #5436da;
        color: white;
    }
    
    .message-content {
        line-height: 1.6;
        color: var(--text-primary);
    }
    
    /* Input Area */
    .chat-input-container {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: var(--bg-main);
        border-top: 1px solid var(--border-gray);
        padding: 1rem;
        z-index: 100;
    }
    
    .chat-input-wrapper {
        max-width: 768px;
        margin: 0 auto;
        display: flex;
        gap: 0.5rem;
        align-items: flex-end;
    }
    
    .chat-input {
        flex: 1;
        background: var(--bg-input);
        border: 1px solid var(--border-gray);
        border-radius: 12px;
        padding: 0.75rem 1rem;
        color: var(--text-primary);
        font-size: 1rem;
        resize: none;
        min-height: 52px;
        max-height: 200px;
    }
    
    .chat-input:focus {
        outline: none;
        border-color: var(--accent-green);
    }
    
    .chat-send-button {
        background: var(--accent-green);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.2s;
    }
    
    .chat-send-button:hover {
        background: #0d8a6a;
    }
    
    .chat-send-button:disabled {
        opacity: 0.5;
        cursor: not-allowed;
    }
    
    /* File Upload in Chat */
    .file-upload-chat {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem;
        background: var(--bg-input);
        border-radius: 8px;
        margin-top: 0.5rem;
    }
    
    /* Welcome Message */
    .welcome-message {
        text-align: center;
        padding: 3rem 1rem;
        color: var(--text-secondary);
    }
    
    .welcome-message h1 {
        font-size: 2rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
    }
    
    .welcome-message p {
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
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
        background: var(--bg-sidebar);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--border-gray);
        border-radius: 4px;
    }
</style>
"""

st.markdown(chat_css, unsafe_allow_html=True)

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="InsightForge Chat",
    layout="wide",
    page_icon="💬",
    initial_sidebar_state="collapsed"
)

# =========================
# INITIALIZE SESSION STATE
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []
if "df" not in st.session_state:
    st.session_state.df = None
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

# =========================
# SIDEBAR - MINIMAL
# =========================
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    
    api_key = st.text_input(
        "Claude API Key",
        type="password",
        value=st.session_state.api_key,
        help="Get your key at console.anthropic.com",
        label_visibility="visible"
    )
    st.session_state.api_key = api_key
    
    st.divider()
    
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.df = None
        st.rerun()
    
    st.divider()
    
    st.markdown("""
    <div style="font-size: 0.875rem; color: var(--text-secondary);">
        <p><strong>InsightForge Chat</strong></p>
        <p>AI-powered data analytics</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# MAIN CHAT INTERFACE
# =========================

# Display welcome message if no messages
if len(st.session_state.messages) == 0:
    st.markdown("""
    <div class="welcome-message">
        <h1>InsightForge</h1>
        <p>Upload a CSV file or ask me anything about your data</p>
        <p style="font-size: 0.875rem; color: var(--text-secondary);">
            I can help you analyze data, create visualizations, and answer questions
        </p>
    </div>
    """, unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    
    with st.container():
        if role == "user":
            st.markdown(f"""
            <div class="chat-message user">
                <div class="message-header">
                    <div class="message-avatar user">You</div>
                </div>
                <div class="message-content">{content}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message assistant">
                <div class="message-header">
                    <div class="message-avatar assistant">AI</div>
                </div>
                <div class="message-content">{content}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Display dataframes if present
        if "dataframe" in message:
            st.dataframe(message["dataframe"], use_container_width=True)
        
        # Display charts if present
        if "chart" in message:
            st.plotly_chart(message["chart"], use_container_width=True)

# =========================
# CHAT INPUT AREA
# =========================
st.markdown("<br><br><br>", unsafe_allow_html=True)  # Space for fixed input

col1, col2 = st.columns([1, 0.1])

with col1:
    # File uploader
    uploaded_file = st.file_uploader(
        "📎 Upload CSV file",
        type=["csv"],
        help="Upload a CSV file to analyze",
        label_visibility="collapsed",
        key="file_uploader"
    )
    
    if uploaded_file and st.session_state.df is None:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state.df = df
            
            # Add system message about file upload
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"✅ I've loaded your dataset! It has {len(df)} rows and {len(df.columns)} columns.\n\n**Columns:** {', '.join(df.columns.tolist())}\n\nWhat would you like to know about this data?"
            })
            st.rerun()
        except Exception as e:
            st.error(f"Error loading file: {str(e)}")
    
    # Text input
    user_input = st.text_area(
        "Type your message...",
        height=100,
        placeholder="Ask me anything about your data, or upload a CSV file to get started...",
        label_visibility="collapsed",
        key="chat_input"
    )

with col2:
    send_button = st.button("Send", type="primary", use_container_width=True)

# Handle user input
if send_button and user_input:
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Process the message
    if st.session_state.df is not None:
        # We have data, process the question
        df = st.session_state.df
        
        if st.session_state.api_key:
            # Use AI to answer
            with st.spinner("Thinking..."):
                try:
                    client = Anthropic(api_key=st.session_state.api_key)
                    
                    # Determine if visualization is needed
                    viz_prompt = f"""Given this data question: "{user_input}"

Should this be visualized? Respond with ONLY ONE WORD:
- "line" (for trends over time)
- "bar" (for comparisons)
- "histogram" (for distributions)
- "scatter" (for relationships)
- "pie" (for proportions)
- "none" (if just a number/text answer)
"""
                    
                    viz_response = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=100,
                        messages=[{"role": "user", "content": viz_prompt}]
                    )
                    
                    chart_type = viz_response.content[0].text.strip().lower()
                    
                    # Generate pandas code
                    columns = df.columns.tolist()
                    sample_data = df.head(3).to_string()
                    
                    code_prompt = f"""You are a data analyst. 
Given a dataframe with these columns: {columns}

Sample data:
{sample_data}

User question: {user_input}

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
                    
                    # Execute code
                    local_vars = {"df": df, "pd": pd, "np": np}
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
                            response_message["content"] = f"Here are the results:\n\n{result.to_string()}"
                        elif isinstance(result, pd.DataFrame):
                            response_message["content"] = "Here's the analysis:"
                            response_message["dataframe"] = result
                        else:
                            response_message["content"] = str(result)
                        
                        # Create visualization if needed
                        if chart_type != "none" and 'x_data' in local_vars and 'y_data' in local_vars:
                            x_data = local_vars.get('x_data', [])
                            y_data = local_vars.get('y_data', [])
                            
                            chart_colors = ['#10a37f', '#5436da', '#8e8ea0']
                            
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
                                plot_bgcolor='#343541',
                                paper_bgcolor='#343541',
                                font=dict(color='#ececf1', family="Inter, sans-serif"),
                                xaxis=dict(gridcolor='#565869'),
                                yaxis=dict(gridcolor='#565869')
                            )
                            
                            response_message["chart"] = fig
                    
                    st.session_state.messages.append(response_message)
                    
                except Exception as e:
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": f"❌ Error: {str(e)}\n\nPlease check your API key and try again."
                    })
        else:
            # No API key, provide basic response
            st.session_state.messages.append({
                "role": "assistant",
                "content": "I can see your data, but I need your Claude API key to answer questions. Please enter it in the sidebar settings."
            })
    else:
        # No data uploaded
        if "upload" in user_input.lower() or "file" in user_input.lower():
            st.session_state.messages.append({
                "role": "assistant",
                "content": "Please use the file upload button (📎) above to upload a CSV file, or drag and drop it here."
            })
        else:
            st.session_state.messages.append({
                "role": "assistant",
                "content": "Hello! I'm InsightForge, your AI data analyst. To get started, please upload a CSV file using the upload button (📎) above. Once you upload data, I can help you analyze it, answer questions, and create visualizations!"
            })
    
    st.rerun()
