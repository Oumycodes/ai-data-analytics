#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Starting InsightForge Services...${NC}\n"

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Function to cleanup on exit
cleanup() {
    echo -e "\n${YELLOW}Stopping services...${NC}"
    kill $STREAMLIT_PID $NEXTJS_PID 2>/dev/null
    exit
}

# Trap Ctrl+C
trap cleanup INT TERM

# Start Streamlit
echo -e "${GREEN}Starting Streamlit app...${NC}"
cd "$SCRIPT_DIR"
streamlit run app.py > /dev/null 2>&1 &
STREAMLIT_PID=$!

# Wait a moment for Streamlit to start
sleep 3

# Start Next.js
echo -e "${GREEN}Starting Next.js frontend...${NC}"
cd "$SCRIPT_DIR/frontend"
npm run dev > /dev/null 2>&1 &
NEXTJS_PID=$!

# Wait a moment for Next.js to start
sleep 3

echo -e "\n${GREEN}✅ Services are running!${NC}\n"
echo -e "${BLUE}📊 Streamlit App:${NC} http://localhost:8501 (PID: $STREAMLIT_PID)"
echo -e "${BLUE}🌐 Next.js Frontend:${NC} http://localhost:3000 (PID: $NEXTJS_PID)"
echo -e "${BLUE}🎯 Launch App Page:${NC} http://localhost:3000/app\n"
echo -e "${YELLOW}Press Ctrl+C to stop both services${NC}\n"

# Wait for both processes
wait
