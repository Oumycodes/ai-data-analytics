@echo off
echo Starting InsightForge Services...
echo.

REM Start Streamlit in a new window
start "Streamlit App" cmd /k "cd /d %~dp0 && streamlit run app.py"

REM Wait a moment
timeout /t 3 /nobreak >nul

REM Start Next.js in a new window
start "Next.js Frontend" cmd /k "cd /d %~dp0\frontend && npm run dev"

echo.
echo Services are starting...
echo Streamlit App: http://localhost:8501
echo Next.js Frontend: http://localhost:3000
echo Launch App Page: http://localhost:3000/app
echo.
echo Close the command windows to stop the services.
pause
